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

def harmonic_mean(P, R, alpha):
        denominator = (alpha * P + (1 - alpha) * R)
        if denominator == 0: return 0.0
        return P * R / denominator

def simple_meteor(hypothesis, reference, alpha, delta_nouns, delta_verbs, delta_adjadvs, delta_other, w_exact, w_stems, w_synonyms):

        hyp_temp, ref_temp = [], []
        hyp_temp.append(nltk.pos_tag(hypothesis))
        ref_temp.append(nltk.pos_tag(reference))

##        print "hypothesis = ", hypothesis, len(hypothesis), "\n"
##        print "reference = ", reference, len(reference), "\n"

        hyp_nouns, ref_nouns, hyp_verbs, ref_verbs, hyp_adjadvs, ref_adjadvs, hyp_other, ref_other = [], [], [], [], [], [], [], []
        
        for item in hyp_temp[0]:
                if item[1] in ["NN", "NNS", "NNP", "NNPS", "PRP", "PRP$", "WP", "WP$"]:
                        hyp_nouns.append(item[0])
                elif item[1] in ["MD", "VB", "VBD", "DBG", "VBN", "VBP", "VBZ"]:
                        hyp_verbs.append(item[0])
                elif item[1] in ["JJ", "JJR", "JJS", "RB", "RBR", "RBS"]:
                        hyp_adjadvs.append(item[0])
                else:
                        hyp_other.append(item[0])
                        
        for item in ref_temp[0]:
                if item[1] in ["NN", "NNS", "NNP", "NNPS", "PRP", "PRP$", "WP", "WP$"]:
                        ref_nouns.append(item[0])
                elif item[1] in ["MD", "VB", "VBD", "DBG", "VBN", "VBP", "VBZ"]:
                        ref_verbs.append(item[0])
                elif item[1] in ["JJ", "JJR", "JJS", "RB", "RBR", "RBS"]:
                        ref_adjadvs.append(item[0])
                else:
                        ref_other.append(item[0])

        exact_noun_matches = Counter(hyp_nouns) & Counter(ref_nouns)
        count_exact_noun_matches = float(sum(exact_noun_matches.viewvalues()))
##        print "exact_noun_matches = ", exact_noun_matches
##        print "count_exact_noun_matches = ", count_exact_noun_matches
        
        exact_verb_matches = Counter(hyp_verbs) & Counter(ref_verbs)
        count_exact_verb_matches = float(sum(exact_verb_matches.viewvalues()))
##        print "exact_verb_matches = ", exact_verb_matches
##        print "count_exact_verb_matches = ", count_exact_verb_matches

        exact_adjadv_matches = Counter(hyp_adjadvs) & Counter(ref_adjadvs)
        count_exact_adjadv_matches = float(sum(exact_adjadv_matches.viewvalues()))
##        print "exact_adjadv_matches = ", exact_adjadv_matches
##        print "count_exact_adjadv_matches = ", count_exact_adjadv_matches

        exact_other_matches = Counter(hyp_other) & Counter(ref_other)
        count_exact_other_matches = float(sum(exact_other_matches.viewvalues()))
##        print "exact_other_matches = ", exact_other_matches
##        print "count_exact_other_matches = ", count_exact_other_matches
        

        Leftover_hyp_nouns = Counter(hyp_nouns) - (Counter(hyp_nouns) & Counter(ref_nouns))
        Leftover_hyp_verbs = Counter(hyp_verbs) - (Counter(hyp_verbs) & Counter(ref_verbs))
        Leftover_hyp_adjadvs = Counter(hyp_adjadvs) - (Counter(hyp_adjadvs) & Counter(ref_adjadvs))
        Leftover_hyp_other = Counter(hyp_other) - (Counter(hyp_other) & Counter(ref_other))
##        print "Leftover_hyp_nouns = ", Leftover_hyp_nouns
##        print "Leftover_hyp_verbs = ", Leftover_hyp_verbs
##        print "Leftover_hyp_adjadvs = ", Leftover_hyp_adjadvs
##        print "Leftover_hyp_other = ", Leftover_hyp_other

        Leftover_ref_nouns = Counter(ref_nouns) - (Counter(hyp_nouns) & Counter(ref_nouns))
        Leftover_ref_verbs = Counter(ref_verbs) - (Counter(hyp_verbs) & Counter(ref_verbs))
        Leftover_ref_adjadvs = Counter(ref_adjadvs) - (Counter(hyp_adjadvs) & Counter(ref_adjadvs))
        Leftover_ref_other = Counter(ref_other) - (Counter(hyp_other) & Counter(ref_other))
##        print "Leftover_ref_nouns = ", Leftover_ref_nouns
##        print "Leftover_ref_verbs = ", Leftover_ref_verbs
##        print "Leftover_ref_adjadvs = ", Leftover_ref_adjadvs
##        print "Leftover_ref_other = ", Leftover_ref_other

        hyp_nouns_stems, ref_nouns_stems, hyp_verbs_stems, ref_verbs_stems, \
                         hyp_adjadvs_stems, ref_adjadvs_stems, hyp_other_stems, ref_other_stems = \
                         [], [], [], [], [], [], [], []

        for item in Leftover_hyp_nouns:
                hyp_nouns_stems.append(stemmer.stem(item))
        for item in Leftover_hyp_verbs:
                hyp_verbs_stems.append(stemmer.stem(item))
        for item in Leftover_hyp_adjadvs:
                hyp_adjadvs_stems.append(stemmer.stem(item))
        for item in Leftover_hyp_other:
                hyp_other_stems.append(stemmer.stem(item))

        for item in Leftover_ref_nouns:
                ref_nouns_stems.append(stemmer.stem(item))
        for item in Leftover_ref_verbs:
                ref_verbs_stems.append(stemmer.stem(item))
        for item in Leftover_ref_adjadvs:
                hyp_adjadvs_stems.append(stemmer.stem(item))
        for item in Leftover_ref_other:
                ref_other_stems.append(stemmer.stem(item))

##        print "hyp_nouns_stems = ", hyp_nouns_stems
##        print "hyp_verbs_stems = ", hyp_verbs_stems
##        print "hyp_adjadvs_stems = ", hyp_adjadvs_stems
##        print "hyp_other_stems = ", hyp_other_stems, "\n"

##        print "ref_nouns_stems = ", ref_nouns_stems
##        print "ref_verbs_stems = ", ref_verbs_stems
##        print "ref_adjadvs_stems = ", ref_adjadvs_stems
##        print "ref_other_stems = ", ref_other_stems, "\n"

        stemmed_noun_matches = Counter(hyp_nouns_stems) & Counter(ref_nouns_stems)
        count_stemmed_noun_matches = float(sum(stemmed_noun_matches.viewvalues()))
##        print "stemmed_noun_matches = ", stemmed_noun_matches
##        print "count_stemmed_noun_matches = ", count_stemmed_noun_matches, "\n"
        
        stemmed_verb_matches = Counter(hyp_verbs_stems) & Counter(ref_verbs_stems)
        count_stemmed_verb_matches = float(sum(stemmed_verb_matches.viewvalues()))
##        print "stemmed_verb_matches = ", stemmed_verb_matches
##        print "count_stemmed_verb_matches = ", count_stemmed_verb_matches, "\n"

        stemmed_adjadv_matches = Counter(hyp_adjadvs_stems) & Counter(ref_adjadvs_stems)
        count_stemmed_adjadv_matches = float(sum(stemmed_adjadv_matches.viewvalues()))
##        print "stemmed_adjadv_matches = ", stemmed_adjadv_matches
##        print "count_stemmed_adjadv_matches = ", count_stemmed_adjadv_matches, "\n"
        
        stemmed_other_matches = Counter(hyp_other_stems) & Counter(ref_other_stems)
        count_stemmed_other_matches = float(sum(stemmed_other_matches.viewvalues()))
##        print "stemmed_other_matches = ", stemmed_other_matches
##        print "count_stemmed_other_matches = ", count_stemmed_other_matches, "\n"


        def Precision2(delta_nouns, delta_verbs, delta_other, w_exact, w_stems, count_exact_noun_matches, count_exact_verb_matches, \
                       count_exact_adjadv_matches, count_exact_other_matches, count_stemmed_noun_matches, count_stemmed_verb_matches, \
                       count_stemmed_adjadv_matches, count_stemmed_other_matches, hypothesis):
                if len(hypothesis) == 0: return 0.0
                else:
                        return ((w_exact * ((delta_nouns * count_exact_noun_matches) + (delta_verbs * count_exact_verb_matches) + \
                                            (delta_adjadvs * count_exact_adjadv_matches) + (delta_other * count_exact_other_matches))) \
                               + (w_stems * ((delta_nouns * count_stemmed_noun_matches) + (delta_verbs * count_stemmed_verb_matches) + \
                                             (delta_other * count_stemmed_adjadv_matches) + (delta_other * count_stemmed_other_matches)))) \
                               / len(hypothesis)

        def Recall2(delta_nouns, delta_verbs, delta_other, w_exact, w_stems, count_exact_noun_matches, count_exact_verb_matches, \
                       count_exact_adjadv_matches, count_exact_other_matches, count_stemmed_noun_matches, count_stemmed_verb_matches, \
                       count_stemmed_adjadv_matches, count_stemmed_other_matches, reference):
                if len(reference) == 0: return 0.0
                else:
                        return ((w_exact * ((delta_nouns * count_exact_noun_matches) + (delta_verbs * count_exact_verb_matches) + \
                                            (delta_adjadvs * count_exact_adjadv_matches) + (delta_other * count_exact_other_matches))) \
                               + (w_stems * ((delta_nouns * count_stemmed_noun_matches) + (delta_verbs * count_stemmed_verb_matches) + \
                                             (delta_other * count_stemmed_adjadv_matches) + (delta_other * count_stemmed_other_matches)))) \
                               / len(reference)

        P2 = Precision2(delta_nouns, delta_verbs, delta_other, w_exact, w_stems, count_exact_noun_matches, count_exact_verb_matches, \
                       count_exact_adjadv_matches, count_exact_other_matches, count_stemmed_noun_matches, count_stemmed_verb_matches, \
                       count_stemmed_adjadv_matches, count_stemmed_other_matches, hypothesis)
        R2 = Recall2(delta_nouns, delta_verbs, delta_other, w_exact, w_stems, count_exact_noun_matches, count_exact_verb_matches, \
                       count_exact_adjadv_matches, count_exact_other_matches, count_stemmed_noun_matches, count_stemmed_verb_matches, \
                       count_stemmed_adjadv_matches, count_stemmed_other_matches, reference)

##        print "P2 = ", P2
##        print "R2 = ", R2
##        print "harmonic_mean(P2, R2, alpha) = ", harmonic_mean(P2, R2, alpha), "\n", "--------------------------------------------------"
        return harmonic_mean(P2, R2, alpha)

#   -------------------------------------------------------------------------------------------
 
def main():
        parser = argparse.ArgumentParser(description='Evaluate translation hypotheses.')
        # PEP8: use ' and not " for strings
        parser.add_argument('-i', '--input', default='data/train-test.hyp1-hyp2-ref',
                help='input file (default data/train-test.hyp1-hyp2-ref)')
        parser.add_argument('-n', '--num_sentences', default=None, type=int,
                help='Number of hypothesis pairs to evaluate')
        parser.add_argument('-a', '--alpha', default=0.8, type=float, help='precision/recall weight parameter')
        parser.add_argument('-dn', '--delta_nouns', default=.40, type=float, help='noun weight parameter')
        parser.add_argument('-dv', '--delta_verbs', default=.25, type=float, help='verb weight parameter')
        parser.add_argument('-da', '--delta_adjadvs', default=.30, type=float, help='adjective/adverb weight parameter')
        parser.add_argument('-do', '--delta_other', default=.05, type=float, help='other weight parameter')
        
        parser.add_argument('-w1', '--w_exact', default=1, type=float, help='exact matches matcher weight')
        parser.add_argument('-w2', '--w_stems', default=.8, type=float, help='stemmed matches matcher weight')
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
                h1_val = simple_meteor(h1, reference, opts.alpha, opts.delta_nouns, opts.delta_verbs, \
                                       opts.delta_adjadvs, opts.delta_other, opts.w_exact, opts.w_stems, opts.w_synonyms)
                h2_val = simple_meteor(h2, reference, opts.alpha, opts.delta_nouns, opts.delta_verbs, \
                                       opts.delta_adjadvs, opts.delta_other, opts.w_exact, opts.w_stems, opts.w_synonyms)

                if h1_val != 0 and h2_val != 0:
                        if (h1_val / h2_val) > 1.0002:
                                print -1
                        elif (h1_val / h2_val) <= 1.0003 and (h1_val / h2_val) >= 0.9997:
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
