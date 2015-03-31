#!/usr/bin/env python
from __future__ import division
import argparse # optparse is deprecated
from itertools import islice # slicing for iterators
 
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

    alpha = 0.5
 
    # we create a generator and avoid loading all sentences into a list
    def sentences():
        with open(opts.input) as f:
            for pair in f:
                yield [sentence.strip().split() for sentence in pair.split(' ||| ')]
 
    # note: the -n option does not work in the original code
    for h1, h2, ref in islice(sentences(), opts.num_sentences):
        rset = set(ref)
	h1_match = word_matches(h1, rset)
	h2_match = word_matches(h2, rset)
    
   	h1_precision = h1_match / len(h1)
   	h1_recall = h1_match / len(rset)

   	h2_precision = h2_match / len(h2)
   	h2_recall = h2_match / len(rset)

   	f_mean_h1 = (h1_precision * h1_recall) / (((h1_precision * alpha) + 0.01) * ((h1_recall * (1 - alpha)) + 0.09))
   	f_mean_h2 = (h2_precision * h2_recall) / (((h2_precision * alpha) + 0.01) * ((h2_recall * (1 - alpha)) + 0.09))


	if f_mean_h2 != 0 and f_mean_h1 != 0:
		if (f_mean_h1 / f_mean_h2) > 1.0005:
			print -1
		elif (f_mean_h1 / f_mean_h2) <= 1.0005 and (f_mean_h1 / f_mean_h2) >= 0.9995:
			print 0
		else:
			print 1
	elif f_mean_h2 == 0:
		print -1
	else:
		print 1

 
# convention to allow import of this file as a module
if __name__ == '__main__':
    main()
