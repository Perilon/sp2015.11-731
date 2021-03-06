from __future__ import division
from collections import defaultdict

pig = open("/home/andrew/sp2015.11-731/hw1/pig")
corpus = pig.readlines()
bitext = [[sentence.strip().split() for sentence in pair.split(" ||| ")] for pair in corpus]

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
        translation_probability[(english_word, german_word)] = float(1/len(english_wordset))

ef_count = defaultdict(float)
f_total = defaultdict(float)

s_total = defaultdict(float)


def em():
    for pair in bitext:
       # print "------------------------------------------\nPair being considered: ", pair
        for english_word in pair[1]:
           # print "English word being considered: " + english_word
            s_total[english_word] = 0
           # print "s_total[" + english_word + "]: " + str(s_total[english_word])
            for german_word in pair[0]:
               # print "German word being considered: " + german_word
                s_total[english_word] += translation_probability[(english_word, german_word)]
               # print "New s_total[" + english_word + "]: " + str(s_total[english_word])
        #print "\n"
        
        for english_word in pair[1]:
          #  print "English word being reconsidered: " + english_word
            for german_word in pair[0]:
              #  print "German word being reconsidered: " + german_word
             #   print "ef_count[" + english_word + ", " + german_word + "]: " + str(ef_count[english_word, german_word])
              #  print "translation_probability[(" + english_word + ", " + german_word + ")]: " + str(translation_probability[(english_word, german_word)])
             #   print "s_total[" + english_word + "]: " + str(s_total[english_word])
                ef_count[english_word, german_word] += (translation_probability[(english_word, german_word)] / s_total[english_word])
              #  print "New ef_count[" + english_word + ", " + german_word + "]: " + str(ef_count[english_word, german_word])
              #  print "f_total[" + german_word + "]: " + str(f_total[german_word])
                f_total[german_word] += (translation_probability[(english_word, german_word)] / s_total[english_word])
              #  print "New f_total[" + german_word + "]: " + str(f_total[german_word])
              #  print "\n"
                
   # print "ESTIMATING PROBABILITIES\n---------------------------------------\n"
    for german_word in german_wordset:
      #  print "German word being re-reconsidered: " + german_word
        for english_word in english_wordset:
           # print "English word being re-reconsidered: " + english_word
           # print "translation_probability[(" + english_word + ", " + german_word + ")]: " + str(translation_probability[(english_word, german_word)])
           #print "ef_count[" + english_word + ", " + german_word + "]: " + str(ef_count[english_word, german_word])
          #  print "f_total[" + german_word + "]: " + str(f_total[german_word])
            translation_probability[(english_word, german_word)] = ef_count[(english_word, german_word)] / f_total[german_word]
           # print "New translation_probability[(" + english_word + ", " + german_word + ")]: " + str(translation_probability[(english_word, german_word)])
           # print "\n"
