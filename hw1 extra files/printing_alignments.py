for pair in bitext:
	whole_sentence_alignment = []
	for english_word in pair[1]:
		#print english_word
		possibilities = []
		#print possibilities
		for item in translation_probability.items():
			if item[0][0] == english_word:
				if item[0][1] in pair[0]:
					possibilities.append(item[1])
				#print "possibilities = ", possibilities
		best_match = max(possibilities)
		#print "best_match = ", best_match
		for item in translation_probability.items():
			if item[1] == best_match:
				german_match = item[0][1]
				#print "german_match = ", german_match

		for german_word in pair[0]:
			if german_word == german_match:
				alignment_german = pair[0].index(german_word)
				#print "german_word = ", german_word

		word_alignment = str(alignment_german) + "-" + str(pair[1].index(english_word))
		whole_sentence_alignment.append(word_alignment)
	print "initial alignment = ", whole_sentence_alignment, "\n"


	for n in range(len(whole_sentence_alignment)):
		whole_sentence_alignment[n] = whole_sentence_alignment[n].split("-")

	whole_sentence_alignment.sort()
	print "new alignment = ", whole_sentence_alignment, "\n"
	final_output = []
	for item in whole_sentence_alignment:
		new = item[0] + "-" + item[1]
		final_output.append(new)
	final_output = " ".join(final_output)
	print "final_output = ", final_output, "\n"
