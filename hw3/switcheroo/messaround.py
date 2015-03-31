Python 2.7.6 (default, Mar 22 2014, 22:59:56) 
[GCC 4.8.2] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> import nltk
>>> f = open("/home/andrew/sp2015.11-731/hw3/output.txt")
>>> g = f.readlines()
>>> len(g)
55
>>> g[0]
'the army turkish has no interest in take risks implied participation in the fighting sectarian in iraq . \n'
>>> g[55]

Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    g[55]
IndexError: list index out of range
>>> g[54]
'the way in which has been conducted the electoral process in zimbabwe from march has been a continuation not constitutional of a government . \n'
>>> for sentence in g:
	g = g.strip()

	

Traceback (most recent call last):
  File "<pyshell#9>", line 2, in <module>
    g = g.strip()
AttributeError: 'list' object has no attribute 'strip'
>>> for sentence in g:
	sentence = sentence.strip()

	
>>> g[0]
'the army turkish has no interest in take risks implied participation in the fighting sectarian in iraq . \n'
>>> g = [sentence.strip() for sentence in f.readlines()]
>>> g[0]

Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    g[0]
IndexError: list index out of range
>>> g
[]
>>> for sentence in f.readlines():
	print sentence.strip()

	
>>> len(f.readlines())
0
>>> g = f.readlines()
>>> len(g)
0
>>> f = open("/home/andrew/sp2015.11-731/hw3/output.txt")
>>> for sentence in f.readlines():
	print sentence.strip()

	
the army turkish has no interest in take risks implied participation in the fighting sectarian in iraq .
erdogan has no intention of left drawn to this trap .
the small cost tax to non vote makes it rational for everyone vote and simultaneously establishes a standard social voting .
the australian want to be forced to vote .
moreover , an atmosphere business inflexible and light to the family is no longer the only option for women who work .
over the last year and a half , they to 1.8 $ 1 trillion , with far the highest in the world .
but the paradox is that reserves of today are not riches real that can be used to stimulate the economy local .
it will most likely that the us experience a much of a slowdown , as occurred in the recession light of the last two years .
but not seen to be adopters taxes carbon .
what does know that we chinese authorities never faced a challenge of this magnitude with a potential such for to gain or lose prestige .
all of this raises the question of whether china will by replace the us as power hegemonic global that defines and applied rules of the global economy .
this is unsustainable , and eventually precipitate a confrontation with proportions with the united states and europe ) .
the more centralized is political power , more could hinder the central the development of markets .
instead , political integration could have a effect opposed in the development of markets .
but now seems to america has into trouble again and again wants weaken the pact .
and china , for their part , will develop their financial markets and their ability to generate financial assets high - quality internally .
clearly , is preferable the second option .
the asian financial crisis and devaluation brazilian in early 1999 did that the burden argentine was decidedly overvalued .
there up a deficit current - account and a - debt that they were literally of proportions greek .
all of this has been possible because it has been seen as , viewed the parameters historical , as a period exceptional of political stability .
so far , or in cameroon or in chad , governments have been loath to publish no record of income relative to the project 's pipeline .
for starters , now america possesses a true friend and ally in the élysée palace .
this period of time would both to turkey as in the union a chance to reconciled .
what it gives rise to emotions stronger is the population muslim turkey 's .
it is also fears that one day islamists turn to turkey into a state fundamentalist .
the european central bank , established in 1998 , has the mandate of managing the new currency to maintain the price stability .
between 2000 and 2005 , the dollar has lost more 25 % of its value to the euro .
to an serious downturn , a country can wish to engage keynesian political traditional through fiscal stimulus in large - scale and financed by deficit .
moreover , the current economic crisis has made it back to talk about the need for the european union has competition in tax .
countries with large income could it as a reason enough to want out .
he has never been easy to reach agreements economic international .
for citizens young , islamists , in particular , outlets normal for political involvement have closed .
first , how much capacity conventional for the war must retain the us ?
this strategy has endured on a base bipartisan in america , and opinion polls show that still has an wide acceptance in japan .
nevertheless , the alliance faces three serious challenges in a new context externally .
what can prevent the situation deteriorates more and will probably in a systemic crisis ?
but where , precisely , is the core of the new economy ?
it is not of surprising that more than half of companies more respected are american .
why was meant to the world war ii confidence any in the future ?
might it removing subsidies that point to end wrong to release funds for programs more specific and effective of fighting poverty and job creation .
according to the global agenda of food , the 70 % of the population lacks food security .
in theory , in such areas could be eliminated half , roughly the gap educational building schools for girls .
it is estimated that the benefits are being six times higher than the costs .
indeed , many observers believe that women will determine the outcome electoral .
women who competing in the labor market usually support efforts at challenging the double moral sexual and doom strongly the harassment sexual .
after all , some women have had long time force and the will of reaching the top .
as wants to be , unions are a key factor for the evolution of our economic system in 2008 , and in the coming years .
there is no doubt that the world has seen progress in some fronts in recent decades .
however , in general the gaps of inequality are great and in many cases are growing further .
unfortunately , most likely summit on whether an opportunity lost .
global warming at all is our main environmental threat .
and economic models show that france has lost much or more jobs from the costs additional of the subsidies .
this situation has lasted for two decades .
so , uribe could not defended by the new deal military .
the way in which has been conducted the electoral process in zimbabwe from march has been a continuation not constitutional of a government .
>>> for sentence in f.readlines():
	print sentence.strip()

	
>>> f = open("/home/andrew/sp2015.11-731/hw3/output.txt")
>>> g = f.readlines()
>>> h = g[0]
>>> h
'the army turkish has no interest in take risks implied participation in the fighting sectarian in iraq . \n'
>>> h = h.strip()
>>> h
'the army turkish has no interest in take risks implied participation in the fighting sectarian in iraq .'
>>> nltk.pos_tag(h)
[('t', 'NN'), ('h', 'NN'), ('e', 'NN'), (' ', ':'), ('a', 'DT'), ('r', 'NN'), ('m', 'NN'), ('y', 'NN'), (' ', ':'), ('t', 'NN'), ('u', 'NN'), ('r', 'NN'), ('k', 'NN'), ('i', 'PRP'), ('s', 'VBZ'), ('h', 'JJ'), (' ', 'NN'), ('h', 'NN'), ('a', 'DT'), ('s', 'NN'), (' ', ':'), ('n', 'NN'), ('o', 'NN'), (' ', ':'), ('i', 'PRP'), ('n', 'VBP'), ('t', 'JJ'), ('e', 'NN'), ('r', 'NN'), ('e', 'NN'), ('s', 'NNS'), ('t', 'VBP'), (' ', ':'), ('i', 'PRP'), ('n', 'VBP'), (' ', ':'), ('t', 'NN'), ('a', 'DT'), ('k', 'NN'), ('e', 'NN'), (' ', ':'), ('r', 'NN'), ('i', 'PRP'), ('s', 'VBZ'), ('k', 'NN'), ('s', 'NNS'), (' ', ':'), ('i', 'PRP'), ('m', 'VBP'), ('p', 'NN'), ('l', 'NN'), ('i', 'PRP'), ('e', 'VBP'), ('d', 'JJ'), (' ', 'NN'), ('p', 'NN'), ('a', 'DT'), ('r', 'NN'), ('t', 'NN'), ('i', 'PRP'), ('c', 'VBP'), ('i', 'PRP'), ('p', 'VBP'), ('a', 'DT'), ('t', 'NN'), ('i', 'PRP'), ('o', 'VBP'), ('n', 'JJ'), (' ', 'NN'), ('i', 'PRP'), ('n', 'VBP'), (' ', ':'), ('t', 'NN'), ('h', 'NN'), ('e', 'NN'), (' ', ':'), ('f', 'NN'), ('i', 'PRP'), ('g', 'VBP'), ('h', 'JJ'), ('t', 'NN'), ('i', 'PRP'), ('n', 'VBP'), ('g', 'JJ'), (' ', 'NN'), ('s', 'NNS'), ('e', 'VBP'), ('c', 'NN'), ('t', 'NN'), ('a', 'DT'), ('r', 'NN'), ('i', 'PRP'), ('a', 'DT'), ('n', 'NN'), (' ', ':'), ('i', 'PRP'), ('n', 'VBP'), (' ', ':'), ('i', 'PRP'), ('r', 'VBP'), ('a', 'DT'), ('q', 'NN'), (' ', ':'), ('.', '.')]
>>> from nltk import tokenize
>>> h
'the army turkish has no interest in take risks implied participation in the fighting sectarian in iraq .'
>>> text_h = word_tokenize(h)

Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    text_h = word_tokenize(h)
NameError: name 'word_tokenize' is not defined
>>> import nltk.data
>>> text_h = word_tokenize(h)

Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    text_h = word_tokenize(h)
NameError: name 'word_tokenize' is not defined
>>> from nltk.tokenize import word_tokenize
>>> text_h = word_tokenize(h)
>>> text_h
['the', 'army', 'turkish', 'has', 'no', 'interest', 'in', 'take', 'risks', 'implied', 'participation', 'in', 'the', 'fighting', 'sectarian', 'in', 'iraq', '.']
>>> nltk.pos_tag(text)

Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    nltk.pos_tag(text)
NameError: name 'text' is not defined
>>> nltk.pos_tag(text_h)
[('the', 'DT'), ('army', 'NN'), ('turkish', 'NN'), ('has', 'VBZ'), ('no', 'DT'), ('interest', 'NN'), ('in', 'IN'), ('take', 'NN'), ('risks', 'NNS'), ('implied', 'VBD'), ('participation', 'NN'), ('in', 'IN'), ('the', 'DT'), ('fighting', 'NN'), ('sectarian', 'NN'), ('in', 'IN'), ('iraq', 'NN'), ('.', '.')]
>>> postags = nltk.pos_tag(text_h)
>>> postags
[('the', 'DT'), ('army', 'NN'), ('turkish', 'NN'), ('has', 'VBZ'), ('no', 'DT'), ('interest', 'NN'), ('in', 'IN'), ('take', 'NN'), ('risks', 'NNS'), ('implied', 'VBD'), ('participation', 'NN'), ('in', 'IN'), ('the', 'DT'), ('fighting', 'NN'), ('sectarian', 'NN'), ('in', 'IN'), ('iraq', 'NN'), ('.', '.')]
>>> nouns = ["NN", "NNS", "NNP", "NNPS", "PRP", "PRP$"]
>>> adjectives = ["JJ", "JJR", "JJS"]
>>> len(postags)
18
>>> for x in range(len(postags)-1):
	print postags[n][0],

	

Traceback (most recent call last):
  File "<pyshell#52>", line 2, in <module>
    print postags[n][0],
NameError: name 'n' is not defined
>>> for x in range(len(postags)-1):
	print postags[x][0],

	
the army turkish has no interest in take risks implied participation in the fighting sectarian in iraq
>>> from nltk.tag.stanford import POSTagger
>>> h
'the army turkish has no interest in take risks implied participation in the fighting sectarian in iraq .'
>>> st = POSTagger('/usr/share/stanford-postagger/models/english-bidirectional-distsim.tagger', '/usr/share/stanford-postagger/stanford-postagger.jar', "UTF-8")

Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    st = POSTagger('/usr/share/stanford-postagger/models/english-bidirectional-distsim.tagger', '/usr/share/stanford-postagger/stanford-postagger.jar', "UTF-8")
  File "/usr/local/lib/python2.7/dist-packages/nltk/tag/stanford.py", line 124, in __init__
    super(POSTagger, self).__init__(*args, **kwargs)
  File "/usr/local/lib/python2.7/dist-packages/nltk/tag/stanford.py", line 47, in __init__
    verbose=verbose)
  File "/usr/local/lib/python2.7/dist-packages/nltk/internals.py", line 644, in find_jar
    searchpath, url, verbose, is_regex))
  File "/usr/local/lib/python2.7/dist-packages/nltk/internals.py", line 577, in find_jar_iter
    (name_pattern, path_to_jar))
LookupError: Could not find stanford-postagger.jar jar file at /usr/share/stanford-postagger/stanford-postagger.jar
>>> h = "the army turkish has no interest in take risks implied participation in the fighting sectarian in iraq ."
>>> text_h = word_tokenize(h)
>>> text_h
['the', 'army', 'turkish', 'has', 'no', 'interest', 'in', 'take', 'risks', 'implied', 'participation', 'in', 'the', 'fighting', 'sectarian', 'in', 'iraq', '.']
>>> postags = nltk.pos_tag(text_h)
>>> postags
[('the', 'DT'), ('army', 'NN'), ('turkish', 'NN'), ('has', 'VBZ'), ('no', 'DT'), ('interest', 'NN'), ('in', 'IN'), ('take', 'NN'), ('risks', 'NNS'), ('implied', 'VBD'), ('participation', 'NN'), ('in', 'IN'), ('the', 'DT'), ('fighting', 'NN'), ('sectarian', 'NN'), ('in', 'IN'), ('iraq', 'NN'), ('.', '.')]
>>> st = POSTagger("/home/andrew/Desktop/stanford-postagger-2015-01-30/models/english-bidirectional-distsim.tagger
	       
SyntaxError: EOL while scanning string literal
>>> st = POSTagger("/home/andrew/Desktop/stanford-postagger-2015-01-30/models/english-bidirectional-distsim.tagger", "/home/andrew/Desktop/stanford-postagger-2015-01-30/stanford-postagger-3.5.1.jar", "UTF-8")
>>> st.tag(h.split())
Exception in thread "main" java.lang.UnsupportedClassVersionError: edu/stanford/nlp/tagger/maxent/MaxentTagger : Unsupported major.minor version 52.0
	at java.lang.ClassLoader.defineClass1(Native Method)
	at java.lang.ClassLoader.defineClass(ClassLoader.java:800)
	at java.security.SecureClassLoader.defineClass(SecureClassLoader.java:142)
	at java.net.URLClassLoader.defineClass(URLClassLoader.java:449)
	at java.net.URLClassLoader.access$100(URLClassLoader.java:71)
	at java.net.URLClassLoader$1.run(URLClassLoader.java:361)
	at java.net.URLClassLoader$1.run(URLClassLoader.java:355)
	at java.security.AccessController.doPrivileged(Native Method)
	at java.net.URLClassLoader.findClass(URLClassLoader.java:354)
	at java.lang.ClassLoader.loadClass(ClassLoader.java:425)
	at sun.misc.Launcher$AppClassLoader.loadClass(Launcher.java:308)
	at java.lang.ClassLoader.loadClass(ClassLoader.java:358)
	at sun.launcher.LauncherHelper.checkAndLoadMain(LauncherHelper.java:482)


Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    st.tag(h.split())
  File "/usr/local/lib/python2.7/dist-packages/nltk/tag/stanford.py", line 59, in tag
    return self.tag_sents([tokens])[0]
  File "/usr/local/lib/python2.7/dist-packages/nltk/tag/stanford.py", line 81, in tag_sents
    stdout=PIPE, stderr=PIPE)
  File "/usr/local/lib/python2.7/dist-packages/nltk/internals.py", line 160, in java
    raise OSError('Java command failed!')
OSError: Java command failed!
>>> h.split9)
SyntaxError: invalid syntax
>>> h.split()
['the', 'army', 'turkish', 'has', 'no', 'interest', 'in', 'take', 'risks', 'implied', 'participation', 'in', 'the', 'fighting', 'sectarian', 'in', 'iraq', '.']
>>> h_text

Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    h_text
NameError: name 'h_text' is not defined
>>> text_h
['the', 'army', 'turkish', 'has', 'no', 'interest', 'in', 'take', 'risks', 'implied', 'participation', 'in', 'the', 'fighting', 'sectarian', 'in', 'iraq', '.']
>>> st.tag(text_h)
Exception in thread "main" java.lang.UnsupportedClassVersionError: edu/stanford/nlp/tagger/maxent/MaxentTagger : Unsupported major.minor version 52.0
	at java.lang.ClassLoader.defineClass1(Native Method)
	at java.lang.ClassLoader.defineClass(ClassLoader.java:800)
	at java.security.SecureClassLoader.defineClass(SecureClassLoader.java:142)
	at java.net.URLClassLoader.defineClass(URLClassLoader.java:449)
	at java.net.URLClassLoader.access$100(URLClassLoader.java:71)
	at java.net.URLClassLoader$1.run(URLClassLoader.java:361)
	at java.net.URLClassLoader$1.run(URLClassLoader.java:355)
	at java.security.AccessController.doPrivileged(Native Method)
	at java.net.URLClassLoader.findClass(URLClassLoader.java:354)
	at java.lang.ClassLoader.loadClass(ClassLoader.java:425)
	at sun.misc.Launcher$AppClassLoader.loadClass(Launcher.java:308)
	at java.lang.ClassLoader.loadClass(ClassLoader.java:358)
	at sun.launcher.LauncherHelper.checkAndLoadMain(LauncherHelper.java:482)


Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    st.tag(text_h)
  File "/usr/local/lib/python2.7/dist-packages/nltk/tag/stanford.py", line 59, in tag
    return self.tag_sents([tokens])[0]
  File "/usr/local/lib/python2.7/dist-packages/nltk/tag/stanford.py", line 81, in tag_sents
    stdout=PIPE, stderr=PIPE)
  File "/usr/local/lib/python2.7/dist-packages/nltk/internals.py", line 160, in java
    raise OSError('Java command failed!')
OSError: Java command failed!
>>> st = POSTagger("/home/andrew/Desktop/stanford-postagger-2014-8-27/models/english-bidirectional-distsim.tagger", "/home/andrew/Desktop/stanford-postagger-2014-8-27/stanford-postagger-3.4.1.jar", "UTF-8")

Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    st = POSTagger("/home/andrew/Desktop/stanford-postagger-2014-8-27/models/english-bidirectional-distsim.tagger", "/home/andrew/Desktop/stanford-postagger-2014-8-27/stanford-postagger-3.4.1.jar", "UTF-8")
  File "/usr/local/lib/python2.7/dist-packages/nltk/tag/stanford.py", line 124, in __init__
    super(POSTagger, self).__init__(*args, **kwargs)
  File "/usr/local/lib/python2.7/dist-packages/nltk/tag/stanford.py", line 47, in __init__
    verbose=verbose)
  File "/usr/local/lib/python2.7/dist-packages/nltk/internals.py", line 644, in find_jar
    searchpath, url, verbose, is_regex))
  File "/usr/local/lib/python2.7/dist-packages/nltk/internals.py", line 577, in find_jar_iter
    (name_pattern, path_to_jar))
LookupError: Could not find stanford-postagger.jar jar file at /home/andrew/Desktop/stanford-postagger-2014-8-27/stanford-postagger-3.4.1.jar
>>> st = POSTagger("/home/andrew/Desktop/stanford-postagger-2014-08-27/models/english-bidirectional-distsim.tagger", "/home/andrew/Desktop/stanford-postagger-2014-08-27/stanford-postagger-3.4.1.jar", "UTF-8")
>>> st
<nltk.tag.stanford.POSTagger object at 0x7f4340768e50>
>>> st.tag(text_h)
[(u'the', u'DT'), (u'army', u'NN'), (u'turkish', u'NN'), (u'has', u'VBZ'), (u'no', u'DT'), (u'interest', u'NN'), (u'in', u'IN'), (u'take', u'NN'), (u'risks', u'NNS'), (u'implied', u'VBD'), (u'participation', u'NN'), (u'in', u'IN'), (u'the', u'DT'), (u'fighting', u'VBG'), (u'sectarian', u'NN'), (u'in', u'IN'), (u'iraq', u'NN'), (u'.', u'.')]
>>> h = "for citizens young , islamists , in particular , outlets normal for political involvement have closed ."
>>> token_h = word_tokenize(h)
>>> token_h
['for', 'citizens', 'young', ',', 'islamists', ',', 'in', 'particular', ',', 'outlets', 'normal', 'for', 'political', 'involvement', 'have', 'closed', '.']
>>> st.tag(token_h)
[(u'for', u'IN'), (u'citizens', u'NNS'), (u'young', u'JJ'), (u',', u','), (u'islamists', u'NNS'), (u',', u','), (u'in', u'IN'), (u'particular', u'JJ'), (u',', u','), (u'outlets', u'NNS'), (u'normal', u'JJ'), (u'for', u'IN'), (u'political', u'JJ'), (u'involvement', u'NN'), (u'have', u'VBP'), (u'closed', u'VBN'), (u'.', u'.')]
>>> tag_h = st.tag(token_h)
>>> nouns
['NN', 'NNS', 'NNP', 'NNPS', 'PRP', 'PRP$']
>>> nouns = [u"NN", u"NNS", u"NNP", u"NNPS", u"PRP", u"PRP$"]
>>> adjectives
['JJ', 'JJR', 'JJS']
>>> adjectives = [u"JJ", u"JJR", u"JJS"]
>>> new_sent = []
>>> for x in range(len(tag_h)-2):
	if tag_h[x][1] in nouns nad tag_h[x+1][1] in adjective:
		
SyntaxError: invalid syntax
>>> for x in range(len(tag_h)-2):
	print "x =", x
	if tag_h[x][1] in nouns and tag_h[x+1][1] in adjective:
		new_sent.append(tag_h[x+1][0])
		new_sent.append(tag_h[x][0])
		x += 1
		print "x = ", x
	else:
		new_sent.append(tag_h[x])

		
x = 0
x = 1

Traceback (most recent call last):
  File "<pyshell#96>", line 3, in <module>
    if tag_h[x][1] in nouns and tag_h[x+1][1] in adjective:
NameError: name 'adjective' is not defined
>>> for x in range(len(tag_h)-2):
	print "x =", x
	if tag_h[x][1] in nouns and tag_h[x+1][1] in adjectives:
		new_sent.append(tag_h[x+1][0])
		new_sent.append(tag_h[x][0])
		x += 1
		print "x = ", x
	else:
		new_sent.append(tag_h[x])

		
x = 0
x = 1
x =  2
x = 2
x = 3
x = 4
x = 5
x = 6
x = 7
x = 8
x = 9
x =  10
x = 10
x = 11
x = 12
x = 13
x = 14
>>> new_sent
[(u'for', u'IN'), (u'for', u'IN'), u'young', u'citizens', (u'young', u'JJ'), (u',', u','), (u'islamists', u'NNS'), (u',', u','), (u'in', u'IN'), (u'particular', u'JJ'), (u',', u','), u'normal', u'outlets', (u'normal', u'JJ'), (u'for', u'IN'), (u'political', u'JJ'), (u'involvement', u'NN'), (u'have', u'VBP')]
>>> new_sent = []
>>> for x in range(len(tag_h)-2):
	print "x =", x
	if tag_h[x][1] in nouns and tag_h[x+1][1] in adjectives:
		new_sent.append(tag_h[x+1][0])
		new_sent.append(tag_h[x][0])
		x += 1
		print "x = ", x
		print new_sent
	else:
		new_sent.append(tag_h[x])
		print new_sent

		
x = 0
[(u'for', u'IN')]
x = 1
x =  2
[(u'for', u'IN'), u'young', u'citizens']
x = 2
[(u'for', u'IN'), u'young', u'citizens', (u'young', u'JJ')]
x = 3
[(u'for', u'IN'), u'young', u'citizens', (u'young', u'JJ'), (u',', u',')]
x = 4
[(u'for', u'IN'), u'young', u'citizens', (u'young', u'JJ'), (u',', u','), (u'islamists', u'NNS')]
x = 5
[(u'for', u'IN'), u'young', u'citizens', (u'young', u'JJ'), (u',', u','), (u'islamists', u'NNS'), (u',', u',')]
x = 6
[(u'for', u'IN'), u'young', u'citizens', (u'young', u'JJ'), (u',', u','), (u'islamists', u'NNS'), (u',', u','), (u'in', u'IN')]
x = 7
[(u'for', u'IN'), u'young', u'citizens', (u'young', u'JJ'), (u',', u','), (u'islamists', u'NNS'), (u',', u','), (u'in', u'IN'), (u'particular', u'JJ')]
x = 8
[(u'for', u'IN'), u'young', u'citizens', (u'young', u'JJ'), (u',', u','), (u'islamists', u'NNS'), (u',', u','), (u'in', u'IN'), (u'particular', u'JJ'), (u',', u',')]
x = 9
x =  10
[(u'for', u'IN'), u'young', u'citizens', (u'young', u'JJ'), (u',', u','), (u'islamists', u'NNS'), (u',', u','), (u'in', u'IN'), (u'particular', u'JJ'), (u',', u','), u'normal', u'outlets']
x = 10
[(u'for', u'IN'), u'young', u'citizens', (u'young', u'JJ'), (u',', u','), (u'islamists', u'NNS'), (u',', u','), (u'in', u'IN'), (u'particular', u'JJ'), (u',', u','), u'normal', u'outlets', (u'normal', u'JJ')]
x = 11
[(u'for', u'IN'), u'young', u'citizens', (u'young', u'JJ'), (u',', u','), (u'islamists', u'NNS'), (u',', u','), (u'in', u'IN'), (u'particular', u'JJ'), (u',', u','), u'normal', u'outlets', (u'normal', u'JJ'), (u'for', u'IN')]
x = 12
[(u'for', u'IN'), u'young', u'citizens', (u'young', u'JJ'), (u',', u','), (u'islamists', u'NNS'), (u',', u','), (u'in', u'IN'), (u'particular', u'JJ'), (u',', u','), u'normal', u'outlets', (u'normal', u'JJ'), (u'for', u'IN'), (u'political', u'JJ')]
x = 13
[(u'for', u'IN'), u'young', u'citizens', (u'young', u'JJ'), (u',', u','), (u'islamists', u'NNS'), (u',', u','), (u'in', u'IN'), (u'particular', u'JJ'), (u',', u','), u'normal', u'outlets', (u'normal', u'JJ'), (u'for', u'IN'), (u'political', u'JJ'), (u'involvement', u'NN')]
x = 14
[(u'for', u'IN'), u'young', u'citizens', (u'young', u'JJ'), (u',', u','), (u'islamists', u'NNS'), (u',', u','), (u'in', u'IN'), (u'particular', u'JJ'), (u',', u','), u'normal', u'outlets', (u'normal', u'JJ'), (u'for', u'IN'), (u'political', u'JJ'), (u'involvement', u'NN'), (u'have', u'VBP')]
>>> for x in range(len(tag_h)-2):
	print "x =", x
	if tag_h[x][1] in nouns and tag_h[x+1][1] in adjectives:
		new_sent.append(tag_h[x+1][0])
		new_sent.append(tag_h[x][0])
		print "x = ", x
		print new_sent
	else:
		new_sent.append(tag_h[x])
		print new_sent

		
x = 0
[(u'for', u'IN'), u'young', u'citizens', (u'young', u'JJ'), (u',', u','), (u'islamists', u'NNS'), (u',', u','), (u'in', u'IN'), (u'particular', u'JJ'), (u',', u','), u'normal', u'outlets', (u'normal', u'JJ'), (u'for', u'IN'), (u'political', u'JJ'), (u'involvement', u'NN'), (u'have', u'VBP'), (u'for', u'IN')]
x = 1
x =  1
[(u'for', u'IN'), u'young', u'citizens', (u'young', u'JJ'), (u',', u','), (u'islamists', u'NNS'), (u',', u','), (u'in', u'IN'), (u'particular', u'JJ'), (u',', u','), u'normal', u'outlets', (u'normal', u'JJ'), (u'for', u'IN'), (u'political', u'JJ'), (u'involvement', u'NN'), (u'have', u'VBP'), (u'for', u'IN'), u'young', u'citizens']
x = 2
[(u'for', u'IN'), u'young', u'citizens', (u'young', u'JJ'), (u',', u','), (u'islamists', u'NNS'), (u',', u','), (u'in', u'IN'), (u'particular', u'JJ'), (u',', u','), u'normal', u'outlets', (u'normal', u'JJ'), (u'for', u'IN'), (u'political', u'JJ'), (u'involvement', u'NN'), (u'have', u'VBP'), (u'for', u'IN'), u'young', u'citizens', (u'young', u'JJ')]
x = 3
[(u'for', u'IN'), u'young', u'citizens', (u'young', u'JJ'), (u',', u','), (u'islamists', u'NNS'), (u',', u','), (u'in', u'IN'), (u'particular', u'JJ'), (u',', u','), u'normal', u'outlets', (u'normal', u'JJ'), (u'for', u'IN'), (u'political', u'JJ'), (u'involvement', u'NN'), (u'have', u'VBP'), (u'for', u'IN'), u'young', u'citizens', (u'young', u'JJ'), (u',', u',')]
x = 4
[(u'for', u'IN'), u'young', u'citizens', (u'young', u'JJ'), (u',', u','), (u'islamists', u'NNS'), (u',', u','), (u'in', u'IN'), (u'particular', u'JJ'), (u',', u','), u'normal', u'outlets', (u'normal', u'JJ'), (u'for', u'IN'), (u'political', u'JJ'), (u'involvement', u'NN'), (u'have', u'VBP'), (u'for', u'IN'), u'young', u'citizens', (u'young', u'JJ'), (u',', u','), (u'islamists', u'NNS')]
x = 5
[(u'for', u'IN'), u'young', u'citizens', (u'young', u'JJ'), (u',', u','), (u'islamists', u'NNS'), (u',', u','), (u'in', u'IN'), (u'particular', u'JJ'), (u',', u','), u'normal', u'outlets', (u'normal', u'JJ'), (u'for', u'IN'), (u'political', u'JJ'), (u'involvement', u'NN'), (u'have', u'VBP'), (u'for', u'IN'), u'young', u'citizens', (u'young', u'JJ'), (u',', u','), (u'islamists', u'NNS'), (u',', u',')]
x = 6
[(u'for', u'IN'), u'young', u'citizens', (u'young', u'JJ'), (u',', u','), (u'islamists', u'NNS'), (u',', u','), (u'in', u'IN'), (u'particular', u'JJ'), (u',', u','), u'normal', u'outlets', (u'normal', u'JJ'), (u'for', u'IN'), (u'political', u'JJ'), (u'involvement', u'NN'), (u'have', u'VBP'), (u'for', u'IN'), u'young', u'citizens', (u'young', u'JJ'), (u',', u','), (u'islamists', u'NNS'), (u',', u','), (u'in', u'IN')]
x = 7
[(u'for', u'IN'), u'young', u'citizens', (u'young', u'JJ'), (u',', u','), (u'islamists', u'NNS'), (u',', u','), (u'in', u'IN'), (u'particular', u'JJ'), (u',', u','), u'normal', u'outlets', (u'normal', u'JJ'), (u'for', u'IN'), (u'political', u'JJ'), (u'involvement', u'NN'), (u'have', u'VBP'), (u'for', u'IN'), u'young', u'citizens', (u'young', u'JJ'), (u',', u','), (u'islamists', u'NNS'), (u',', u','), (u'in', u'IN'), (u'particular', u'JJ')]
x = 8
[(u'for', u'IN'), u'young', u'citizens', (u'young', u'JJ'), (u',', u','), (u'islamists', u'NNS'), (u',', u','), (u'in', u'IN'), (u'particular', u'JJ'), (u',', u','), u'normal', u'outlets', (u'normal', u'JJ'), (u'for', u'IN'), (u'political', u'JJ'), (u'involvement', u'NN'), (u'have', u'VBP'), (u'for', u'IN'), u'young', u'citizens', (u'young', u'JJ'), (u',', u','), (u'islamists', u'NNS'), (u',', u','), (u'in', u'IN'), (u'particular', u'JJ'), (u',', u',')]
x = 9
x =  9
[(u'for', u'IN'), u'young', u'citizens', (u'young', u'JJ'), (u',', u','), (u'islamists', u'NNS'), (u',', u','), (u'in', u'IN'), (u'particular', u'JJ'), (u',', u','), u'normal', u'outlets', (u'normal', u'JJ'), (u'for', u'IN'), (u'political', u'JJ'), (u'involvement', u'NN'), (u'have', u'VBP'), (u'for', u'IN'), u'young', u'citizens', (u'young', u'JJ'), (u',', u','), (u'islamists', u'NNS'), (u',', u','), (u'in', u'IN'), (u'particular', u'JJ'), (u',', u','), u'normal', u'outlets']
x = 10
[(u'for', u'IN'), u'young', u'citizens', (u'young', u'JJ'), (u',', u','), (u'islamists', u'NNS'), (u',', u','), (u'in', u'IN'), (u'particular', u'JJ'), (u',', u','), u'normal', u'outlets', (u'normal', u'JJ'), (u'for', u'IN'), (u'political', u'JJ'), (u'involvement', u'NN'), (u'have', u'VBP'), (u'for', u'IN'), u'young', u'citizens', (u'young', u'JJ'), (u',', u','), (u'islamists', u'NNS'), (u',', u','), (u'in', u'IN'), (u'particular', u'JJ'), (u',', u','), u'normal', u'outlets', (u'normal', u'JJ')]
x = 11
[(u'for', u'IN'), u'young', u'citizens', (u'young', u'JJ'), (u',', u','), (u'islamists', u'NNS'), (u',', u','), (u'in', u'IN'), (u'particular', u'JJ'), (u',', u','), u'normal', u'outlets', (u'normal', u'JJ'), (u'for', u'IN'), (u'political', u'JJ'), (u'involvement', u'NN'), (u'have', u'VBP'), (u'for', u'IN'), u'young', u'citizens', (u'young', u'JJ'), (u',', u','), (u'islamists', u'NNS'), (u',', u','), (u'in', u'IN'), (u'particular', u'JJ'), (u',', u','), u'normal', u'outlets', (u'normal', u'JJ'), (u'for', u'IN')]
x = 12
[(u'for', u'IN'), u'young', u'citizens', (u'young', u'JJ'), (u',', u','), (u'islamists', u'NNS'), (u',', u','), (u'in', u'IN'), (u'particular', u'JJ'), (u',', u','), u'normal', u'outlets', (u'normal', u'JJ'), (u'for', u'IN'), (u'political', u'JJ'), (u'involvement', u'NN'), (u'have', u'VBP'), (u'for', u'IN'), u'young', u'citizens', (u'young', u'JJ'), (u',', u','), (u'islamists', u'NNS'), (u',', u','), (u'in', u'IN'), (u'particular', u'JJ'), (u',', u','), u'normal', u'outlets', (u'normal', u'JJ'), (u'for', u'IN'), (u'political', u'JJ')]
x = 13
[(u'for', u'IN'), u'young', u'citizens', (u'young', u'JJ'), (u',', u','), (u'islamists', u'NNS'), (u',', u','), (u'in', u'IN'), (u'particular', u'JJ'), (u',', u','), u'normal', u'outlets', (u'normal', u'JJ'), (u'for', u'IN'), (u'political', u'JJ'), (u'involvement', u'NN'), (u'have', u'VBP'), (u'for', u'IN'), u'young', u'citizens', (u'young', u'JJ'), (u',', u','), (u'islamists', u'NNS'), (u',', u','), (u'in', u'IN'), (u'particular', u'JJ'), (u',', u','), u'normal', u'outlets', (u'normal', u'JJ'), (u'for', u'IN'), (u'political', u'JJ'), (u'involvement', u'NN')]
x = 14
[(u'for', u'IN'), u'young', u'citizens', (u'young', u'JJ'), (u',', u','), (u'islamists', u'NNS'), (u',', u','), (u'in', u'IN'), (u'particular', u'JJ'), (u',', u','), u'normal', u'outlets', (u'normal', u'JJ'), (u'for', u'IN'), (u'political', u'JJ'), (u'involvement', u'NN'), (u'have', u'VBP'), (u'for', u'IN'), u'young', u'citizens', (u'young', u'JJ'), (u',', u','), (u'islamists', u'NNS'), (u',', u','), (u'in', u'IN'), (u'particular', u'JJ'), (u',', u','), u'normal', u'outlets', (u'normal', u'JJ'), (u'for', u'IN'), (u'political', u'JJ'), (u'involvement', u'NN'), (u'have', u'VBP')]
>>> for x in range(len(tag_h)-2):
	print "x =", x
	if tag_h[x][1] in nouns and tag_h[x+1][1] in adjectives:
		new_sent.append(tag_h[x+1][0])
		new_sent.append(tag_h[x][0])
		print "x = ", x
		print new_sent
	else:
		new_sent.append(tag_h[x][1])
		print new_sent

		
x = 0
[(u'for', u'IN'), u'young', u'citizens', (u'young', u'JJ'), (u',', u','), (u'islamists', u'NNS'), (u',', u','), (u'in', u'IN'), (u'particular', u'JJ'), (u',', u','), u'normal', u'outlets', (u'normal', u'JJ'), (u'for', u'IN'), (u'political', u'JJ'), (u'involvement', u'NN'), (u'have', u'VBP'), (u'for', u'IN'), u'young', u'citizens', (u'young', u'JJ'), (u',', u','), (u'islamists', u'NNS'), (u',', u','), (u'in', u'IN'), (u'particular', u'JJ'), (u',', u','), u'normal', u'outlets', (u'normal', u'JJ'), (u'for', u'IN'), (u'political', u'JJ'), (u'involvement', u'NN'), (u'have', u'VBP'), u'IN']
x = 1
x =  1
[(u'for', u'IN'), u'young', u'citizens', (u'young', u'JJ'), (u',', u','), (u'islamists', u'NNS'), (u',', u','), (u'in', u'IN'), (u'particular', u'JJ'), (u',', u','), u'normal', u'outlets', (u'normal', u'JJ'), (u'for', u'IN'), (u'political', u'JJ'), (u'involvement', u'NN'), (u'have', u'VBP'), (u'for', u'IN'), u'young', u'citizens', (u'young', u'JJ'), (u',', u','), (u'islamists', u'NNS'), (u',', u','), (u'in', u'IN'), (u'particular', u'JJ'), (u',', u','), u'normal', u'outlets', (u'normal', u'JJ'), (u'for', u'IN'), (u'political', u'JJ'), (u'involvement', u'NN'), (u'have', u'VBP'), u'IN', u'young', u'citizens']
x = 2
[(u'for', u'IN'), u'young', u'citizens', (u'young', u'JJ'), (u',', u','), (u'islamists', u'NNS'), (u',', u','), (u'in', u'IN'), (u'particular', u'JJ'), (u',', u','), u'normal', u'outlets', (u'normal', u'JJ'), (u'for', u'IN'), (u'political', u'JJ'), (u'involvement', u'NN'), (u'have', u'VBP'), (u'for', u'IN'), u'young', u'citizens', (u'young', u'JJ'), (u',', u','), (u'islamists', u'NNS'), (u',', u','), (u'in', u'IN'), (u'particular', u'JJ'), (u',', u','), u'normal', u'outlets', (u'normal', u'JJ'), (u'for', u'IN'), (u'political', u'JJ'), (u'involvement', u'NN'), (u'have', u'VBP'), u'IN', u'young', u'citizens', u'JJ']
x = 3
[(u'for', u'IN'), u'young', u'citizens', (u'young', u'JJ'), (u',', u','), (u'islamists', u'NNS'), (u',', u','), (u'in', u'IN'), (u'particular', u'JJ'), (u',', u','), u'normal', u'outlets', (u'normal', u'JJ'), (u'for', u'IN'), (u'political', u'JJ'), (u'involvement', u'NN'), (u'have', u'VBP'), (u'for', u'IN'), u'young', u'citizens', (u'young', u'JJ'), (u',', u','), (u'islamists', u'NNS'), (u',', u','), (u'in', u'IN'), (u'particular', u'JJ'), (u',', u','), u'normal', u'outlets', (u'normal', u'JJ'), (u'for', u'IN'), (u'political', u'JJ'), (u'involvement', u'NN'), (u'have', u'VBP'), u'IN', u'young', u'citizens', u'JJ', u',']
x = 4
[(u'for', u'IN'), u'young', u'citizens', (u'young', u'JJ'), (u',', u','), (u'islamists', u'NNS'), (u',', u','), (u'in', u'IN'), (u'particular', u'JJ'), (u',', u','), u'normal', u'outlets', (u'normal', u'JJ'), (u'for', u'IN'), (u'political', u'JJ'), (u'involvement', u'NN'), (u'have', u'VBP'), (u'for', u'IN'), u'young', u'citizens', (u'young', u'JJ'), (u',', u','), (u'islamists', u'NNS'), (u',', u','), (u'in', u'IN'), (u'particular', u'JJ'), (u',', u','), u'normal', u'outlets', (u'normal', u'JJ'), (u'for', u'IN'), (u'political', u'JJ'), (u'involvement', u'NN'), (u'have', u'VBP'), u'IN', u'young', u'citizens', u'JJ', u',', u'NNS']
x = 5
[(u'for', u'IN'), u'young', u'citizens', (u'young', u'JJ'), (u',', u','), (u'islamists', u'NNS'), (u',', u','), (u'in', u'IN'), (u'particular', u'JJ'), (u',', u','), u'normal', u'outlets', (u'normal', u'JJ'), (u'for', u'IN'), (u'political', u'JJ'), (u'involvement', u'NN'), (u'have', u'VBP'), (u'for', u'IN'), u'young', u'citizens', (u'young', u'JJ'), (u',', u','), (u'islamists', u'NNS'), (u',', u','), (u'in', u'IN'), (u'particular', u'JJ'), (u',', u','), u'normal', u'outlets', (u'normal', u'JJ'), (u'for', u'IN'), (u'political', u'JJ'), (u'involvement', u'NN'), (u'have', u'VBP'), u'IN', u'young', u'citizens', u'JJ', u',', u'NNS', u',']
x = 6
[(u'for', u'IN'), u'young', u'citizens', (u'young', u'JJ'), (u',', u','), (u'islamists', u'NNS'), (u',', u','), (u'in', u'IN'), (u'particular', u'JJ'), (u',', u','), u'normal', u'outlets', (u'normal', u'JJ'), (u'for', u'IN'), (u'political', u'JJ'), (u'involvement', u'NN'), (u'have', u'VBP'), (u'for', u'IN'), u'young', u'citizens', (u'young', u'JJ'), (u',', u','), (u'islamists', u'NNS'), (u',', u','), (u'in', u'IN'), (u'particular', u'JJ'), (u',', u','), u'normal', u'outlets', (u'normal', u'JJ'), (u'for', u'IN'), (u'political', u'JJ'), (u'involvement', u'NN'), (u'have', u'VBP'), u'IN', u'young', u'citizens', u'JJ', u',', u'NNS', u',', u'IN']
x = 7
[(u'for', u'IN'), u'young', u'citizens', (u'young', u'JJ'), (u',', u','), (u'islamists', u'NNS'), (u',', u','), (u'in', u'IN'), (u'particular', u'JJ'), (u',', u','), u'normal', u'outlets', (u'normal', u'JJ'), (u'for', u'IN'), (u'political', u'JJ'), (u'involvement', u'NN'), (u'have', u'VBP'), (u'for', u'IN'), u'young', u'citizens', (u'young', u'JJ'), (u',', u','), (u'islamists', u'NNS'), (u',', u','), (u'in', u'IN'), (u'particular', u'JJ'), (u',', u','), u'normal', u'outlets', (u'normal', u'JJ'), (u'for', u'IN'), (u'political', u'JJ'), (u'involvement', u'NN'), (u'have', u'VBP'), u'IN', u'young', u'citizens', u'JJ', u',', u'NNS', u',', u'IN', u'JJ']
x = 8
[(u'for', u'IN'), u'young', u'citizens', (u'young', u'JJ'), (u',', u','), (u'islamists', u'NNS'), (u',', u','), (u'in', u'IN'), (u'particular', u'JJ'), (u',', u','), u'normal', u'outlets', (u'normal', u'JJ'), (u'for', u'IN'), (u'political', u'JJ'), (u'involvement', u'NN'), (u'have', u'VBP'), (u'for', u'IN'), u'young', u'citizens', (u'young', u'JJ'), (u',', u','), (u'islamists', u'NNS'), (u',', u','), (u'in', u'IN'), (u'particular', u'JJ'), (u',', u','), u'normal', u'outlets', (u'normal', u'JJ'), (u'for', u'IN'), (u'political', u'JJ'), (u'involvement', u'NN'), (u'have', u'VBP'), u'IN', u'young', u'citizens', u'JJ', u',', u'NNS', u',', u'IN', u'JJ', u',']
x = 9
x =  9
[(u'for', u'IN'), u'young', u'citizens', (u'young', u'JJ'), (u',', u','), (u'islamists', u'NNS'), (u',', u','), (u'in', u'IN'), (u'particular', u'JJ'), (u',', u','), u'normal', u'outlets', (u'normal', u'JJ'), (u'for', u'IN'), (u'political', u'JJ'), (u'involvement', u'NN'), (u'have', u'VBP'), (u'for', u'IN'), u'young', u'citizens', (u'young', u'JJ'), (u',', u','), (u'islamists', u'NNS'), (u',', u','), (u'in', u'IN'), (u'particular', u'JJ'), (u',', u','), u'normal', u'outlets', (u'normal', u'JJ'), (u'for', u'IN'), (u'political', u'JJ'), (u'involvement', u'NN'), (u'have', u'VBP'), u'IN', u'young', u'citizens', u'JJ', u',', u'NNS', u',', u'IN', u'JJ', u',', u'normal', u'outlets']
x = 10
[(u'for', u'IN'), u'young', u'citizens', (u'young', u'JJ'), (u',', u','), (u'islamists', u'NNS'), (u',', u','), (u'in', u'IN'), (u'particular', u'JJ'), (u',', u','), u'normal', u'outlets', (u'normal', u'JJ'), (u'for', u'IN'), (u'political', u'JJ'), (u'involvement', u'NN'), (u'have', u'VBP'), (u'for', u'IN'), u'young', u'citizens', (u'young', u'JJ'), (u',', u','), (u'islamists', u'NNS'), (u',', u','), (u'in', u'IN'), (u'particular', u'JJ'), (u',', u','), u'normal', u'outlets', (u'normal', u'JJ'), (u'for', u'IN'), (u'political', u'JJ'), (u'involvement', u'NN'), (u'have', u'VBP'), u'IN', u'young', u'citizens', u'JJ', u',', u'NNS', u',', u'IN', u'JJ', u',', u'normal', u'outlets', u'JJ']
x = 11
[(u'for', u'IN'), u'young', u'citizens', (u'young', u'JJ'), (u',', u','), (u'islamists', u'NNS'), (u',', u','), (u'in', u'IN'), (u'particular', u'JJ'), (u',', u','), u'normal', u'outlets', (u'normal', u'JJ'), (u'for', u'IN'), (u'political', u'JJ'), (u'involvement', u'NN'), (u'have', u'VBP'), (u'for', u'IN'), u'young', u'citizens', (u'young', u'JJ'), (u',', u','), (u'islamists', u'NNS'), (u',', u','), (u'in', u'IN'), (u'particular', u'JJ'), (u',', u','), u'normal', u'outlets', (u'normal', u'JJ'), (u'for', u'IN'), (u'political', u'JJ'), (u'involvement', u'NN'), (u'have', u'VBP'), u'IN', u'young', u'citizens', u'JJ', u',', u'NNS', u',', u'IN', u'JJ', u',', u'normal', u'outlets', u'JJ', u'IN']
x = 12
[(u'for', u'IN'), u'young', u'citizens', (u'young', u'JJ'), (u',', u','), (u'islamists', u'NNS'), (u',', u','), (u'in', u'IN'), (u'particular', u'JJ'), (u',', u','), u'normal', u'outlets', (u'normal', u'JJ'), (u'for', u'IN'), (u'political', u'JJ'), (u'involvement', u'NN'), (u'have', u'VBP'), (u'for', u'IN'), u'young', u'citizens', (u'young', u'JJ'), (u',', u','), (u'islamists', u'NNS'), (u',', u','), (u'in', u'IN'), (u'particular', u'JJ'), (u',', u','), u'normal', u'outlets', (u'normal', u'JJ'), (u'for', u'IN'), (u'political', u'JJ'), (u'involvement', u'NN'), (u'have', u'VBP'), u'IN', u'young', u'citizens', u'JJ', u',', u'NNS', u',', u'IN', u'JJ', u',', u'normal', u'outlets', u'JJ', u'IN', u'JJ']
x = 13
[(u'for', u'IN'), u'young', u'citizens', (u'young', u'JJ'), (u',', u','), (u'islamists', u'NNS'), (u',', u','), (u'in', u'IN'), (u'particular', u'JJ'), (u',', u','), u'normal', u'outlets', (u'normal', u'JJ'), (u'for', u'IN'), (u'political', u'JJ'), (u'involvement', u'NN'), (u'have', u'VBP'), (u'for', u'IN'), u'young', u'citizens', (u'young', u'JJ'), (u',', u','), (u'islamists', u'NNS'), (u',', u','), (u'in', u'IN'), (u'particular', u'JJ'), (u',', u','), u'normal', u'outlets', (u'normal', u'JJ'), (u'for', u'IN'), (u'political', u'JJ'), (u'involvement', u'NN'), (u'have', u'VBP'), u'IN', u'young', u'citizens', u'JJ', u',', u'NNS', u',', u'IN', u'JJ', u',', u'normal', u'outlets', u'JJ', u'IN', u'JJ', u'NN']
x = 14
[(u'for', u'IN'), u'young', u'citizens', (u'young', u'JJ'), (u',', u','), (u'islamists', u'NNS'), (u',', u','), (u'in', u'IN'), (u'particular', u'JJ'), (u',', u','), u'normal', u'outlets', (u'normal', u'JJ'), (u'for', u'IN'), (u'political', u'JJ'), (u'involvement', u'NN'), (u'have', u'VBP'), (u'for', u'IN'), u'young', u'citizens', (u'young', u'JJ'), (u',', u','), (u'islamists', u'NNS'), (u',', u','), (u'in', u'IN'), (u'particular', u'JJ'), (u',', u','), u'normal', u'outlets', (u'normal', u'JJ'), (u'for', u'IN'), (u'political', u'JJ'), (u'involvement', u'NN'), (u'have', u'VBP'), u'IN', u'young', u'citizens', u'JJ', u',', u'NNS', u',', u'IN', u'JJ', u',', u'normal', u'outlets', u'JJ', u'IN', u'JJ', u'NN', u'VBP']
>>> new_sent = []
>>> for x in range(len(tag_h)-2):
	print "x =", x
	if tag_h[x][1] in nouns and tag_h[x+1][1] in adjectives:
		new_sent.append(tag_h[x+1][0])
		new_sent.append(tag_h[x][0])
		print "x = ", x
		print new_sent
	else:
		new_sent.append(tag_h[x][1])
		print new_sent

		
x = 0
[u'IN']
x = 1
x =  1
[u'IN', u'young', u'citizens']
x = 2
[u'IN', u'young', u'citizens', u'JJ']
x = 3
[u'IN', u'young', u'citizens', u'JJ', u',']
x = 4
[u'IN', u'young', u'citizens', u'JJ', u',', u'NNS']
x = 5
[u'IN', u'young', u'citizens', u'JJ', u',', u'NNS', u',']
x = 6
[u'IN', u'young', u'citizens', u'JJ', u',', u'NNS', u',', u'IN']
x = 7
[u'IN', u'young', u'citizens', u'JJ', u',', u'NNS', u',', u'IN', u'JJ']
x = 8
[u'IN', u'young', u'citizens', u'JJ', u',', u'NNS', u',', u'IN', u'JJ', u',']
x = 9
x =  9
[u'IN', u'young', u'citizens', u'JJ', u',', u'NNS', u',', u'IN', u'JJ', u',', u'normal', u'outlets']
x = 10
[u'IN', u'young', u'citizens', u'JJ', u',', u'NNS', u',', u'IN', u'JJ', u',', u'normal', u'outlets', u'JJ']
x = 11
[u'IN', u'young', u'citizens', u'JJ', u',', u'NNS', u',', u'IN', u'JJ', u',', u'normal', u'outlets', u'JJ', u'IN']
x = 12
[u'IN', u'young', u'citizens', u'JJ', u',', u'NNS', u',', u'IN', u'JJ', u',', u'normal', u'outlets', u'JJ', u'IN', u'JJ']
x = 13
[u'IN', u'young', u'citizens', u'JJ', u',', u'NNS', u',', u'IN', u'JJ', u',', u'normal', u'outlets', u'JJ', u'IN', u'JJ', u'NN']
x = 14
[u'IN', u'young', u'citizens', u'JJ', u',', u'NNS', u',', u'IN', u'JJ', u',', u'normal', u'outlets', u'JJ', u'IN', u'JJ', u'NN', u'VBP']
>>> new_sent = []
for x in range(len(tag_h)-2):
	print "x =", x
	if tag_h[x][1] in nouns and tag_h[x+1][1] in adjectives:
		new_sent.append(tag_h[x+1][0])
		new_sent.append(tag_h[x][0])
		print "x = ", x
		print new_sent
	else:
		new_sent.append(tag_h[x][0])
		print new_sent
		
>>> new_sent = []
>>> for x in range(len(tag_h)-2):
	print "x =", x
	if tag_h[x][1] in nouns and tag_h[x+1][1] in adjectives:
		new_sent.append(tag_h[x+1][0])
		new_sent.append(tag_h[x][0])
		print "x = ", x
		print new_sent
	else:
		new_sent.append(tag_h[x][0])
		print new_sent

		
x = 0
[u'for']
x = 1
x =  1
[u'for', u'young', u'citizens']
x = 2
[u'for', u'young', u'citizens', u'young']
x = 3
[u'for', u'young', u'citizens', u'young', u',']
x = 4
[u'for', u'young', u'citizens', u'young', u',', u'islamists']
x = 5
[u'for', u'young', u'citizens', u'young', u',', u'islamists', u',']
x = 6
[u'for', u'young', u'citizens', u'young', u',', u'islamists', u',', u'in']
x = 7
[u'for', u'young', u'citizens', u'young', u',', u'islamists', u',', u'in', u'particular']
x = 8
[u'for', u'young', u'citizens', u'young', u',', u'islamists', u',', u'in', u'particular', u',']
x = 9
x =  9
[u'for', u'young', u'citizens', u'young', u',', u'islamists', u',', u'in', u'particular', u',', u'normal', u'outlets']
x = 10
[u'for', u'young', u'citizens', u'young', u',', u'islamists', u',', u'in', u'particular', u',', u'normal', u'outlets', u'normal']
x = 11
[u'for', u'young', u'citizens', u'young', u',', u'islamists', u',', u'in', u'particular', u',', u'normal', u'outlets', u'normal', u'for']
x = 12
[u'for', u'young', u'citizens', u'young', u',', u'islamists', u',', u'in', u'particular', u',', u'normal', u'outlets', u'normal', u'for', u'political']
x = 13
[u'for', u'young', u'citizens', u'young', u',', u'islamists', u',', u'in', u'particular', u',', u'normal', u'outlets', u'normal', u'for', u'political', u'involvement']
x = 14
[u'for', u'young', u'citizens', u'young', u',', u'islamists', u',', u'in', u'particular', u',', u'normal', u'outlets', u'normal', u'for', u'political', u'involvement', u'have']
>>> tag_h
[(u'for', u'IN'), (u'citizens', u'NNS'), (u'young', u'JJ'), (u',', u','), (u'islamists', u'NNS'), (u',', u','), (u'in', u'IN'), (u'particular', u'JJ'), (u',', u','), (u'outlets', u'NNS'), (u'normal', u'JJ'), (u'for', u'IN'), (u'political', u'JJ'), (u'involvement', u'NN'), (u'have', u'VBP'), (u'closed', u'VBN'), (u'.', u'.')]
>>> new_sent = []
>>> for x in range(len(tag_h)-2):
	print "x =", x
	if tag_h[x][1] in nouns and tag_h[x+1][1] in adjectives:
		new_sent.append(tag_h[x+1][0])
		new_sent.append(tag_h[x][0])
		print "x = ", x
		x += 1
		print "new x =", x
		print new_sent
	else:
		new_sent.append(tag_h[x][0])
		print new_sent

		
x = 0
[u'for']
x = 1
x =  1
new x = 2
[u'for', u'young', u'citizens']
x = 2
[u'for', u'young', u'citizens', u'young']
x = 3
[u'for', u'young', u'citizens', u'young', u',']
x = 4
[u'for', u'young', u'citizens', u'young', u',', u'islamists']
x = 5
[u'for', u'young', u'citizens', u'young', u',', u'islamists', u',']
x = 6
[u'for', u'young', u'citizens', u'young', u',', u'islamists', u',', u'in']
x = 7
[u'for', u'young', u'citizens', u'young', u',', u'islamists', u',', u'in', u'particular']
x = 8
[u'for', u'young', u'citizens', u'young', u',', u'islamists', u',', u'in', u'particular', u',']
x = 9
x =  9
new x = 10
[u'for', u'young', u'citizens', u'young', u',', u'islamists', u',', u'in', u'particular', u',', u'normal', u'outlets']
x = 10
[u'for', u'young', u'citizens', u'young', u',', u'islamists', u',', u'in', u'particular', u',', u'normal', u'outlets', u'normal']
x = 11
[u'for', u'young', u'citizens', u'young', u',', u'islamists', u',', u'in', u'particular', u',', u'normal', u'outlets', u'normal', u'for']
x = 12
[u'for', u'young', u'citizens', u'young', u',', u'islamists', u',', u'in', u'particular', u',', u'normal', u'outlets', u'normal', u'for', u'political']
x = 13
[u'for', u'young', u'citizens', u'young', u',', u'islamists', u',', u'in', u'particular', u',', u'normal', u'outlets', u'normal', u'for', u'political', u'involvement']
x = 14
[u'for', u'young', u'citizens', u'young', u',', u'islamists', u',', u'in', u'particular', u',', u'normal', u'outlets', u'normal', u'for', u'political', u'involvement', u'have']
>>> new_sent = []
>>> for x in range(len(tag_h)-2):
	print "x =", x
	if tag_h[x][1] in nouns and tag_h[x+1][1] in adjectives:
		new_sent.append(tag_h[x+1][0])
		new_sent.append(tag_h[x][0])
		print "x = ", x
		
		print "new x =", x
		print new_sent
		continue
	else:
		new_sent.append(tag_h[x][0])
		print new_sent

		
x = 0
[u'for']
x = 1
x =  1
new x = 1
[u'for', u'young', u'citizens']
x = 2
[u'for', u'young', u'citizens', u'young']
x = 3
[u'for', u'young', u'citizens', u'young', u',']
x = 4
[u'for', u'young', u'citizens', u'young', u',', u'islamists']
x = 5
[u'for', u'young', u'citizens', u'young', u',', u'islamists', u',']
x = 6
[u'for', u'young', u'citizens', u'young', u',', u'islamists', u',', u'in']
x = 7
[u'for', u'young', u'citizens', u'young', u',', u'islamists', u',', u'in', u'particular']
x = 8
[u'for', u'young', u'citizens', u'young', u',', u'islamists', u',', u'in', u'particular', u',']
x = 9
x =  9
new x = 9
[u'for', u'young', u'citizens', u'young', u',', u'islamists', u',', u'in', u'particular', u',', u'normal', u'outlets']
x = 10
[u'for', u'young', u'citizens', u'young', u',', u'islamists', u',', u'in', u'particular', u',', u'normal', u'outlets', u'normal']
x = 11
[u'for', u'young', u'citizens', u'young', u',', u'islamists', u',', u'in', u'particular', u',', u'normal', u'outlets', u'normal', u'for']
x = 12
[u'for', u'young', u'citizens', u'young', u',', u'islamists', u',', u'in', u'particular', u',', u'normal', u'outlets', u'normal', u'for', u'political']
x = 13
[u'for', u'young', u'citizens', u'young', u',', u'islamists', u',', u'in', u'particular', u',', u'normal', u'outlets', u'normal', u'for', u'political', u'involvement']
x = 14
[u'for', u'young', u'citizens', u'young', u',', u'islamists', u',', u'in', u'particular', u',', u'normal', u'outlets', u'normal', u'for', u'political', u'involvement', u'have']
>>> tag_h
[(u'for', u'IN'), (u'citizens', u'NNS'), (u'young', u'JJ'), (u',', u','), (u'islamists', u'NNS'), (u',', u','), (u'in', u'IN'), (u'particular', u'JJ'), (u',', u','), (u'outlets', u'NNS'), (u'normal', u'JJ'), (u'for', u'IN'), (u'political', u'JJ'), (u'involvement', u'NN'), (u'have', u'VBP'), (u'closed', u'VBN'), (u'.', u'.')]
>>> for x in range(len(tag_h)-1):
	print x,

	
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
>>> for x in range(len(tag_h)-1):
	print x, tag_h[x],

	
0 (u'for', u'IN') 1 (u'citizens', u'NNS') 2 (u'young', u'JJ') 3 (u',', u',') 4 (u'islamists', u'NNS') 5 (u',', u',') 6 (u'in', u'IN') 7 (u'particular', u'JJ') 8 (u',', u',') 9 (u'outlets', u'NNS') 10 (u'normal', u'JJ') 11 (u'for', u'IN') 12 (u'political', u'JJ') 13 (u'involvement', u'NN') 14 (u'have', u'VBP') 15 (u'closed', u'VBN')
>>> pig = ["a", "b", "c", "d", "e"]
>>> pig[3]
'd'
>>> pig[3] = pig[2]
>>> pig
['a', 'b', 'c', 'c', 'e']
>>> pig = ["a", "b", "c", "d", "e"]
>>> pig[3] = temp

Traceback (most recent call last):
  File "<pyshell#135>", line 1, in <module>
    pig[3] = temp
NameError: name 'temp' is not defined
>>> temp = pig[3]
>>> temp
'd'
>>> pig[3]
'd'
>>> temp = pig[0]
>>> temp2 = pig[4]
>>> pig[0] = temp2
>>> pig[4] = temp
>>> pig
['e', 'b', 'c', 'd', 'a']
>>> oink = tag_h
>>> oink
[(u'for', u'IN'), (u'citizens', u'NNS'), (u'young', u'JJ'), (u',', u','), (u'islamists', u'NNS'), (u',', u','), (u'in', u'IN'), (u'particular', u'JJ'), (u',', u','), (u'outlets', u'NNS'), (u'normal', u'JJ'), (u'for', u'IN'), (u'political', u'JJ'), (u'involvement', u'NN'), (u'have', u'VBP'), (u'closed', u'VBN'), (u'.', u'.')]
>>> for x in range(len(tag_h)-1):
	if tag_h[x][0] in nouns and tag_h[x+1][0] in adjectives:
		temp1 = tag_h[x]
		temp2 = tag_h[x+1]
		tag_h[x] = temp2
		tag_h[x+1] = temp1

		
>>> tag_h
[(u'for', u'IN'), (u'citizens', u'NNS'), (u'young', u'JJ'), (u',', u','), (u'islamists', u'NNS'), (u',', u','), (u'in', u'IN'), (u'particular', u'JJ'), (u',', u','), (u'outlets', u'NNS'), (u'normal', u'JJ'), (u'for', u'IN'), (u'political', u'JJ'), (u'involvement', u'NN'), (u'have', u'VBP'), (u'closed', u'VBN'), (u'.', u'.')]
>>> for x in range(len(tag_h)-1):
	print x, tag_h[x]
	if tag_h[x][0] in nouns and tag_h[x+1][0] in adjectives:
		print True
		temp1 = tag_h[x]
		temp2 = tag_h[x+1]
		tag_h[x] = temp2
		tag_h[x+1] = temp1

		
0 (u'for', u'IN')
1 (u'citizens', u'NNS')
2 (u'young', u'JJ')
3 (u',', u',')
4 (u'islamists', u'NNS')
5 (u',', u',')
6 (u'in', u'IN')
7 (u'particular', u'JJ')
8 (u',', u',')
9 (u'outlets', u'NNS')
10 (u'normal', u'JJ')
11 (u'for', u'IN')
12 (u'political', u'JJ')
13 (u'involvement', u'NN')
14 (u'have', u'VBP')
15 (u'closed', u'VBN')
>>> for x in range(len(tag_h)-1):
	print x, tag_h[x]
	if tag_h[x][1] in nouns and tag_h[x+1][1] in adjectives:
		print True
		temp1 = tag_h[x]
		temp2 = tag_h[x+1]
		tag_h[x] = temp2
		tag_h[x+1] = temp1

		
0 (u'for', u'IN')
1 (u'citizens', u'NNS')
True
2 (u'citizens', u'NNS')
3 (u',', u',')
4 (u'islamists', u'NNS')
5 (u',', u',')
6 (u'in', u'IN')
7 (u'particular', u'JJ')
8 (u',', u',')
9 (u'outlets', u'NNS')
True
10 (u'outlets', u'NNS')
11 (u'for', u'IN')
12 (u'political', u'JJ')
13 (u'involvement', u'NN')
14 (u'have', u'VBP')
15 (u'closed', u'VBN')
>>> tag_h
[(u'for', u'IN'), (u'young', u'JJ'), (u'citizens', u'NNS'), (u',', u','), (u'islamists', u'NNS'), (u',', u','), (u'in', u'IN'), (u'particular', u'JJ'), (u',', u','), (u'normal', u'JJ'), (u'outlets', u'NNS'), (u'for', u'IN'), (u'political', u'JJ'), (u'involvement', u'NN'), (u'have', u'VBP'), (u'closed', u'VBN'), (u'.', u'.')]
>>> f = open("/home/andrew/sp2015.11-731/hw3/output.txt")
>>> g = f.readlines()
>>> st = POSTagger("/home/andrew/Desktop/stanford-postagger-2014-08-27/models/english-bidirectional-distsim.tagger", "/home/andrew/Desktop/stanford-postagger-2014-08-27/stanford-postagger-3.4.1.jar", "UTF-8")
>>> h
'for citizens young , islamists , in particular , outlets normal for political involvement have closed .'
>>> st.tag(h)
[(u'f', u'LS'), (u'o', u'NN'), (u'r', u'NN'), (u'c', u'NN'), (u'i', u'LS'), (u't', u'NN'), (u'i', u'FW'), (u'z', u'SYM'), (u'e', u'LS'), (u'n', u'NN'), (u's', u'NN'), (u'y', u'NN'), (u'o', u'NN'), (u'u', u'NN'), (u'n', u'NN'), (u'g', u'NN'), (u',', u','), (u'i', u'FW'), (u's', u'VBZ'), (u'l', u'NN'), (u'a', u'DT'), (u'm', u'NN'), (u'i', u'FW'), (u's', u'NN'), (u't', u'NN'), (u's', u'NN'), (u',', u','), (u'i', u'FW'), (u'n', u'NN'), (u'p', u'NN'), (u'a', u'DT'), (u'r', u'NN'), (u't', u'NN'), (u'i', u'FW'), (u'c', u'NN'), (u'u', u'NN'), (u'l', u'NN'), (u'a', u'DT'), (u'r', u'NN'), (u',', u','), (u'o', u'NN'), (u'u', u'NN'), (u't', u'NN'), (u'l', u'NN'), (u'e', u'SYM'), (u't', u'NN'), (u's', u'NN'), (u'n', u'NN'), (u'o', u'NN'), (u'r', u'NN'), (u'm', u'NN'), (u'a', u'DT'), (u'l', u'NN'), (u'f', u'FW'), (u'o', u'NN'), (u'r', u'NN'), (u'p', u'NN'), (u'o', u'NN'), (u'l', u'NN'), (u'i', u'LS'), (u't', u'NN'), (u'i', u'LS'), (u'c', u'NN'), (u'a', u'DT'), (u'l', u'NN'), (u'i', u'FW'), (u'n', u'NN'), (u'v', u'LS'), (u'o', u'NN'), (u'l', u'NN'), (u'v', u'LS'), (u'e', u'LS'), (u'm', u'NN'), (u'e', u'SYM'), (u'n', u'NN'), (u't', u'NN'), (u'h', u'NN'), (u'a', u'DT'), (u'v', u'LS'), (u'e', u'LS'), (u'c', u'NN'), (u'l', u'NN'), (u'o', u'NN'), (u's', u'VBZ'), (u'e', u'LS'), (u'd', u'NN'), (u'.', u'.')]
>>> st.tag(h.split())
[(u'for', u'IN'), (u'citizens', u'NNS'), (u'young', u'JJ'), (u',', u','), (u'islamists', u'NNS'), (u',', u','), (u'in', u'IN'), (u'particular', u'JJ'), (u',', u','), (u'outlets', u'NNS'), (u'normal', u'JJ'), (u'for', u'IN'), (u'political', u'JJ'), (u'involvement', u'NN'), (u'have', u'VBP'), (u'closed', u'VBN'), (u'.', u'.')]
>>> sentence = "for citizens young , islamists , in particular , outlets normal for political involvement have closed . "
>>> final_form = []
>>> tokenized_sentence = word_tokenize(sentence)
>>> tag_sent = st.tag(tokenized_sentence)
>>> tag_sent
[(u'for', u'IN'), (u'citizens', u'NNS'), (u'young', u'JJ'), (u',', u','), (u'islamists', u'NNS'), (u',', u','), (u'in', u'IN'), (u'particular', u'JJ'), (u',', u','), (u'outlets', u'NNS'), (u'normal', u'JJ'), (u'for', u'IN'), (u'political', u'JJ'), (u'involvement', u'NN'), (u'have', u'VBP'), (u'closed', u'VBN'), (u'.', u'.')]
>>> for x in range(len(tag_sent)-1):
		if tag_sent[x][0] in nouns and tag_h[x+1][0] in adjectives:
			temp1 = tag_sent[x]
			temp2 = tag_sent[x+1]
			tag_sent[x] = temp2
			tag_sent[x+1] = temp1

			
>>> tag_sent
[(u'for', u'IN'), (u'citizens', u'NNS'), (u'young', u'JJ'), (u',', u','), (u'islamists', u'NNS'), (u',', u','), (u'in', u'IN'), (u'particular', u'JJ'), (u',', u','), (u'outlets', u'NNS'), (u'normal', u'JJ'), (u'for', u'IN'), (u'political', u'JJ'), (u'involvement', u'NN'), (u'have', u'VBP'), (u'closed', u'VBN'), (u'.', u'.')]
>>> st_span = POSTagger("/home/andrew/Desktop/stanford-postagger-full-2014-08-27/models/spanish.tagger", "/home/andrew/Desktop/stanford-postagger-2014-08-27/stanford-postagger-3.4.1.jar", "UTF-8")
>>> s = "para los ciudadanos jóvenes , los islamistas en particular , los canales normales de participación política se han cerrado ."
>>> s = word_tokenize(s)
>>> s
['para', 'los', 'ciudadanos', 'j\xc3\xb3venes', ',', 'los', 'islamistas', 'en', 'particular', ',', 'los', 'canales', 'normales', 'de', 'participaci\xc3\xb3n', 'pol\xc3\xadtica', 'se', 'han', 'cerrado', '.']
>>> st_span(s)

Traceback (most recent call last):
  File "<pyshell#179>", line 1, in <module>
    st_span(s)
TypeError: 'POSTagger' object is not callable
>>> ss = st_span.tag(s)
>>> ss
[(u'para', u'sp000'), (u'los', u'da0000'), (u'ciudadanos', u'nc0p000'), (u'j\xf3venes', u'aq0000'), (u',', u'fc'), (u'los', u'da0000'), (u'islamistas', u'nc0p000'), (u'en', u'sp000'), (u'particular', u'aq0000'), (u',', u'fc'), (u'los', u'da0000'), (u'canales', u'nc0p000'), (u'normales', u'aq0000'), (u'de', u'sp000'), (u'participaci\xf3n', u'nc0s000'), (u'pol\xedtica', u'aq0000'), (u'se', u'pp000000'), (u'han', u'vaip000'), (u'cerrado', u'vmp0000'), (u'.', u'fp')]
>>> pig = "APT_0001a_v_enus.wav"
>>> pig[5:8]
'001'
>>> 
