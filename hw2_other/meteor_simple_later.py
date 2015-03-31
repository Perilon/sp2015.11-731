#!/usr/bin/env python
from __future__ import division
import argparse # optparse is deprecated
from itertools import islice # slicing for iterators

function_words = ["you", "i", "to", "the", "a", "and", "that", "it", "of", "me", "what", "is", "in", "this", "know", "i'm", "for", "no", "have", "my", "don't", "just", "not", "do", "be", "on", "your", "was", "we", "it's", "with", "so", "but", "all", "well", "are", "he", "oh", "about", "right", "you're", "get", "here", "out", "going", "like", "yeah", "if", "her", "she", "can", "up", "want", "think", "that's", "now", "go", "him", "at", "how", "got", "there", "one", "did", "why", "see", "come", "good", "they", "really", "as", "would", "look", "when", "time", "will", "okay", "back", "can't", "mean", "tell", "i'll", "from", "hey", "were", "he's", "could", "didn't", "yes", "his", "been", "or", "something", "who", "because", "some", "had", "then", "say", "ok"]

alpha = 0.85
delta = 0.75
 
# DRY
def word_matches(h, ref):
    return sum(1 for w in h if w in ref)
    # or sum(w in ref for w in f) # cast bool -> int
    # or sum(map(ref.__contains__, h)) # ugly!
 
def main():
    parser = argparse.ArgumentParser(description='Evaluate translation hypotheses.')
    # PEP8: use ' and not " for strings
    parser.add_argument('-i', '--input', default='data/train-test.hyp1-hyp2-ref',
            help='input file (default data/train-test.hyp1-hyp2-ref)')
    parser.add_argument('-n', '--num_sentences', default=None, type=int,
            help='Number of hypothesis pairs to evaluate')
    # note that if x == [1, 2, 3], then x[:None] == x[:] == x (copy); no need for sys.maxint
    opts = parser.parse_args()
 
    # we create a generator and avoid loading all sentences into a list
    def sentences():
        with open(opts.input) as f:
            for pair in f:
                yield [sentence.strip().split() for sentence in pair.split(' ||| ')]

    def function_count(sentence):
	count = 0
	for word in sentence:
		if word.lower() in function_words:
			count += 1
	return count

 
    # note: the -n option does not work in the original code
    for h1, h2, ref in islice(sentences(), opts.num_sentences):
##-----------------------------------------------------------
	ref_content_words = []
	ref_function_words = []

	for word in ref:
		if word in function_words:
			ref_function_words.append(word)
		else:
			ref_content_words.append(word)

	ref_function_set = set(ref_function_words)
	ref_content_set = set(ref_content_words)

	count_ref_function = len(ref_function_set)
	count_ref_content = len(ref_content_set)
##-----------------------------------------------------------
	h1_content_words = []
	h1_function_words = []

	for word in h1:
		if word in function_words:
			h1_function_words.append(word)
		else:
			h1_content_words.append(word)

	h1_function_set = set(h1_function_words)
	h1_content_set = set(h1_content_words)

	count_h1_function = len(h1_function_set)
	count_h1_content = len(h1_content_set)
##-----------------------------------------------------------
	h2_content_words = []
	h2_function_words = []

	for word in h2:
		if word in function_words:
			h2_function_words.append(word)
		else:
			h2_content_words.append(word)

	h2_function_set = set(h2_function_words)
	h2_content_set = set(h2_content_words)

	count_h2_function = len(h2_function_set)
	count_h2_content = len(h2_content_set)
##-----------------------------------------------------------
	count_h1_ref_content_shared = 0
	count_h1_ref_function_shared = 0
	
	for word in h1_content_set:
		if word in ref_content_set:
			count_h1_ref_content_shared += 1

	for word in h1_function_set:
		if word in ref_function_set:
			count_h1_ref_function_shared += 1
##-----------------------------------------------------------
	count_h2_ref_content_shared = 0
	count_h2_ref_function_shared = 0
	
	for word in h2_content_set:
		if word in ref_content_set:
			count_h2_ref_content_shared += 1

	for word in h2_function_set:
		if word in ref_function_set:
			count_h2_ref_function_shared += 1
##-----------------------------------------------------------
	h1_precision_numerator = (delta * count_h1_ref_content_shared) + ((1 - delta) * count_h1_ref_function_shared)
	h1_precision_denominator = (delta * count_h1_content) + ((1 - delta) * count_h1_function)
	h1_precision = h1_precision_numerator / h1_precision_denominator

	h1_recall_numerator = (delta * count_h1_ref_content_shared) + ((1 - delta) * count_h1_ref_function_shared)
	h1_recall_denominator = (delta * count_ref_content) + ((1 - delta) * count_ref_function)
	h1_recall = h1_recall_numerator / h1_recall_denominator
##-----------------------------------------------------------
	h2_precision_numerator = (delta * count_h2_ref_content_shared) + ((1 - delta) * count_h2_ref_function_shared)
	h2_precision_denominator = (delta * count_h2_content) + ((1 - delta) * count_h2_function)
	h2_precision = (h2_precision_numerator) / (h2_precision_denominator)

	h2_recall_numerator = (delta * count_h2_ref_content_shared) + ((1 - delta) * count_h2_ref_function_shared)
	h2_recall_denominator = (delta * count_ref_content) + ((1 - delta) * count_ref_function)
	h2_recall = (h2_recall_numerator) / (h2_recall_denominator)
##-----------------------------------------------------------

   	f_mean_h1 = ((h1_precision * h1_recall) + 0.001) / (((alpha * h1_precision) + ((1 - alpha) * h1_recall)) + 0.001)
   	f_mean_h2 = ((h2_precision * h1_recall) + 0.001) / (((alpha * h2_precision) + ((1 - alpha) * h2_recall)) + 0.001)

	if f_mean_h1 / f_mean_h2 > 1.002:
		print -1
	elif f_mean_h1 / f_mean_h2 <= 1.002 and f_mean_h1 / f_mean_h2 >= 0.998:
		print 0
	else:
		print 1

 
# convention to allow import of this file as a module
if __name__ == '__main__':
    main()
