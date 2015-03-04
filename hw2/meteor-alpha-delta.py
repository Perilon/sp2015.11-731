#!/usr/bin/env python
import argparse # optparse is deprecated
from itertools import islice # slicing for iterators
from collections import Counter
import nltk

function_words = ["you", "i", "to", "the", "a", "and", "that", "it", "of", "me", "what", "is", "in", "this", "know", "i'm", "for", "no", "have", "my", "don't", "just", "not", "do", "be", "on", "your", "was", "we", "it's", "with", "so", "but", "all", "well", "are", "he", "oh", "about", "right"]

#function_words = ['a', 'about', 'above', 'after', 'again', 'against', 'all', 'am', 'an', 'and', 'any', 'are', "aren't", 'as', 'at', 'be', 'because', 'been', 'before', 'being', 'below', 'between', 'both', 'but', 'by', "can't", 'cannot', 'could', "couldn't", 'did', "didn't", 'do', 'does', "doesn't", 'doing', "don't", 'down', 'during', 'each', 'few', 'for', 'from', 'further', 'had', "hadn't", 'has', "hasn't", 'have', "haven't", 'having', 'he', "he'd", "he'll", "he's", 'her', 'here', "here's", 'hers', 'herself', 'him', 'himself', 'his', 'how', "how's", 'i', "i'd", "i'll", "i'm", "i've", 'if', 'in', 'into', 'is', "isn't", 'it', "it's", 'its', 'itself', "let's", 'me', 'more', 'most', "mustn't", 'my', 'myself', 'no', 'nor', 'not', 'of', 'off', 'on', 'once', 'only', 'or', 'other', 'ought', 'our', 'ours\tourselves', 'out', 'over', 'own', 'same', "shan't", 'she', "she'd", "she'll", "she's", 'should', "shouldn't", 'so', 'some', 'such', 'than', 'that', "that's", 'the', 'their', 'theirs', 'them', 'themselves', 'then', 'there', "there's", 'these', 'they', "they'd", "they'll", "they're", "they've", 'this', 'those', 'through', 'to', 'too', 'under', 'until', 'up', 'very', 'was', "wasn't", 'we', "we'd", "we'll", "we're", "we've", 'were', "weren't", 'what', "what's", 'when', "when's", 'where', "where's", 'which', 'while', 'who', "who's", 'whom', 'why', "why's", 'with', "won't", 'would', "wouldn't", 'you', "you'd", "you'll", "you're", "you've", 'your', 'yours', 'yourself', 'yourselves']

#function_words = ['the', 'of', 'and', 'to', 'a', 'in', 'that', 'is', 'was', 'he', 'for', 'it', 'with', 'as', 'his', 'on', 'be', 'at', 'by', 'i', 'this', 'had', 'not', 'are', 'but', 'from', 'or', 'have', 'an', 'they']

C_function = Counter(function_words)
for item in C_function.keys():
    C_function[item] = 20

def harmonic_mean(P, R, alpha):
    denominator = (alpha * P + (1 - alpha) * R)
    if denominator == 0: return 0.0
    return P * R / denominator

def simple_meteor(hypothesis, reference, alpha, delta):

    m_function = float(sum((Counter(hypothesis) & Counter(reference) & C_function).viewvalues()))
    m_content = float(sum((Counter(hypothesis) & Counter(reference)).viewvalues())) - m_function


    #print "counter(h) = ", Counter(h)
    #print "counter(ref) = ", Counter(ref)
    #print "(Counter(h) & Counter(ref)) = ", (Counter(h) & Counter(ref))
    #print "(Counter(h) & Counter(ref)).viewvalues() = ", (Counter(h) & Counter(ref)).viewvalues()


    def Precision(delta, m_content, m_function, hypothesis):
        if len(hypothesis) == 0: return 0.0
        else:
	    return ((delta * m_content) + ((1 - delta) * m_function)) / len(hypothesis)


    def Recall(delta, m_content, m_function, reference):
        if len(reference) == 0: return 0.0
        else:
            return ((delta * m_content) + ((1 - delta) * m_function)) / len(reference)

    P = Precision(delta, m_content, m_function, hypothesis)
    R = Recall(delta, m_content, m_function, reference)

    return harmonic_mean(P, R, alpha)
 
def main():
    parser = argparse.ArgumentParser(description='Evaluate translation hypotheses.')
    # PEP8: use ' and not " for strings
    parser.add_argument('-i', '--input', default='data/train-test.hyp1-hyp2-ref',
        help='input file (default data/train-test.hyp1-hyp2-ref)')
    parser.add_argument('-n', '--num_sentences', default=None, type=int,
        help='Number of hypothesis pairs to evaluate')
    parser.add_argument('-a', '--alpha', default=0.5, type=float, help='precision/recall weight parameter')
    parser.add_argument('-d', '--delta', default=0.5, type=float, help='content/function word weight parameter')
    # note that if x == [1, 2, 3], then x[:None] == x[:] == x (copy); no need for sys.maxint
    opts = parser.parse_args()
 
    # we create a generator and avoid loading all sentences into a list
    def sentences():
        with open(opts.input) as f:
            for pair in f:
                yield [sentence.strip().split() for sentence in pair.lower().translate(None, """.,'"?:;/\*!-""").split(' ||| ')]
 
    # note: the -n option does not work in the original code
    for h1, h2, reference in islice(sentences(), opts.num_sentences):
        h1_val = simple_meteor(h1, reference, opts.alpha, opts.delta)
        h2_val = simple_meteor(h2, reference, opts.alpha, opts.delta)

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
 
#convention to allow import of this file as a module
if __name__ == '__main__':
    main()

