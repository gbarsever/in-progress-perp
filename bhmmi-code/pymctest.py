from __future__ import division

from collections import OrderedDict
import itertools
import random
from math import log10
#from scipy import stats
#from scipy.stats import bernoulli
import numpy as np

'''       p *= (emissions[cTag][words.get(i)] + beta) /
                (computeSum(emissions, cTag) + beta * pWords.get(cTag).size());

        p *= (transitions[pTag][cTag] + alpha) /
                (computeSum(transitions, pTag) + alpha * nTags);

        p *= (transitions[cTag][fTag] + I1 + alpha) /
                (computeSum(transitions, cTag) + I2 + alpha * nTags);
'''


#first do dirichlet process on small section of the corpus
#test sequence I LIKE NICE DOGS

test_corpus = ['start!','I','LIKE','NICE','DOGS','end!']

#let's say i have initial categories
cat1 = ['I', 'LIKE']
cat2 = ['NICE']
cat3 = ['DOGS']
cats = [cat1, cat2, cat3]


#initialize probability with dirichlet (chinese restaurant process)

p = 1

#need to assign prob


for word in test_corpus:
	for x in range(0,len(cats)-1): #but the length will keep changing?
		if not cats[x]:
			x+=1
		if x < len(cats)-1:
			label = cats[x]
			next_label = cats[x+1]
		else:
			break
		if word in label:
			label.remove(word)
			next_label.append(word)
			#calculate probability
			       '''p *= (emissions[cTag][words.get(i)] + beta) /
                (computeSum(emissions, cTag) + beta * pWords.get(cTag).size());

        p *= (transitions[pTag][cTag] + alpha) /
                (computeSum(transitions, pTag) + alpha * nTags);

        p *= (transitions[cTag][fTag] + I1 + alpha) /
                (computeSum(transitions, cTag) + I2 + alpha * nTags);'''

			#bernoulli coinflip for if the word stays in label
			#pick random number
			#if number in distribution within probabilities, then assign that probability
			total_p = new_p + p
			rnum = random.uniform(0, total_p)
			#assigns new label (if success)
			#need to recalculate assigned prob
		
		
				
