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

