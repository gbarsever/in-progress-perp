#!/usr/bin/python

from collections import OrderedDict
import itertools
from math import log10
import numpy
import string as S
import re

infile = open("test_switchboard_clean.txt", "r")
readinfile = infile.readlines()

outfile = open("formatted_test_switchboard_clean.txt","w")

for sentence in readinfile:
	sent = sentence.split()
	words = [] #need to odd position
	tags = [] #need to be even position
	for thing in sent:
		if sent.index(thing) % 2 == 0:
			#put in tag list
			tags.append(thing)
		else:
			words.append(thing.lower())
	for x in range(0, len(words)):
		outfile.write(str(words[x])+"**"+str(tags[x])+ " ")
	outfile.write("\n")
			
