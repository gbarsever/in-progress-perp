#!/usr/bin/python

from collections import OrderedDict
import itertools
from math import log10
import numpy
import string as S

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

frame_or_no = raw_input("do you want to determine perplexity over frames or categories?\nFor frames enter f, for categories enter c:\n")
for file_num in range(0,10,1):
	if frame_or_no == "f":
		infile1 = open('./input_corpora/'+str(file_num)+'chunck_train_ff_engNEW.txt','r')
		infile2 = open('./input_corpora/'+str(file_num)+'chunck_test_ff_engNEW.txt','r')#
		#infile1 = open('clean_corpus.txt','r')
		readinfile1 = infile1.readlines()
		readinfile2 = infile2.readlines()
		infile1.close()
		infile2.close()
		test_cats = []
		
		ff_train_corpus = []
		for a_thing in readinfile1:
			if a_thing != '\n':
				new_a_string = "start! "+S.rstrip(a_thing)+" end!"
				ff_train_corpus.append(new_a_string.split())

		ff_test_corpus = []
		for c_thing in readinfile2:
			if c_thing != '\n':
				new_c_string = "start! "+S.rstrip(c_thing)+" end!"
				ff_test_corpus.append(new_c_string.split())
	#~*~*~*~*~*~*~*~*~*~* for FF
		ff_train_dict = {}
		new_ff_train = []
		for sentence in ff_train_corpus: #building the dictionary(ies) for training corpora
			new_ff_train_sentence = "start!**start!"
			for num in range(len(sentence)-2): #dont ignore start and end
				new_key = sentence[num]+"__"+sentence[num+2]  #DOUBLE UNDERSCORE!!!
				new_ff_train_sentence += " "+ sentence[num+1] + "**" + new_key +" "
				if new_key not in ff_train_dict.keys():
					ff_train_dict[new_key] = [sentence[num+1]]
				else:
					temp_list = ff_train_dict[new_key]
					temp_list.append(sentence[num+1])
					ff_train_dict[new_key] = temp_list
			new_ff_train_sentence += "end!**end!"
			new_ff_train.append(new_ff_train_sentence)


		new_ff_test = []
		for sentence in ff_test_corpus: 
			new_ff_test_sentence = "start!**start!"
			for num in range(len(sentence)-2): #dont ignore start and end
				new_key = sentence[num]+"__"+sentence[num+2]  #DOUBLE UNDERSCORE!!!
				new_ff_test_sentence += " "+ sentence[num+1] + "**" + new_key +" "
			new_ff_test_sentence += "end!**end!"
			new_ff_test.append(new_ff_test_sentence)


		ff_word_list_train = []
		ff_word_list_test = []

		for sent in ff_test_corpus:
			for word_thing in sent:
				word_thing_s = word_thing.split("*")
				if word_thing_s[0] != "start!" and word_thing_s[0] != "end!":
					ff_word_list_test.append(word_thing_s[0])

		ff_trans_cat_table = {}
		#preprocess!  turn into thing that looks like the english (and then do same thing to test)

		for sent in new_ff_train:
			sent_s = sent.split()
			for word_thing in sent_s:
				word_thing_s = word_thing.split("**")
				if word_thing_s[0] != "start!" and word_thing_s[0] != "end!":
					ff_word_list_train.append(word_thing_s[0])
			for word_num in range(len(sent_s)-1):
				word = sent_s[word_num]
				both_word = word.split("**")
				next_word = sent_s[word_num+1]
				both_next_word = next_word.split("**")
				new_key = both_word[1]+'$'+both_next_word[1]
				if new_key not in ff_trans_cat_table.keys():
					ff_trans_cat_table[new_key] = 1
				else:
					temp = ff_trans_cat_table[new_key] 
					temp +=1
					ff_trans_cat_table[new_key] = temp
					#figure out something here for how to get frequency of "starts"

		ff_word_difference = [item for item in ff_word_list_test if item not in ff_word_list_train]
		ff_train_dict['glom'] = ff_word_difference
		
		#now making it frequent, needs to have .5% of types and .1% of tokens
		new_ff_train_dict = {}
		for thing in ff_train_dict.keys():
			if len(set(ff_train_dict[thing])) >= (.005)*len(set(ff_word_list_train)) and len(ff_train_dict[thing]) >= (.001)*len(ff_word_list_train) and len(set(ff_train_dict[thing])) > 2:
				new_ff_train_dict[thing] = ff_train_dict[thing]
		
		#print(len(new_ff_train_dict.keys()))
		
		#break
			
		ff_list = ff_train_dict.keys()	

		#~!~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~	


	elif frame_or_no == "c":
		infile1 = open('./input_corpora/'+str(file_num)+'chunck_train_gold_engNEW.txt','r')
		infile2 = open('./input_corpora/'+str(file_num)+'chunck_test_gold_engNEW.txt','r')#
		readinfile1 = infile1.readlines()
		readinfile2 = infile2.readlines()
		infile1.close()
		infile2.close()
		train_corpus = []
		for a_thing in readinfile1:
			if a_thing != '\n':
				new_a_string = "start!**start! "+S.rstrip(a_thing)+" end!**end!"
				train_corpus.append(new_a_string)

		test_corpus = []
		for c_thing in readinfile2:
			if c_thing != '\n':
				new_c_string = "start!**start! "+S.rstrip(c_thing)+" end!**end!"
				test_corpus.append(new_c_string)
			
		train_dict = {}
		for sentence in train_corpus: #building the dictionary(ies) for training corpora
			sent = sentence.split()
			for word_cat in sent[0:len(sent)-1]: #ignore end
				temp = word_cat.split("**")
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
				word_thing_s = word_thing.split("**")
				if word_thing_s[0] != "start!" and word_thing_s[0] != "end!":
					word_list_test.append(word_thing_s[0])

		trans_cat_table = {}
		for sent in train_corpus:
			sent_s = sent.split()
			for word_thing in sent_s:
				word_thing_s = word_thing.split("**")
				if word_thing_s[0] != "start!" and word_thing_s[0] != "end!":
					word_list_train.append(word_thing_s[0])
			for word_num in range(len(sent_s)-1):
				word = sent_s[word_num]
				both_word = word.split("**")
				next_word = sent_s[word_num+1]
				both_next_word = next_word.split("**")
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
	else:
		print("you entered something weird.  boo.\n")
		break


	#should make table of all probabilities in training set.

	## need: container for grammatical categories and the words they belong to
	## then: need to have table where can look up the transitional probability between categories

	#eventually get list of lists [['noun, 'cat','dog'],['verb','go']...etc...

	#then need order of categories.  read in single column so ['start!','noun','verb','det'...]

	#have an input parameter about whether unknown words exist in individual or glom category

	# how to make this command parameter??? 



	# train_corpus = ["start!*start! i*n really*av love*v cute*a cats*n end!*end!", "start!*start! i*n love*v cute*a dogs*n end!*end!", "start!*start! fly*v end!*end!"]
	# test_corpus = ["start!*start! i*n like*v cute*a birds*n end!*end!", "start!*start! go*v end!*end!"]
	# ff_train_corpus = ["start! i love cute cats end!", "start! i love cute dogs end!", "start! fly end!"]
	# ff_test_corpus = ["start! i like cute birds end!", "start! go end!"]





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



	def prob_utterance(k,tab, l):
		'''calculates the probability of a sentence minus the end part given a sentence'''
		g = k.split()
		minus_end = 1
		for x in range(1,len(g)-1):
			word_split = g[x].split("**")
			word_split2 = g[x-1].split("**") #previous Gn
			trans_key =  word_split2[1]+'$'+word_split[1]
			if trans_key in tab.keys() and word_split2[1] in l.keys():
				trans_val = tab[trans_key] + 0.5
				num_previous_cat = len(l[word_split2[1]])+0.5
			else:
				trans_val = 0.5
				num_previous_cat = 0.5
			p_trans_temp = trans_val/num_previous_cat
			if word_split[1] in l.keys():
				p_emiss = (l[word_split[1]].count(word_split[0]) + 0.5)/(len(l[word_split[1]])+0.5)
			else:
				p_emiss = 0.5/0.5 #b/c the prob is gonna be 1/1 for every tiny category
			minus_end = minus_end * p_trans_temp * p_emiss
		return log10(minus_end)
	
	def ends_of_utterance(j,tab,l):
		'''calculates the probability of the end part of the sentence'''
		g = j.split()
		ends = 1
		word_split = g[-1].split("**")
		word_split2 = g[-2].split("**") #previous Gn
		trans_key =  word_split2[1]+'$'+word_split[1]
		if trans_key in tab.keys():
			trans_val = tab[trans_key] + 0.5
		else:
			trans_val = 0.5
		if word_split2[1] in l.keys():
			num_previous_cat = len(l[word_split2[1]])+0.5
		else:
			num_previous_cat = 0.5
		ends = trans_val/num_previous_cat
		return log10(ends)

	def calculate_perplexity(t_c,table,tab_list):
		'''calculates total probability of corpus using logs (and then taking them out)'''
		init_prob = 0
		test_perplex = 0
		for sent in t_c:
			sentence_prob = 0
			sentence_prob = prob_utterance(sent, table, tab_list) + ends_of_utterance(sent,table,tab_list)
			test_perplex += perplexity(sent, sentence_prob)
		corpus_perplexity = test_perplex/len(t_c)
		return corpus_perplexity
	
	def perplexity(s, total_prob):
		'''calculates the perplexity of an utterance given the probability and sentence (for length)'''
		count = 0
		perplex = 0
		predone = 0
		count = len(s)-2 #not counting start and end
		predone = (-1/count)*total_prob
		perplex = numpy.power(10,predone)
		return perplex

	
	
	if frame_or_no == "f":
		print(calculate_perplexity(new_ff_test, ff_trans_cat_table, ff_train_dict))
	elif frame_or_no == "c":
		print(calculate_perplexity(test_corpus, trans_cat_table, train_dict)) #needs test corpus, trans_cat_table, and train_dict	


		
		
	 


