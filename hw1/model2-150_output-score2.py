#!/usr/bin/env python
from __future__ import division
import optparse
import sys
from collections import defaultdict

optparser = optparse.OptionParser()
optparser.add_option("-b", "--bitext", dest="bitext", default="data/dev-test-train.de-en", help="Parallel corpus (default data/dev-test-train.de-en)")
optparser.add_option("-t", "--threshold", dest="threshold", default=0.5, type="float", help="Threshold for aligning with Dice's coefficient (default=0.5)")
optparser.add_option("-n", "--num_sentences", dest="num_sents", default=sys.maxint, type="int", help="Number of sentences to use for training and alignment")
optparser.add_option("-i", "--num_iterations", dest="num_iter", default=5, type="int", help="Number of iterations")
(opts, _) = optparser.parse_args()

full_bitext = [[sentence.strip().split() for sentence in pair.split(' ||| ')] for pair in open(opts.bitext)]
bitext = full_bitext[:opts.num_sents]


full_english_wordset = []
full_german_wordset = []

translation_probability = defaultdict(lambda: defaultdict(float))

for pair in bitext:
    for german_word in pair[0]:
        full_german_wordset.append(german_word)

for pair in bitext:
    for english_word in pair[1]:
        full_english_wordset.append(english_word)

english_wordset = set(full_english_wordset)
german_wordset = set(full_german_wordset)


for pair in bitext:
    for german_word in pair[0]:
        for english_word in pair[1]:
            translation_probability[(english_word, german_word)] = 0.2


def em():
    for iteration in range(opts.num_iter):
        ef_count = defaultdict(float)
        f_total = defaultdict(float)
        s_total = defaultdict(lambda: defaultdict(float))
        for pair in bitext:
            for english_word in pair[1]:
                s_total[english_word] = 0

                for german_word in pair[0]:
                    s_total[english_word] += translation_probability[(english_word, german_word)]

                for german_word in pair[0]:
                    ef_count[english_word, german_word] += translation_probability[(english_word, german_word)] #/ s_total[english_word]
                    f_total[german_word] += translation_probability[(english_word, german_word)] / s_total[english_word]
                    
        for pair in bitext:
            for german_word in pair[0]:
                for english_word in pair[1]:
                    translation_probability[(english_word, german_word)] = ef_count[(english_word, german_word)] / f_total[german_word]

    ##----------------------------Model 2 part------------------------                
    aijLeLf = defaultdict(float)
    f_total = defaultdict(float)
    
    for pair in bitext:
        Le = len(pair[1])
        Lf = len(pair[0])
        for j in range(Le):
            for i in range(Lf):
                aijLeLf[(i, j, Le, Lf)] = 1/(Lf)
                
##    for item in aijLeLf.items()[:10]:
##        sys.stdout.write(str(item) + "\n")
##    sys.stdout.write(str( aijLeLf[(39, 35, 75, 75)]) + "\n")
##    sys.stdout.write(str( type(aijLeLf[(39, 35, 75, 75)])) + "\n")
    
##    for item in translation_probability.items()[:10]:
##        sys.stdout.write(str(item) + "\n")
##    sys.stdout.write(str ( translation_probability[("draw", "auf")]) + "\n")

    for iteration in range(opts.num_iter):
        ef_count = defaultdict(float)
        f_total = defaultdict(float)
        count_a_ijLeLf = defaultdict(float)
        count_a_ijLeLf[(i, j, Le, Lf)] = 0
        total_a_jLeLf = defaultdict(float)
        total_a_jLeLf[(j, Le, Lf)] = 0
        s_total = defaultdict(float)

        for pair in bitext:
            Le = len(pair[1])
            Lf = len(pair[0])

##            sys.stdout.write(str(Le) + "\n")
##            sys.stdout.write(str(Lf) + "\n")

            for j in range(Le):
##                s_total = defaultdict(float)
                s_total[pair[1][j]] = 0

##                sys.stdout.write(str(s_total.items()) + "\n")
##                sys.stdout.write(str( s_total[pair[1][j]]) + "\n")
##                s_total[pair[1][j]] += 1
##                sys.stdout.write(str( s_total[pair[1][j]]) + "\n")
                
                for i in range(Lf):
##                    sys.stdout.write(str( translation_probability[(pair[1][j], pair[0][1])]) + "\n")
                    s_total[pair[1][j]] += (translation_probability[(pair[1][j], pair[0][i])] * aijLeLf[(i, j, Le, Lf)])
                        
            for j in range(Le):
                
                for i in range(Lf):
                    c = translation_probability[(pair[1][j], pair[0][i])]  * aijLeLf[(i, j, Le, Lf)] / s_total[pair[1][j]]
                    ef_count[(pair[1][j], pair[0][i])] += c
                    f_total[pair[0][i]] += c
                    count_a_ijLeLf[(i, j, Le, Lf)] += c
                    total_a_jLeLf[(j, Le, Lf)] += c
                    
        for item in translation_probability.keys():
            translation_probability[item] = 0
        for item in aijLeLf.keys():
            aijLeLf[item] = 0
            
        for item in translation_probability.keys():
            translation_probability[item] = ef_count[item] / f_total[item[1]]

        for item in aijLeLf.keys():
            aijLeLf[item] = count_a_ijLeLf[item] / total_a_jLeLf[(item[1], item[2], item[3])]    
    

def printmatches3():
    for pair in full_bitext[:150]:
        for (english_word_index, english_word) in enumerate(pair[1]):
            best_score = 0
            for (german_word_index, german_word) in enumerate(pair[0]):
                if translation_probability[(english_word, german_word)] > best_score:
                    best_match = german_word_index
                    best_score = translation_probability[(english_word, german_word)]
            sys.stdout.write(str(best_match) + "-" + str(english_word_index) + " ")
        sys.stdout.write("\n")

em()
printmatches3()
