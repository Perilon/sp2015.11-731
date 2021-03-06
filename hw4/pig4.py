#!/usr/bin/env python
from __future__ import division
import sys
import argparse
from collections import defaultdict
from utils import read_ttable
import scipy
from scipy.sparse import csr_matrix
from scipy.sparse import csc_matrix
import numpy as np
import random
import unicodedata

def remove_accents(input_str):
    nkfd_form = unicodedata.normalize('NFKD', input_str)
    return u"".join([c for c in nkfd_form if not unicodedata.combining(c)])

def dot(w, v):
	s = 0.0
	for k in set(w.keys()) & set(v.keys()):
		s += w[k] * v[k]
	return s

def removekey(d, key):
    r = dict(d)
    del r[key]
    return r

def Loss(x, y, w, gamma):
	return max(0, (gamma - (np.dot((y - x), w))))

parser = argparse.ArgumentParser()
parser.add_argument('--input', '-i', default='data/sample20.input')
parser.add_argument('--ttable', '-t', default='data/ttable')
parser.add_argument('--refs', '-r', default='data/sample20.refs')
args = parser.parse_args()

fo = open(args.refs)
refs = fo.readlines()
fo2 = open(args.input)
read_input = fo2.readlines()

#--------------------------------------------------------------------------
prev_ft_strings = []
Next_ft_strings = []
incomplete_prev_ft_strings = []
incomplete_Next_ft_strings = []
input_line_index = -1
for line in read_input:
	input_line_index += 1
	left_context, phrase, right_context = [part.strip() for part in line.decode('utf-8').strip().split('|||')]
	left_context = left_context.strip().split()
	right_context = right_context.strip().split()

	phrase = phrase[:4]

	#print "line = ", line.strip()
	if len(left_context) > 0:
		prev = left_context[-1]
		prev = prev[:4]
	else:
		prev = "<s>"
	if len(right_context) > 0:
		Next = right_context[0]
		Next = Next[:4]
	else:
		Next = "</s>"

	correct_czech = refs[input_line_index].decode("UTF-8").strip()

	correct_czech = remove_accents(correct_czech[:4])

	prev_ft_str = "src:" + phrase + "_tgt:" + correct_czech + "_prev:" + prev
	Next_ft_str = "src:" + phrase + "_tgt:" + correct_czech + "_next:" + Next
	incomplete_prev_ft_str = "src:" + phrase + "_tgt:" + correct_czech
	incomplete_Next_ft_str = "src:" + phrase + "_tgt:" + correct_czech

	prev_ft_strings.append(prev_ft_str)
	Next_ft_strings.append(Next_ft_str)
	incomplete_prev_ft_strings.append(incomplete_prev_ft_str)
	incomplete_Next_ft_strings.append(incomplete_Next_ft_str)

prev_ft_strings = sorted(set(prev_ft_strings))
Next_ft_strings = sorted(set(Next_ft_strings))
incomplete_prev_ft_strings = sorted(set(incomplete_prev_ft_strings))
incomplete_Next_ft_strings = sorted(set(incomplete_Next_ft_strings))

prev_ft_strings_dict = {}
Next_ft_strings_dict = {}
incomplete_prev_ft_strings_dict = {}
incomplete_Next_ft_strings_dict = {}

for i, item in enumerate(prev_ft_strings):
	prev_ft_strings_dict[item] = i
for i, item in enumerate(Next_ft_strings):
	Next_ft_strings_dict[item] = i
for i, item in enumerate(incomplete_prev_ft_strings):
	incomplete_prev_ft_strings_dict[item] = i
for i, item in enumerate(incomplete_Next_ft_strings):
	incomplete_Next_ft_strings_dict[item] = i

len_prev = len(prev_ft_strings)
len_Next = len(Next_ft_strings)
len_all = len_prev + len_Next	
	#print len_prev, len_Next, len_all
#---------------------------------------------------------------------------

translation_table = read_ttable(args.ttable)

#rand_init_weights = np.random.random(4) * 0.1
weights = {'log_prob_tgs': 0.1, "log_prob_sgt": 0.1, "log_lex_prob_tgs": 0.1, "log_lex_prob_sgt": 0.1}
#weights = {'log_prob_tgs': rand_init_weights[0], "log_prob_sgt": rand_init_weights[1], "log_lex_prob_tgs": rand_init_weights[2], "log_lex_prob_sgt": rand_init_weights[3]}

w1, w2, w3, w4 = weights["log_prob_tgs"], weights["log_prob_sgt"], weights["log_lex_prob_tgs"], weights["log_lex_prob_sgt"]

w_first_part = np.array([w1, w2, w3, w4])
zeros_prev = np.zeros(len_prev)
zeros_Next = np.zeros(len_Next)
w = np.append(np.append(w_first_part, zeros_prev), zeros_Next)

alpha = .0001
gamma = .1
iterations = 6

w_table = np.zeros([iterations, 4])
total_loss_table = np.zeros([iterations, 1])


iter_num = -1
for iters in range(iterations):
	iter_num += 1
	sys.stderr.write("Iteration %d \n" % (iter_num + 1))
	input_line_index = -1
	total_corpus_loss = 0
	#total_gradient = 0
	for line in open(args.input):
		#print "w = ", w
		input_line_index += 1
		#print "input_line_index = ", input_line_index
		sys.stderr.write('Line # %d\r' % input_line_index)
		#print "refs[input_line_index].decode('UTF-8').strip() = ", refs[input_line_index].decode("UTF-8").strip()
		correct_czech = refs[input_line_index].decode("UTF-8").strip()

		#print "correct_czech =", correct_czech

		left_context, phrase, right_context = [part.strip() for part in line.decode('utf-8').strip().split('|||')]

		left_context = left_context.strip().split()
		right_context = right_context.strip().split()

		if len(left_context) > 0:
			prev = left_context[-1]
			prev = prev[:4]
		else:
			prev = "<s>"
		if len(right_context) > 0:
			Next = right_context[0]
			Next = Next[:4]
		else:
			Next = "</s>"

		#prev_ft_str = "src:" + phrase + "_tgt:" + correct_czech + "_prev:" + prev   ###?
		#Next_ft_str = "src:" + phrase + "_tgt:" + correct_czech + "_next:" + Next   ###?

		correct_weights = translation_table[phrase][correct_czech]
		#print "correct_weights = ", correct_weights
		c1, c2, c3, c4 = correct_weights["log_prob_tgs"], correct_weights["log_prob_sgt"], \
	                       correct_weights["log_lex_prob_tgs"], correct_weights["log_lex_prob_sgt"]
		
		phrase_stemmed = phrase[:4]
		correct_czech_stemmed = remove_accents(correct_czech[:4])
		
		zeros_prev = np.zeros(len_prev)
		zeros_Next = np.zeros(len_Next)

		prev_ft_str = "src:" + phrase_stemmed + "_tgt:" + correct_czech_stemmed + "_prev:" + prev
		Next_ft_str = "src:" + phrase_stemmed + "_tgt:" + correct_czech_stemmed + "_next:" + Next

		#if prev_ft_str in prev_ft_strings:
			#print "prev_ft_str =", prev_ft_str
			#zeros_prev[prev_ft_strings.index(prev_ft_str)] = 1
			
		if prev_ft_strings_dict.get(prev_ft_str, 0) != 0:
			zeros_prev[prev_ft_strings_dict[prev_ft_str]] = 1
			#print "good1"

		#else:
			#print "nope"
		#if Next_ft_str in Next_ft_strings:
			#zeros_Next[Next_ft_strings.index(Next_ft_str)] = 1
			#zeros_Next[Next_ft_strings_dict[Next_ft_str]] = 1

		if Next_ft_strings_dict.get(Next_ft_str, 0) != 0:
			zeros_Next[Next_ft_strings_dict[Next_ft_str]] = 1
			#print "good2"

		y_first_part = np.array([c1, c2, c3, c4])
		y = np.append(np.append(y_first_part, zeros_prev), zeros_Next)
		#print "y = ", y

		incorrect_translations = removekey(translation_table[phrase], correct_czech)
		#print "incorrect_translations = ", incorrect_translations
		m = len(incorrect_translations)

		x = np.zeros([m, (4+len_all)])

		for n, incorrect_czech_word in enumerate(incorrect_translations.keys()):

			zeros_prev = np.zeros(len_prev)
			zeros_Next = np.zeros(len_Next)
			wrong_prev_ft_str = "src:" + phrase + "_tgt:" + incorrect_czech_word + "_prev:" + prev
			wrong_Next_ft_str = "src:" + phrase + "_tgt:" + incorrect_czech_word + "_next:" + Next
			
			#if wrong_prev_ft_str in prev_ft_strings:
				#zeros_prev[prev_ft_strings.index(wrong_prev_ft_str)] = 1

			if prev_ft_strings_dict.get(wrong_prev_ft_str, 0) != 0:
				zeros_prev[prev_ft_strings_dict[wrong_prev_ft_str]] = 1

			#if wrong_Next_ft_str in Next_ft_strings:
				#zeros_Next[Next_ft_strings.index(wrong_Next_ft_str)] = 1

			if Next_ft_strings_dict.get(wrong_Next_ft_str, 0) != 0:
				zeros_Next[Next_ft_strings_dict[wrong_Next_ft_str]] = 1

			in1, in2, in3, in4 = incorrect_translations[incorrect_czech_word]["log_prob_tgs"], incorrect_translations[incorrect_czech_word]["log_prob_sgt"], \
	incorrect_translations[incorrect_czech_word]["log_lex_prob_tgs"], incorrect_translations[incorrect_czech_word]["log_lex_prob_sgt"]

			temp_array = np.array([in1, in2, in3, in4])

			x[n] = np.append(np.append(temp_array, zeros_prev), zeros_Next)

		#print "x = ", x
		loss_on_sentence = sum([max(0, (gamma - (np.dot((y - x[i]), w)))) for i in range(m)])
		#print "loss_on_sentence = ", loss_on_sentence
		total_corpus_loss += loss_on_sentence
		#print "total_corpus_loss = ", total_corpus_loss

		if loss_on_sentence > 0:
			
			k = sum([Loss(x[i], y, w, gamma) != 0 for i in range(x.shape[0])])
			#print "k = ", k

			new_gradient = sum([(x[i] - y) for i in range(x.shape[0]) if Loss(x[i], y, w, gamma) != 0]) # * (1.0/k)

	       		#gradient = sum([(x[i] - y) for i in range(m)]) # * (1.0/m)
			#total_gradient += gradient
			#print "gradient = ", gradient
			#print "new_gradient = ", new_gradient
			#print "alpha * new_gradient = ", (alpha * new_gradient), "\n"
			#print "total_gradient = ", total_gradient, "\n"
			w = np.subtract(w, (alpha * new_gradient))
			#print "new w = ", w, "\n"
		#else:
			#print "No loss here!\n"

	#w = w - (alpha * total_gradient)
	#print "total_gradient = ", total_gradient

	total_loss_table[iter_num] = total_corpus_loss
	w_table[iter_num] = w[:4]

	#print "total corpus loss = ", total_corpus_loss, "\n---------------------------------\n"
	#print "new w = ", w, "\n-----------------------------\n"
	#print "len(w) =", len(w)

	#sys.stderr.write("w = %s \n" % str(w))
	#sys.stderr.write("total loss = %s \n" % str(total_corpus_loss))

sys.stderr.write("%s\n" % str(total_loss_table))
sys.stderr.write("%s\n" % str(w_table))

#final_weights = {'log_prob_tgs': w[0], "log_prob_sgt": w[1], "log_lex_prob_tgs": w[2], "log_lex_prob_sgt": w[3]}
final_weights = w
final_weights = scipy.sparse.csr_matrix(final_weights)
final_weights = final_weights.T

def update_ttable(filename):
	translation_table = defaultdict(lambda: defaultdict(lambda: defaultdict(float)))
	print >>sys.stderr, 'Reading ttable from %s...' % filename
	with open(filename) as f:
		for i, line in enumerate(f):
			source, target, features = [part.strip() for part in line.decode('utf-8').strip().split('|||')]
			first_features = np.array([float(v) for v in features.split()])
		
			zeros_prev = np.zeros(len_prev)
			zeros_Next = np.zeros(len_Next)

			candidate = "src:" + source[:4] + "_tgt:" + target[:4]

			#if candidate in incomplete_prev_ft_strings:
			#	zeros_prev[incomplete_prev_ft_strings.index(candidate)] = 1

			if incomplete_prev_ft_strings_dict.get(candidate, 0) != 0:
				zeros_prev[incomplete_prev_ft_strings_dict[candidate]] = 1		

			#if candidate in incomplete_Next_ft_strings:
			#	zeros_Next[incomplete_Next_ft_strings.index(candidate)] = 1

			if incomplete_Next_ft_strings_dict.get(candidate, 0) != 0:
				zeros_Next[incomplete_Next_ft_strings_dict[candidate]] = 1

			features = np.append(np.append(first_features, zeros_prev), zeros_Next)
			features = scipy.sparse.csr_matrix(features)
			#print len(features)		
			
			#assert len(features) == 4
			#features = { 'log_prob_tgs': features[0], \
			#	     'log_prob_sgt': features[1], \
			#	     'log_lex_prob_tgs': features[2], \
			#	     'log_lex_prob_sgt': features[3] }
			translation_table[source][target] = features
			sys.stderr.write('%d\r' % i)
	print >>sys.stderr
	return translation_table

updated_translation_table = update_ttable(args.ttable)
#print updated_translation_table.items()[:10]


with open("data/dev+test.input") as f:
	for i, line in enumerate(f):
		sys.stderr.write("Calculating line %d \r" % i)
		left_context, phrase, right_context = [part.strip() for part in line.decode('utf-8').strip().split('|||')]
		candidates = [target for target, features in sorted(updated_translation_table[phrase].iteritems(), key=lambda (t, f): f.dot(final_weights)[(0,0)], reverse=True)]
		print ' ||| '.join(candidates).encode('utf-8')
