#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse # optparse is deprecated
from itertools import islice # slicing for iterators
from collections import Counter
import nltk
from nltk.stem.porter import *
import codecs
stemmer = PorterStemmer()

function_words = ["you", "i", "to", "the", "a", "and", "that", "it", "of", "me", "what", "is", "in", "this", "know", "i'm", "for", "no", "have", "my", "don't", "just", "not", "do", "be", "on", "your", "was", "we", "it's", "with", "so", "but", "all", "well", "are", "he", "oh", "about", "right"]

C_function = Counter(function_words)
for item in C_function.keys():
        C_function[item] = 20

def harmonic_mean(P, R, alpha):
        denominator = (alpha * P + (1 - alpha) * R)
        if denominator == 0: return 0.0
        return P * R / denominator

def simple_meteor(hypothesis, reference, alpha, delta, w_exact, w_stems):

        exact_match_function = (Counter(hypothesis) & Counter(reference)) & C_function
        exact_match_content = (Counter(hypothesis) & Counter(reference)) - exact_match_function

##      print "exact_match_function = ", exact_match_function
##      print "exact_match_content = ", exact_match_content
        
        exact_match_function_count = float(sum(exact_match_function.viewvalues()))
        exact_match_content_count = float(sum(exact_match_content.viewvalues()))

##      print "exact_match_function_count = ", exact_match_function_count
##      print "exact_match_content_count = ", exact_match_content_count

        nonexact_function_hyp = (Counter(hypothesis) - (Counter(reference) & Counter(hypothesis))) & C_function
        nonexact_content_hyp = (Counter(hypothesis) - (Counter(reference) & Counter(hypothesis))) - nonexact_function_hyp
##      print "nonexact_function_hyp = ", nonexact_function_hyp
##      print "nonexact_content_hyp = ", nonexact_content_hyp

        nonexact_function_ref = (Counter(reference) - (Counter(reference) & Counter(hypothesis))) & C_function
        nonexact_content_ref = (Counter(reference) - (Counter(reference) & Counter(hypothesis))) - nonexact_function_ref
##      print "nonexact_function_ref = ",  nonexact_function_ref
##      print "nonexact_content_ref = ", nonexact_content_ref

        nonexact_f_stems_hyp = []
        nonexact_c_stems_hyp = []
        nonexact_f_stems_ref = []
        nonexact_c_stems_ref = []

        for word in nonexact_function_hyp.keys():
                        nonexact_f_stems_hyp.append(stemmer.stem(word))
        for word in nonexact_content_hyp.keys():
                        nonexact_c_stems_hyp.append(stemmer.stem(word))
        for word in nonexact_function_ref.keys():
                        nonexact_f_stems_ref.append(stemmer.stem(word))
        for word in nonexact_content_ref.keys():
                        nonexact_c_stems_ref.append(stemmer.stem(word))
##      print "nonexact_f_stems_hyp = ", nonexact_f_stems_hyp
##      print "nonexact_c_stems_hyp = ", nonexact_c_stems_hyp
##      print "nonexact_f_stems_ref = ", nonexact_f_stems_ref
##      print "nonexact_c_stems_ref = ", nonexact_c_stems_ref

        nonexact_match_function = Counter(nonexact_f_stems_hyp) & Counter(nonexact_f_stems_ref)
        nonexact_match_content = Counter(nonexact_c_stems_hyp) & Counter(nonexact_c_stems_ref)
##      print "nonexact_match_function = ", nonexact_match_function
##      print "nonexact_match_content = ", nonexact_match_content

        nonexact_match_function_count = float(sum(nonexact_match_function.viewvalues()))
        nonexact_match_content_count = float(sum(nonexact_match_content.viewvalues()))

##      print "nonexact_match_function_count = ", nonexact_match_function_count
##      print "nonexact_match_content_count = ", nonexact_match_content_count

##        def Precision(delta, exact_match_content_count, exact_match_function_count, hypothesis):
##                if len(hypothesis) == 0: return 0.0
##                else:
##                        return ((delta * exact_match_content_count) + ((1 - delta) * exact_match_function_count)) / len(hypothesis)
##
##        def Recall(delta, exact_match_content_count, exact_match_function_count, reference):
##                if len(reference) == 0: return 0.0
##                else:
##                        return ((delta * exact_match_content_count) + ((1 - delta) * exact_match_function_count)) / len(reference)

##        P = Precision(delta, exact_match_content_count, exact_match_function_count, hypothesis)
##        R = Recall(delta, exact_match_content_count, exact_match_function_count, reference)

##      print "Precision = ", P
##      print "Recall = ", R
##
##      print "Harmonic mean = ", harmonic_mean(P, R, alpha)

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
        
##      print "Precision2 = ", P2
##      print "Recall2 = ", R2
##
##      print "Harmonic mean 2 = ", harmonic_mean(P2, R2, alpha)

        return harmonic_mean(P2, R2, alpha)
 
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
        # note that if x == [1, 2, 3], then x[:None] == x[:] == x (copy); no need for sys.maxint
        opts = parser.parse_args()
 
        # we create a generator and avoid loading all sentences into a list
        def sentences():
                with open(opts.input) as f:
                        for pair in f:
                                yield [sentence.decode('UTF-8').strip().split() for sentence in pair.translate(None, """.,'"?:;/\*!-""").lower().split(' ||| ')]
 
        # note: the -n option does not work in the original code
        for h1, h2, reference in islice(sentences(), opts.num_sentences):
                h1_val = simple_meteor(h1, reference, opts.alpha, opts.delta, opts.w_exact, opts.w_stems)
                h2_val = simple_meteor(h2, reference, opts.alpha, opts.delta, opts.w_exact, opts.w_stems)

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
