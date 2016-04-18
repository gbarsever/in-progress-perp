#!/usr/bin/python

from collections import OrderedDict
import itertools
from math import log10
import re

infile = open('formatted_test_switchboard_clean.txt', "r")
readinfile = infile.readlines()


#new chunks!

utterance_mega_list = []#for english!
for line in readinfile:
    utterance_mega_list.append(line.split())

x = utterance_mega_list

#90/10, still need to see if need to make catch all category if basing frames off training only
avg = len(x)/float(10)
out = []
last = 0.0
combined = 0
clean_list = []
while last< len(x):
    out.append(x[int(last):int(last + avg)])
    last += avg
for y in range(10):
    test_list = out.pop(y)
    for ele in out:
        for thing in ele:
            clean_list.append(thing)
    out.insert(y,test_list)
    outfile1 = open(str(y)+'chunck_train_gold_adultNEW.txt', 'w')
    outfile2 = open(str(y)+'chunck_test_gold_adultNEW.txt','w')
    for n in clean_list:
        for z in n:
            outfile1.write(z)
            outfile1.write(' ')
        outfile1.write('\n')
    for j in test_list:
        for o in j:
            outfile2.write(o)
            outfile2.write(' ')
        outfile2.write('\n')

    clean_list = []