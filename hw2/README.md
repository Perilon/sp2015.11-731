---So, "meteor-alpha-delta-w1-w2-w3.py" is my version that has output the best results, with parameters alpha = .8, delta = .65, w_exact = 1, w_stems = .6, and w_synonyms = .8 (I think that's what it was?).  I have also worked on a version that eschews the content/function word dichotomy and seeks to sort and weight words by a more fine-grained POS distinction.

"Meteor-new-approach.py" has a noun-verb-other distinction with delta parameters for each (that should be made sure to sum to 1), and supports matching by exact match and by stems.

"Meteor-new-approach-nvao.py" has a noun-verb-adjective/adverb-other distinction, with delta parameters for each and matches by exact match and by stems.

An informal survey of results indicates that relatively few words are left over from the exact matches for the stemmed matches possibility to kick in, but it does occasionally.

I'm still playing around with tuning the parameters to get the best results for this line of approach.  The way the defaults are set right now gets 0.517437.

--------------------------------------------------------------

---Did some obnoxious stuff with WordNet synsets for a modicum of improvement.  Have a matcher weight for that category too now.  I think this isn't the most fruitful approach to finding words that share similar meanings, and it takes a long time to run.

---Implemented matcher weights for exact matches and stemmed matches

---Eliminating various punctuation

---Used cnakos' code as a base, added a delta parameter option and some function words.  Defined what outputs 0 a little more broadly.

There are three Python programs here (`-h` for usage):

 - `./evaluate` evaluates pairs of MT output hypotheses relative to a reference translation using counts of matched words
 - `./check` checks that the output file is correctly formatted
 - `./grade` computes the accuracy

The commands are designed to work in a pipeline. For instance, this is a valid invocation:

    ./evaluate | ./check | ./grade


The `data/` directory contains the following two files:

 - `data/train-test.hyp1-hyp2-ref` is a file containing tuples of two translation hypotheses and a human (gold standard) translation. The first 26208 tuples are training data. The remaining 24131 tuples are test data.

 - `data/train.gold` contains gold standard human judgements indicating whether the first hypothesis (hyp1) or the second hypothesis (hyp2) is better or equally good/bad for training data.

Until the deadline the scores shown on the leaderboard will be accuracy on the training set. After the deadline, scores on the blind test set will be revealed and used for final grading of the assignment.
