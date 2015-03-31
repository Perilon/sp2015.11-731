#!/usr/bin/env python
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
 
    # we create a generator and avoid loading all sentences into a list
    def sentences():
        with open(opts.input) as f:
            for pair in f:
                yield [sentence.strip().split() for sentence in pair.split(' ||| ')]

    alpha = 0.85
 
    # note: the -n option does not work in the original code
    for h1, h2, ref in islice(sentences(), opts.num_sentences):
        rset = set(ref)

        h1_match = word_matches(h1, rset)
        h2_match = word_matches(h2, rset)

	h1_precision = (h1_match + 1) / (len(h1) + 1)
	h1_recall = (h1_match + 1) / (len(rset) + 1)

	h2_precision = (h2_match + 1) / (len(h2) + 1)
	h2_recall = (h2_match + 1) / (len(rset) + 1)

	f_mean_h1 = ((h1_precision * h1_recall) + .001) / (((alpha * h1_precision) + ((alpha-1) * h1_recall)) + .001)
	f_mean_h2 = ((h2_precision * h2_recall) + .001) / (((alpha * h2_precision) + ((alpha-1) * h2_recall)) + .001)
	

        print(-1 if (f_mean_h1 / f_mean_h2) > 1.01 else # \begin{cases}
                (0 if ((f_mean_h1 / f_mean_h2) <= 1.01 and (f_mean_h1 / f_mean_h2) >= 0.99)
                    else 1)) # \end{cases}
 
# convention to allow import of this file as a module
if __name__ == '__main__':
    main()
