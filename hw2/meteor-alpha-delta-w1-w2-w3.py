#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse # optparse is deprecated
from itertools import islice # slicing for iterators
from collections import Counter
import nltk
from nltk.stem.porter import *
import codecs
stemmer = PorterStemmer()
from nltk.corpus import wordnet as wn

function_words = ["you", "i", "to", "the", "a", "and", "that", "it", "of", "me", "what", "is", "in", "this", "know", "i'm", "for", "no", "have", "my", "don't", "just", "not", "do", "be", "on", "your", "was", "we", "it's", "with", "so", "but", "all", "well", "are", "he", "oh", "about", "right"]

C_function = Counter(function_words)
for item in C_function.keys():
        C_function[item] = 20

def harmonic_mean(P, R, alpha):
        denominator = (alpha * P + (1 - alpha) * R)
        if denominator == 0: return 0.0
        return P * R / denominator

def simple_meteor(hypothesis, reference, alpha, delta, w_exact, w_stems, w_synonyms):

        exact_match_function = (Counter(hypothesis) & Counter(reference)) & C_function
        exact_match_content = (Counter(hypothesis) & Counter(reference)) - exact_match_function
        
        exact_match_function_count = float(sum(exact_match_function.viewvalues()))
        exact_match_content_count = float(sum(exact_match_content.viewvalues()))

        nonexact_function_hyp = (Counter(hypothesis) - (Counter(reference) & Counter(hypothesis))) & C_function
        nonexact_content_hyp = (Counter(hypothesis) - (Counter(reference) & Counter(hypothesis))) - nonexact_function_hyp

        nonexact_function_ref = (Counter(reference) - (Counter(reference) & Counter(hypothesis))) & C_function
        nonexact_content_ref = (Counter(reference) - (Counter(reference) & Counter(hypothesis))) - nonexact_function_ref

        nonexact_f_stems_hyp, nonexact_c_stems_hyp, nonexact_f_stems_ref, nonexact_c_stems_ref, \
                              orig_word_f_hyp, orig_word_c_hyp, orig_word_f_ref, orig_word_c_ref = [], [], [], [], [], [], [], []

        for word in nonexact_function_hyp.keys():
                        nonexact_f_stems_hyp.append(stemmer.stem(word))
        for word in nonexact_content_hyp.keys():
                        nonexact_c_stems_hyp.append(stemmer.stem(word))
        for word in nonexact_function_ref.keys():
                        nonexact_f_stems_ref.append(stemmer.stem(word))
        for word in nonexact_content_ref.keys():
                        nonexact_c_stems_ref.append(stemmer.stem(word))

        nonexact_match_function = Counter(nonexact_f_stems_hyp) & Counter(nonexact_f_stems_ref)
        nonexact_match_content = Counter(nonexact_c_stems_hyp) & Counter(nonexact_c_stems_ref)

        for word in nonexact_function_hyp.keys():
                if stemmer.stem(word) in nonexact_match_function.keys():
                        orig_word_f_hyp.append(word)
        for word in nonexact_content_hyp.keys():
                if stemmer.stem(word) in nonexact_match_content.keys():
                        orig_word_c_hyp.append(word)
        for word in nonexact_function_ref.keys():
                if stemmer.stem(word) in nonexact_match_function.keys():
                        orig_word_f_ref.append(word)
        for word in nonexact_content_ref.keys():
                if stemmer.stem(word) in nonexact_match_content.keys():
                        orig_word_c_ref.append(word)

        nonexact_match_function_count = float(sum(nonexact_match_function.viewvalues()))
        nonexact_match_content_count = float(sum(nonexact_match_content.viewvalues()))

        def Precision2(delta, w_exact, w_stems, exact_match_content_count, exact_match_function_count, hypothesis):
                if len(hypothesis) == 0: return 0.0
                else:
                        return ((w_exact * ((delta * exact_match_content_count) + ((1 - delta) * exact_match_function_count))) \
                                + (w_stems * ((delta * nonexact_match_content_count) + ((1 - delta) * nonexact_match_function_count)))) / len(hypothesis)

        def Recall2(delta, w_exact, w_stems, exact_match_content_count, exact_match_function_count, reference):
                if len(reference) == 0: return 0.0
                else:
                        return ((w_exact * ((delta * exact_match_content_count) + ((1 - delta) * exact_match_function_count))) \
                                + (w_stems * ((delta * nonexact_match_content_count) + ((1 - delta) * nonexact_match_function_count)))) / len(reference)

        P2 = Precision2(delta, w_exact, w_stems, exact_match_content_count, exact_match_function_count, hypothesis)
        R2 = Recall2(delta, w_exact, w_stems, exact_match_content_count, exact_match_function_count, reference)

#   -------------------------------------------------------------------------------------------

        Leftover_function_hyp = nonexact_function_hyp - nonexact_match_function - Counter(orig_word_f_hyp)
        Leftover_content_hyp = nonexact_content_hyp - nonexact_match_content - Counter(orig_word_c_hyp)

        Leftover_function_ref = nonexact_function_ref - nonexact_match_function - Counter(orig_word_f_ref)
        Leftover_content_ref = nonexact_content_ref - nonexact_match_content - Counter(orig_word_c_ref)

        def path_similarity(word1, word2):
                if wn.synsets(word1) != [] and wn.synsets(word2) != []:
                        path_similarity_dict = {}
                        synstrings1_list = []
                        for item in wn.synsets(word1):
                                synstrings1_list.append(str(item))
                        synstrings2_list = []
                        for item in wn.synsets(word2):
                                synstrings2_list.append(str(item))
                        synsets1_list = []
                        synsets2_list = []
                        for item1 in synstrings1_list:
                                synsets1_list.append( wn.synset(item1[item1.find("(")+2:item1.find(")")-1]) )
                        for item2 in synstrings2_list:
                                synsets2_list.append( wn.synset(item2[item2.find("(")+2:item2.find(")")-1]) )
                        for item1 in synsets1_list:
                                for item2 in synsets2_list:
                                        path_similarity_dict[(item1, item2)] = item1.path_similarity(item2)
                        best_match = max(path_similarity_dict.values())
                        best_matches = []
                        for item in path_similarity_dict.items():
                                if item[1] == best_match:
                                        best_matches.append(item)
                                return best_match

##        print "Leftover_content_hyp = ", Leftover_content_hyp
##        print "Leftover_content_ref = ", Leftover_content_ref

        def find_synonyms(Leftover_content_hyp, Leftover_content_ref):
                best_synonyms_dict = {}
                word1_scores = {}
                if len(Leftover_content_hyp) != 0 and len(Leftover_content_ref) != 0:
                        for word1 in Leftover_content_hyp:
                                word1_scores[word1] = 0
                                for word2 in Leftover_content_ref:
                                        sim = path_similarity(word1, word2)
                                        best_match_of_word1 = None
                                        if sim > word1_scores[word1]:
                                                word1_scores[word1] = sim
                                                best_match_of_word1 = word2
                                best_synonyms_dict[(word1, best_match_of_word1)] = word1_scores[word1]
                        return best_synonyms_dict
                else:
                        return best_synonyms_dict

        content_synonyms_hyp = []
        content_synonyms_ref = []

        for possibility in find_synonyms(Leftover_content_hyp, Leftover_content_ref).items():
                if possibility[1] >= .4:
                        content_synonyms_hyp.append(possibility[0][0])
                        content_synonyms_ref.append(possibility[0][1])

        content_synonyms_hyp = Counter(content_synonyms_hyp)
        content_synonyms_ref = Counter(content_synonyms_ref)

        content_synonyms_count = float(sum(content_synonyms_hyp.viewvalues()))
        function_synonyms_count = 0.0
    

        def Precision3(delta, w_exact, w_stems, w_synonyms, hypothesis):
                if len(hypothesis) == 0: return 0.0
                else:
                        return ((w_exact * ((delta * exact_match_content_count) + ((1 - delta) * exact_match_function_count))) \
                   + (w_stems * ((delta * nonexact_match_content_count) + ((1 - delta) * nonexact_match_function_count))) \
                    + (w_synonyms * ((delta * content_synonyms_count) + ((1 - delta) * function_synonyms_count)))) / len(hypothesis)

        def Recall3(delta, w_exact, w_stems, w_synonyms, reference):
                if len(reference) == 0: return 0.0
                else:
                        return ((w_exact * ((delta * exact_match_content_count) + ((1 - delta) * exact_match_function_count))) \
                                + (w_stems * ((delta * nonexact_match_content_count) + ((1 - delta) * nonexact_match_function_count))) \
                                + (w_synonyms * ((delta * content_synonyms_count) + ((1 - delta) * function_synonyms_count)))) / len(reference)

        P3 = Precision3(delta, w_exact, w_stems, w_synonyms, hypothesis)
        R3 = Recall3(delta, w_exact, w_stems, w_synonyms, reference)

        return harmonic_mean(P3, R3, alpha)
 
def main():
        parser = argparse.ArgumentParser(description='Evaluate translation hypotheses.')
        # PEP8: use ' and not " for strings
        parser.add_argument('-i', '--input', default='data/train-test.hyp1-hyp2-ref',
                help='input file (default data/train-test.hyp1-hyp2-ref)')
        parser.add_argument('-n', '--num_sentences', default=None, type=int,
                help='Number of hypothesis pairs to evaluate')
        parser.add_argument('-a', '--alpha', default=0.5, type=float, help='precision/recall weight parameter')
        parser.add_argument('-d', '--delta', default=0.5, type=float, help='content/function word weight parameter')
        parser.add_argument('-w1', '--w_exact', default=1, type=float, help='exact matches matcher weight')
        parser.add_argument('-w2', '--w_stems', default=.6, type=float, help='stemmed matches matcher weight')
        parser.add_argument('-w3', '--w_synonyms', default = .8, type=float, help='synonym matches matcher weight')
        # note that if x == [1, 2, 3], then x[:None] == x[:] == x (copy); no need for sys.maxint
        opts = parser.parse_args()
 
        # we create a generator and avoid loading all sentences into a list
        def sentences():
                with open(opts.input) as f:
                        for pair in f:
                                yield [sentence.decode('UTF-8').strip().split() for sentence in pair.translate(None, """~`!@#$%^&*()_+-={}[]:;"'<>?,./\\""").lower().split(' ||| ')]
 
        # note: the -n option does not work in the original code
        for h1, h2, reference in islice(sentences(), opts.num_sentences):
                h1_val = simple_meteor(h1, reference, opts.alpha, opts.delta, opts.w_exact, opts.w_stems, opts.w_synonyms)
                h2_val = simple_meteor(h2, reference, opts.alpha, opts.delta, opts.w_exact, opts.w_stems, opts.w_synonyms)

                if h1_val != 0 and h2_val != 0:
                        if (h1_val / h2_val) > 1.0002:
                                print -1
                        elif (h1_val / h2_val) <= 1.0002 and (h1_val / h2_val) >= 0.9998:
                                print 0
                        else:
                                print 1
                elif h2_val == 0:
                        print -1
                else:
                        print 1
 
# convention to allow import of this file as a module
#if __name__ == '__main__':
main()
