#!/usr/bin/python

from collections import OrderedDict
import itertools
from math import log10
import numpy
import string as S
import re

infile = open("test_switchboard.txt", "r")

readinfile = infile.read()

# y = re.findall(


# readinfile.split()

new_corpus = []
d = re.compile('[A-Z]+\s.[a-z]+')
y = d.findall(readinfile)

iter = 0
for x in y:
	if y[iter] == 'SYM Speaker' and y[iter+1] == 'SYM Speaker':
		del y[iter]
	else:
		iter+= 1
	

for n,i in enumerate(y):
	if i=='SYM Speaker':
		y[n]="\n"
del y[0]
outfile = open("test_switchboard_clean.txt", "w")

for word in y:
	outfile.write(word+" ")
	
infile.close()
outfile.close()
	
