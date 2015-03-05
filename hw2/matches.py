from collections import Counter
import nltk
from nltk.stem.porter import *
stemmer = PorterStemmer()
from nltk.corpus import wordnet as wn

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

    print "hypothesis = ", hypothesis, "\n"
    print "reference = ", reference, "\n"
    
    exact_match_function = (Counter(hypothesis) & Counter(reference)) & C_function
    exact_match_content = (Counter(hypothesis) & Counter(reference)) - exact_match_function

    print "exact_match_function = ", exact_match_function
    print "exact_match_content = ", exact_match_content
    
    exact_match_function_count = float(sum(exact_match_function.viewvalues()))
    exact_match_content_count = float(sum(exact_match_content.viewvalues()))

    print "exact_match_function_count = ", exact_match_function_count
    print "exact_match_content_count = ", exact_match_content_count

#   -------------------------------------------------------------------------------------------
    nonexact_function_hyp = (Counter(hypothesis) - (Counter(reference) & Counter(hypothesis))) & C_function
    nonexact_content_hyp = (Counter(hypothesis) - (Counter(reference) & Counter(hypothesis))) - nonexact_function_hyp
    print "nonexact_function_hyp = ", nonexact_function_hyp
    print "nonexact_content_hyp = ", nonexact_content_hyp

    nonexact_function_ref = (Counter(reference) - (Counter(reference) & Counter(hypothesis))) & C_function
    nonexact_content_ref = (Counter(reference) - (Counter(reference) & Counter(hypothesis))) - nonexact_function_ref
    print "nonexact_function_ref = ",  nonexact_function_ref
    print "nonexact_content_ref = ", nonexact_content_ref

    nonexact_f_stems_hyp, nonexact_c_stems_hyp, nonexact_f_stems_ref, nonexact_c_stems_ref, \
                          orig_word_f_hyp, orig_word_c_hyp, orig_word_f_ref, orig_word_c_ref = [], [], [], [], [], [], [], []

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

    for word in nonexact_function_hyp.keys():
        if stemmer.stem(word) in nonexact_match_function.keys():
            orig_word_f_hyp.append(word)
    for word in nonexact_content_hyp.keys():
        if stemmer.stem(word) in nonexact_match_content.keys():
            orig_word_c_hyp.append(word)
    for word in nonexact_function_ref.keys():
        if stemmer.stem(word) in nonexact_match_function.keys():
            orig_word_f_ref.append(word)
    for word in nonexact_content_ref.keys():
        if stemmer.stem(word) in nonexact_match_content.keys():
            orig_word_c_ref.append(word)

    print "orig_word_f_hyp = ", orig_word_f_hyp
    print "orig_word_c_hyp = ", orig_word_c_hyp
    print "orig_word_f_ref = ", orig_word_f_ref
    print "orig_word_c_ref = ", orig_word_c_ref

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

#   -------------------------------------------------------------------------------------------

##    Leftover_function_hyp = (Counter(hypothesis) - (Counter(reference) & Counter(hypothesis)) - nonexact_match_function) & C_function
##    Leftover_content_hyp = (Counter(hypothesis) - (Counter(reference) & Counter(hypothesis)) - nonexact_match_content) - nonexact_function_hyp

    Leftover_function_hyp = nonexact_function_hyp - nonexact_match_function - Counter(orig_word_f_hyp)
    Leftover_content_hyp = nonexact_content_hyp - nonexact_match_content - Counter(orig_word_c_hyp)

    print "Leftover_function_hyp =", Leftover_function_hyp
    print "Leftover_content_hyp =", Leftover_content_hyp

##    Leftover_function_ref = (Counter(reference) - (Counter(reference) & Counter(hypothesis)) - nonexact_match_function) & C_function
##    Leftover_content_ref = (Counter(reference) - (Counter(reference) & Counter(hypothesis)) - nonexact_match_content) - nonexact_function_ref

    Leftover_function_ref = nonexact_function_ref - nonexact_match_function - Counter(orig_word_f_ref)
    Leftover_content_ref = nonexact_content_ref - nonexact_match_content - Counter(orig_word_c_ref)

    print "Leftover_function_ref = ", Leftover_function_ref
    print "Leftover_content_ref = ", Leftover_content_ref

    def path_similarity(word1, word2):
            if wn.synsets(word1) != [] and wn.synsets(word2) != []:
                    path_similarity_dict = {}
                    synstrings1_list = []
                    for item in wn.synsets(word1):
                            synstrings1_list.append(str(item))
                    synstrings2_list = []
                    for item in wn.synsets(word2):
                            synstrings2_list.append(str(item))
                    synsets1_list = []
                    synsets2_list = []
                    for item1 in synstrings1_list:
                            synsets1_list.append( wn.synset(item1[item1.find("(")+2:item1.find(")")-1]) )
                    for item2 in synstrings2_list:
                            synsets2_list.append( wn.synset(item2[item2.find("(")+2:item2.find(")")-1]) )
                    for item1 in synsets1_list:
                            for item2 in synsets2_list:
                                    path_similarity_dict[(item1, item2)] = item1.path_similarity(item2)
                    best_match = max(path_similarity_dict.values())
                    best_matches = []
                    for item in path_similarity_dict.items():
                            if item[1] == best_match:
                                    best_matches.append(item)
                    return best_match

    def find_synonyms(Leftover_content_hyp, Leftover_content_ref):
        best_synonyms_dict = {}
        word1_scores = {}
        for word1 in Leftover_content_hyp:
            word1_scores[word1] = 0
            for word2 in Leftover_content_ref:
                sim = path_similarity(word1, word2)
                if sim > word1_scores[word1]:
                    word1_scores[word1] = sim
                    best_match_of_word1 = word2
            best_synonyms_dict[(word1, best_match_of_word1)] = word1_scores[word1]
        return best_synonyms_dict

    content_synonyms_hyp = []
    content_synonyms_ref = []

    print "find_synonyms.items() = ", find_synonyms(Leftover_content_hyp, Leftover_content_ref).items()

    for possibility in find_synonyms(Leftover_content_hyp, Leftover_content_ref).items():
        if possibility[1] >= .4:
            print "possibility = ", possibility[1]
            content_synonyms_hyp.append(possibility[0][0])
            content_synonyms_ref.append(possibility[0][1])

    content_synonyms_hyp = Counter(content_synonyms_hyp)
    content_synonyms_ref = Counter(content_synonyms_ref)

    print "content_synonyms_hyp = ", Counter(content_synonyms_hyp)
    print "content_synonyms_ref = ", Counter(content_synonyms_ref)
            
    content_synonyms_hyp_count = float(sum(content_synonyms_hyp.viewvalues()))
    content_synonyms_ref_count = float(sum(content_synonyms_ref.viewvalues()))

    print "content_synonyms_hyp_count = ", content_synonyms_hyp_count
    print "content_synonyms_ref_count = ", content_synonyms_ref_count

    def Precision3(delta, w_exact, w_stems, exact_match_content_count, exact_match_function_count, hypothesis):
        if len(hypothesis) == 0: return 0.0
        else:
            return ((w_exact * ((delta * exact_match_content_count) + ((1 - delta) * exact_match_function_count))) \
                   + (w_stems * ((delta * nonexact_match_content_count) + ((1 - delta) * nonexact_match_function_count)))) / len(hypothesis)
