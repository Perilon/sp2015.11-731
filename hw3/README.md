What's goin' on here?   Using eschling's original commit as a base, my thing here (pig4) takes the Spanish input and splits it in twain at each index in the sentence pretty much, and gets the best translation for each half, and jams those English parts back together, and scores each result of that process, and keeps the best-scoring one, which often is not the same as the version that just does the sentence as a whole (it tries that one too).   That is, sometimes the English version that results from translating and then concatenating two fragments of the source language happens to be nicer than the best you can get from treating the sentence atomically.

The score for the eschling version alone is -5076.682905.   This takes it up to -4993.513309.

Does it take a lot longer?   Heck yeah it does!!!   Would it be faster to use syntactical information to try to split the Spanish sentences at boundaries that make some kind of intuitive sense?   Sure, but I don't think the "logical" splits would all necessarily yield the best results in this case.

=====================================================

Well, I tried implementing some simple code to switch the position of nouns and adjectives in the Spanish input using the NLTK interface to the Stanford POS tagger, then running the default decoder.   That actually provides slightly worse results than the default score overall (-5719).  The same thing is the case when I switch the position of nouns and adjectives in the English output from the regular Spanish input (-5748).   Oh well!

======================================================

There are three Python programs here (`-h` for usage):

 - `./decode` a simple non-reordering (monotone) phrase-based decoder
 - `./grade` computes the model score of your output

The commands are designed to work in a pipeline. For instance, this is a valid invocation:

    ./decode | ./grade


The `data/` directory contains the input set to be decoded and the models

 - `data/input` is the input text

 - `data/lm` is the ARPA-format 3-gram language model

 - `data/tm` is the phrase translation model

