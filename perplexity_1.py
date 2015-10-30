#!/usr/bin/python

from collections import OrderedDict
import itertools
from math import log10
import numpy

#
##
#make a separate thing for types, this is tokens (add parameter?)
##
#
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

#have an input parameter about whether unknown words exist in individual or glom category

# how to make this command paramter??? 
glom_or_in = raw_input("all unknown words in test set in indiviudal categories or one glommed one? type \"i\" for indiviudal and \"g\" for glommed\n")
#glom_or_in = "i" #just for testing


train_corpus = ["start!*start! i*n really*av love*v cute*a cats*n end!*end!", "start!*start! i*n love*v cute*a dogs*n end!*end!"]
test_corpus = ["start!*start! i*n like*v cute*a birds*n end!*end!", "start!*start! go*v end!*end!"]
ff_train_corpus = ["start! i love cute cats end!", "start! i love cute dogs end!"]
ff_test_cropus = ["start! i like cute birds end!", "start! go end!"]

train_dict = {}
ff_train_dict = {}

for sentence in train_corpus: #building the dictionary(ies) for training corpora
	sent = sentence.split()
	for word_cat in sent[0:len(sent)-1]: #ignore end
		temp = word_cat.split("*")
		if temp[1] not in train_dict.keys():
			train_dict[temp[1]] = [temp[0]]
		else:
			temp_list = train_dict[temp[1]]
			temp_list.append(temp[0])
			train_dict[temp[1]] = temp_list
			
cat_list = train_dict.keys()
word_list_train = []
word_list_test = []

for sent in test_corpus:
	sent_s = sent.split()
	for word_thing in sent_s:
		word_thing_s = word_thing.split("*")
		if word_thing_s[0] != "start!" and word_thing_s[0] != "end!":
			word_list_test.append(word_thing_s[0])

trans_cat_table = {}
for sent in train_corpus:
	sent_s = sent.split()
	for word_thing in sent_s:
		word_thing_s = word_thing.split("*")
		if word_thing_s[0] != "start!" and word_thing_s[0] != "end!":
			word_list_train.append(word_thing_s[0])
	for word_num in range(len(sent_s)-1):
		word = sent_s[word_num]
		both_word = word.split("*")
		next_word = sent_s[word_num+1]
		both_next_word = next_word.split("*")
		new_key = both_word[1]+'$'+both_next_word[1]
		if new_key not in trans_cat_table.keys():
			trans_cat_table[new_key] = 1
		else:
			temp = trans_cat_table[new_key] 
			temp +=1
			trans_cat_table[new_key] = temp
			#figure out something here for how to get frequency of "starts"

word_difference = [item for item in word_list_test if item not in word_list_train]
train_dict['glom'] = word_difference



#~*~*~*~*~*~*~*~*~*~* for FF

for sentence in ff_train_corpus: #building the dictionary(ies) for training corpora
	sent = sentence.split()
	for num in range(len(sent)-3): #dont ignore start and end
		new_key = sent[num]+"__"+sent[num+2]  #DOUBLE UNDERSCORE!!!
		if new_key not in ff_train_dict.keys():
			ff_train_dict[new_key] = [sent[num+1]]
		else:
			temp_list = ff_train_dict[new_key]
			temp_list.append(sent[num+1])
			ff_train_dict[new_key] = temp_list
			
print ff_train_dict

ff_word_list_train = []
ff_word_list_test = []

for sent in ff_test_corpus:
	sent_s = sent.split()
	for word_thing in sent_s:
		word_thing_s = word_thing.split("*")
		if word_thing_s[0] != "start!" and word_thing_s[0] != "end!":
			ff_word_list_test.append(word_thing_s[0])

ff_trans_cat_table = {}
for sent in train_corpus:
	sent_s = sent.split()
	for word_thing in sent_s:
		word_thing_s = word_thing.split("*")
		if word_thing_s[0] != "start!" and word_thing_s[0] != "end!":
			word_list_train.append(word_thing_s[0])
	for word_num in range(len(sent_s)-1):
		word = sent_s[word_num]
		both_word = word.split("*")
		next_word = sent_s[word_num+1]
		both_next_word = next_word.split("*")
		new_key = both_word[1]+'$'+both_next_word[1]
		if new_key not in trans_cat_table.keys():
			trans_cat_table[new_key] = 1
		else:
			temp = trans_cat_table[new_key] 
			temp +=1
			trans_cat_table[new_key] = temp
			#figure out something here for how to get frequency of "starts"

word_difference = [item for item in word_list_test if item not in word_list_train]
train_dict['glom'] = word_difference

#~!~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~	
ff_trans_cat_table = {}
for sent in ff_train_corpus:
	sent_s = sent.split()
	for word_thing in sent_s:
		word_thing_s = word_thing.split("*")
		if word_thing_s[0] != "start!" and word_thing_s[0] != "end!":
			word_list_train.append(word_thing_s[0])
	for word_num in range(len(sent_s)-1):
		word = sent_s[word_num]
		both_word = word.split("*")
		next_word = sent_s[word_num+1]
		both_next_word = next_word.split("*")
		new_key = both_word[1]+'$'+both_next_word[1]
		print new_key
		if new_key not in trans_cat_table.keys():
			trans_cat_table[new_key] = 1
		else:
			temp = trans_cat_table[new_key] 
			temp +=1
			trans_cat_table[new_key] = temp
# 					
# print(trans_cat_table) #will need to divide by how much you see first category
			
ff_list = ff_train_dict.keys()	

#perplexity(w1-w2-w3) = Nthroot(1/P(start-w1-w2-w3-end))
#n does not include start and end
# 
# P(start-w1...n-end) = p(g1|start) * p(w1|g1)
# * p(g2|g1) * p(w2|g2)
# * p(g3|g2) * p(w3|g3)
# *	...
# *	p(gn|gn-1) * p(wn|gn)
# *	p(end|gn)

#gold:



def prob_utterance(k):
	'''calculates the probability of a sentence minus the end part given a sentence'''
	g = k.split()
	minus_end = 1
	for x in range(1,len(g)-1):
		word_split = g[x].split("*")
		print(word_split)
		word_split2 = g[x-1].split("*") #previous Gn
		print(word_split2)
		trans_key =  word_split2[1]+'$'+word_split[1]
		if trans_key in trans_cat_table.keys():
			trans_val = trans_cat_table[trans_key] + 0.5
		else:
			trans_val = 0.5
		if word_split2[1] in train_dict.keys():
			num_previous_cat = len(train_dict[word_split2[1]])+0.5
		else:
			num_previous_cat = 0.5
		p_trans_temp = trans_val/num_previous_cat
		if word_split[1] in train_dict.keys():
			p_emiss = (train_dict[word_split[1]].count(word_split[0]) + 0.5)/(len(train_dict[word_split[1]])+0.5)
		else:
			if glom_or_in == 'i':
				p_emiss = 0.5/0.5 #b/c the prob is gonna be 1/1 for every tiny category
			else:
				p_emiss = (train_dict['glom'].count(word_split[0]) + 0.5)/(len(train_dict['glom'])+0.5) #SOMETHING WEIRD HERE!!!!
		print(minus_end,p_trans_temp,p_emiss)
		minus_end = minus_end * p_trans_temp * p_emiss
	return log10(minus_end)
	
def ends_of_utterance(j):
	'''calculates the probability of the end part of the sentence'''
	g = j.split()
	ends = 1
	word_split = g[-1].split("*")
	word_split2 = g[-2].split("*") #previous Gn
	trans_key =  word_split2[1]+'$'+word_split[1]
	if trans_key in trans_cat_table.keys():
		trans_val = trans_cat_table[trans_key] + 0.5
	else:
		trans_val = 0.5
	if word_split2[1] in train_dict.keys():
		num_previous_cat = len(train_dict[word_split2[1]])+0.5
	else:
		num_previous_cat = 0.5
	ends = trans_val/num_previous_cat
	return log10(ends)

def calculate_perplexity(t_c):
	'''calculates total probability of corpus using logs (and then taking them out)'''
	sentence_prob = 0
	test_perplex = 0
	for sent in test_corpus:
		sentence_prob = sentence_prob + prob_utterance(sent) + ends_of_utterance(sent)
		test_perplex += perplexity(sent, sentence_prob)
	corpus_perplexity = test_perplex/len(test_corpus)
	return corpus_perplexity
	
def perplexity(s, total_prob):
	'''calculates the perplexity of an utterance given the probability and sentence (for length)'''
	count = 0
	perplex = 0
	predone = 0
	count = len(s)-2 #not counting start and end
	predone = (-1/count)*total_prob
	perplex = 10**(predone)
	return perplex

print(calculate_perplexity(test_corpus))	



		
		
		
	 


