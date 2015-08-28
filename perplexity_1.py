#!/usr/bin/python

from collections import OrderedDict
import itertools
from math import log10
import numpy


#new improved perplexity code!
#perplexity(w1-w2-w3) = Nthroot(1/P(start-w1-w2-w3-end))
#n does not include start and end
# 
# P(start-w1...n-end) = p(g1|start) * p(w1|g1)
# * p(g2|g1) * p(w2|g2)
# * p(g3|g2) * p(w3|g3)
# *	...
# *	p(gn|gn-1) * p(wn|gn)
# *	p(end|gn)

#start by inputting files (format could be in stella's code)

#should make table of all probabilities in training set.

## need: container for grammatical categories and the words they belong to
## then: need to have table where can look up the transitional probability between categories

#eventually get list of lists [['noun, 'cat','dog'],['verb','go']...etc...

#then need order of categories.  read in single column so ['start!','noun','verb','det'...]

for word in sentence:
	if 


