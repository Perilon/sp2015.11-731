from collections import Counter
import nltk
from nltk.stem.porter import *
stemmer = PorterStemmer()

alpha = .80
delta = .65
w_exact = 1
w_stems = .6

function_words = ["you", "i", "to", "the", "a", "and", "that", "it", "of", "me", "what", "is", "in", "this", "know", "i'm", "for", "no", "have", "my", "don't", "just", "not", "do", "be", "on", "your", "was", "we", "it's", "with", "so", "but", "all", "well", "are", "he", "oh", "about", "right"]

C_function = Counter(function_words)
for item in C_function.keys():
    C_function[item] = 20

def harmonic_mean(P, R, alpha):
    denominator = (alpha * P + (1 - alpha) * R)
    if denominator == 0: return 0.0
    return P * R / denominator

def matches(sentence):

    pig = [sent.strip().split() for sent in sentence.lower().translate(None, """.,'"?:;/\*!-""").split(" ||| ")]
    hypothesis = pig[0]
    reference = pig[2]

    print "hypothesis = ", hypothesis
    print "reference = ", reference
    
    exact_match_function = (Counter(hypothesis) & Counter(reference)) & C_function
    exact_match_content = (Counter(hypothesis) & Counter(reference)) - exact_match_function

    print "exact_match_function = ", exact_match_function
    print "exact_match_content = ", exact_match_content
    
    exact_match_function_count = float(sum(exact_match_function.viewvalues()))
    exact_match_content_count = float(sum(exact_match_content.viewvalues()))

    print "exact_match_function_count = ", exact_match_function_count
    print "exact_match_content_count = ", exact_match_content_count

    nonexact_function_hyp = (Counter(hypothesis) - (Counter(reference) & Counter(hypothesis))) & C_function
    nonexact_content_hyp = (Counter(hypothesis) - (Counter(reference) & Counter(hypothesis))) - nonexact_function_hyp
    print "nonexact_function_hyp = ", nonexact_function_hyp
    print "nonexact_content_hyp = ", nonexact_content_hyp

    nonexact_function_ref = (Counter(reference) - (Counter(reference) & Counter(hypothesis))) & C_function
    nonexact_content_ref = (Counter(reference) - (Counter(reference) & Counter(hypothesis))) - nonexact_function_ref
    print "nonexact_function_ref = ",  nonexact_function_ref
    print "nonexact_content_ref = ", nonexact_content_ref

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
    print "nonexact_f_stems_hyp = ", nonexact_f_stems_hyp
    print "nonexact_c_stems_hyp = ", nonexact_c_stems_hyp
    print "nonexact_f_stems_ref = ", nonexact_f_stems_ref
    print "nonexact_c_stems_ref = ", nonexact_c_stems_ref

    nonexact_match_function = Counter(nonexact_f_stems_hyp) & Counter(nonexact_f_stems_ref)
    nonexact_match_content = Counter(nonexact_c_stems_hyp) & Counter(nonexact_c_stems_ref)
    print "nonexact_match_function = ", nonexact_match_function
    print "nonexact_match_content = ", nonexact_match_content

    nonexact_match_function_count = float(sum(nonexact_match_function.viewvalues()))
    nonexact_match_content_count = float(sum(nonexact_match_content.viewvalues()))

    print "nonexact_match_function_count = ", nonexact_match_function_count
    print "nonexact_match_content_count = ", nonexact_match_content_count

    def Precision(delta, exact_match_content_count, exact_match_function_count, hypothesis):
        if len(hypothesis) == 0: return 0.0
        else:
            return ((delta * exact_match_content_count) + ((1 - delta) * exact_match_function_count)) / len(hypothesis)

    def Recall(delta, exact_match_content_count, exact_match_function_count, reference):
        if len(reference) == 0: return 0.0
        else:
            return ((delta * exact_match_content_count) + ((1 - delta) * exact_match_function_count)) / len(reference)

    P = Precision(delta, exact_match_content_count, exact_match_function_count, hypothesis)
    R = Recall(delta, exact_match_content_count, exact_match_function_count, reference)

    print "Precision = ", P
    print "Recall = ", R

    print "Harmonic mean = ", harmonic_mean(P, R, alpha)

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
    
    print "Precision2 = ", P2
    print "Recall2 = ", R2

    print "Harmonic mean 2 = ", harmonic_mean(P2, R2, alpha)
    
