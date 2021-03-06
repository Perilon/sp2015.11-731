from __future__ import division
from collections import defaultdict

pig = open("/home/andrew/sp2015.11-731/hw1/pig3")
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
        for english_word in pair[1]:
            s_total[english_word] = 0
            for german_word in pair[0]:
                s_total[english_word] += translation_probability[(english_word, german_word)]

        for english_word in pair[1]:
            for german_word in pair[0]:
                ef_count[english_word, german_word] += (translation_probability[(english_word, german_word)]\
                                                         / s_total[english_word])
                f_total[german_word] += (translation_probability[(english_word, german_word)]\
                                                         / s_total[english_word])

    for german_word in german_wordset:
            for english_word in english_wordset:
                    translation_probability[(english_word, german_word)] \
                                                           = ef_count[(english_word, german_word)] / f_total[german_word]
