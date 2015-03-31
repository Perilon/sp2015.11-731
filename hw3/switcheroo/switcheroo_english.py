import nltk
from nltk.tokenize import word_tokenize
from nltk.tag.stanford import POSTagger

st = POSTagger("/home/andrew/Desktop/stanford-postagger-2014-08-27/models/english-bidirectional-distsim.tagger", "/home/andrew/Desktop/stanford-postagger-2014-08-27/stanford-postagger-3.4.1.jar", "UTF-8")

nouns = [u"NN", u"NNS", u"NNP", u"NNPS", u"PRP", u"PRP$"]
adjectives = [u"JJ", u"JJR", u"JJS"]

f = open("/home/andrew/sp2015.11-731/hw3/output.txt")

g = f.readlines()

for sentence in g:
	final_form = []
	tokenized_sentence = word_tokenize(sentence)
	tag_sent = st.tag(tokenized_sentence)

	for x in range(len(tag_sent)-1):
		if tag_sent[x][1] in nouns and tag_sent[x+1][1] in adjectives:
			print True
			temp1 = tag_sent[x]
			temp2 = tag_sent[x+1]
			tag_sent[x] = temp2
			tag_sent[x+1] = temp1
	#print tag_sent
	for (word, POS) in tag_sent:
		final_form.append(word)
	final_form = " ".join(final_form)
	print final_form
