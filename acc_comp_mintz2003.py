#!/usr/bin/python

from collections import OrderedDict
import itertools
from math import log10

#accuracy and completeness (a la mintz 2003) both type and token

#accuracy = hits/(hits + false alarms)
#completeness = hits/(hits + misses)
#take pairs

#hits = the pair is from the same true category
#false alarm = two items were in different categories

# Misses are computed by comparing all possible pairs of word tokens that were 
# categorized. A pair is counted as a Miss if the members belong to the same 
# grammatical category but were not categorized together by the analysis
#so a miss would be: after taking away all the words from the results, what is left in the list that is true


true_1 = ["b","a","c"] #pairs = ba bc ac
#true_2 = ["d","f","s"]

#make pairs and add to giant list (only within categories can be pair anyway_

trues = list(itertools.combinations(true_1,2))
print(trues)

thing = ["a","b","c","d"] #pairs = ab ac ad bc bd cd
#thang = ["a","f","c","s"]
#things = [thing, thang]
#(A)

new_thing = list(itertools.combinations(thing,2))
print(new_thing)

for pair in new_thing:
	#print(set(pair))
	for true_pair in trues:
		if set(pair) == set(true_pair):
			print("yay")
#FIX ORDER-make pairs match even if they are a,b vs b,a

#firstly, for regular accuracy, dont need to know which category they match do
#at the end, do seperately with verbs just to see



