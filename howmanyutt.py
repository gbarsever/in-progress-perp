#!/usr/bin/python

from collections import OrderedDict
import itertools
from math import log10
import numpy
import string as S

infile = open("clean_adult_2016.txt", "r")

readinfile = infile.readlines()

print(len(readinfile))
# need to search for instances of lower case and then whatever is to the left after a white space