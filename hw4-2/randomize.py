import random
from random import sample

fo_NTtxt = open("data/train.input")
NTtxt = fo_NTtxt.readlines()

fo_NTtgvd = open("data/train.refs")
NTtgvd = fo_NTtgvd.readlines()



fo_NTtxt_tune = open("random.input", "w")


fo_NTtgvd_tune = open("random.refs", "w")



tune_set_lines = sample(xrange(len(NTtxt)), 5000)

for num in range(len(NTtxt)):
	if num in tune_set_lines:
		fo_NTtxt_tune.write(NTtxt[num])
		fo_NTtgvd_tune.write(NTtgvd[num])
