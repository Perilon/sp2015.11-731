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

translation_probability = defaultdict(float)

for pair in bitext:
    for german_word in pair[0]:
        full_german_wordset.append(german_word)

for pair in bitext:
    for english_word in pair[1]:
        full_english_wordset.append(english_word)

english_wordset = set(full_english_wordset)
german_wordset = set(full_german_wordset)

for english_word in english_wordset:
    for german_word in german_wordset:
        translation_probability[(english_word, german_word)] = 0.2


def em():
    for iteration in range(opts.num_iter):
        ef_count = defaultdict(float)
        f_total = defaultdict(float)
        s_total = defaultdict(float)
        for pair in bitext:
            for english_word in pair[1]:
                s_total[english_word] = 0
            for english_word in pair[1]:
                for german_word in pair[0]:
                    s_total[english_word] += translation_probability[(english_word, german_word)]
            for english_word in pair[1]:
                for german_word in pair[0]:
                    ef_count[english_word, german_word] += translation_probability[(english_word, german_word)] / s_total[english_word]
                    f_total[german_word] += translation_probability[(english_word, german_word)] / s_total[english_word]
                    
        for german_word in german_wordset:
            for english_word in english_wordset:
                translation_probability[(english_word, german_word)] = ef_count[(english_word, german_word)] / f_total[german_word]


##def printmatches():
##    for pair in bitext[:150]:
##        matches = defaultdict(float)
##        for english_word in pair[1]:
##            for german_word in pair[0]:
##                matches[english_word, german_word] = translation_probability[(english_word, german_word)]
####        print "matches.items() = ", matches.items()
####        print "matches.keys() = ", matches.keys()
####        print "matches.values() = ", matches.values(), "\n"
##        
##        for (english_word_index, english_word) in enumerate(pair[1]):
##            ranking = []
##            for match in matches.items():
##                if match[0][0] == english_word:
##                    ranking.append(match[1])
##            best_match = max(ranking)
##            for match in matches.items():
##                if match[1] == best_match:
##                    german_choice = match[0][1]
##            sys.stdout.write(str(pair[0].index(german_choice)) + "-" + str(english_word_index) + " ")
##        sys.stdout.write("\n")


def printmatches3():
    for pair in bitext:
        for (english_word_index, english_word) in enumerate(pair[1]):
            best_match = 0
            best_score = 0
            for (german_word_index, german_word) in enumerate(pair[0]):
                if translation_probability[(english_word, german_word)] > best_score:
                    best_match = german_word_index
                    best_score = translation_probability[(english_word, german_word)]
            print str(best_match) + "-" + str(english_word_index),
        print "\n"

em()
printmatches3()
