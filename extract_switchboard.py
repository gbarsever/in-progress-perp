#!/usr/bin/python

from collections import OrderedDict
import itertools
from math import log10
import numpy
import string as S
import re

#for all files in 

import os
outfile = open("test_switchboard_clean.txt", "w")
path1 = './switchboard_corpus/2'
path2 = './switchboard_corpus/3'
path3 = './switchboard_corpus/4'
listing1 = os.listdir(path1)
listing2 = os.listdir(path2)
listing3 = os.listdir(path3)
listings = [listing1, listing2, listing3]
count = 1
for list in listings:
	count +=1
	for file in list:
		print "current file is: " + file
		infile = open('./switchboard_corpus/'+str(count)+"/"+file, "r")
		readinfile = infile.read()
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
		#del y[0] # do this only after munged everything else

		for word in y:
			outfile.write(word+" ")
		outfile.write("\n")
		infile.close()
	print("all files in folder "+str(count)+" finished!")
outfile.close()

#still need to separate into 10/90 split and edit the size so that it's the same size as peter 1-12 (with a without after having got rid of the one word utterances)

infile = open("test_switchboard_clean.txt", "r")
readinfile = infile.read()

re.sub('[A-Z].+[a-z]', '\*\*', readinfile)
print(readinfile)
		

