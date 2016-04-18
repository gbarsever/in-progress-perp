#!/usr/bin/python

from __future__ import division

import argparse
import numpy as np
import scipy
import math

from scipy.stats.distributions import entropy

#this just puts asl data into bhmml format

infile = open('0chunck_test_gold.txt','r')
readinfile = infile.readlines()
infile.close()

outfile = open('formatted_test_gold_sample0.txt','w')

for sent in readinfile:
	if sent != '\n':
		split_sent = sent.split()
		outfile.write('XXX\tXXX\txxx\nXXX\tXXX\txxx\n')
		for wordpair in split_sent:
			wordpairlist = wordpair.split('**')
			outfile.write('D\t'+wordpairlist[1]+'\t'+wordpairlist[0]+'\n')

outfile.close()