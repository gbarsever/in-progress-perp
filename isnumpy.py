from collections import OrderedDict
from itertools import *
from math import log10
import scipy as sp
import numpy as np
import sys

#english:
#eng_ff_chunks.txt -for FF child directed
#clean_adult_end_ff_NEW.txt -for FF adult directed
#better_tokens_eng.txt -for cats child directed
#better_tokens_adult.txt -for cats adult direction

token_file = raw_input("enter filename for tokens (child or adult)\n")
ff_file = raw_input("enter filename for frequent frames\n")

infile_token = open(token_file, 'r')
infile = open(ff_file, 'r')

readinfileyay = infile_token.read()
split_file = readinfileyay.split()
word_set = set(split_file)
infile_token.close()

for_lists = infile.read()
infile.close()
token_list = for_lists.split()
type_list = set(token_list)

type_dict = OrderedDict()

for x in word_set:
	word_val = x.split("**")
	list_cat = []
	if word_val[1] not in type_dict:
		list_cat.append(word_val[0].rstrip())
		type_dict[word_val[1]] = list_cat
	else:
		add_cat = type_dict[word_val[1]]
		add_cat.append(word_val[0].rstrip())
		type_dict[word_val[1]] = add_cat
for thing in type_dict:
	make_types = set(type_dict[thing])
	type_dict[thing] = make_types
	
print(type_dict)


'''
for x in word_set:
	word_val = x.split("**")
	list_cat = []
	if word_val[0] not in type_dict:
		list_cat.append(word_val[1].rstrip())
		type_dict[word_val[0]] = list_cat
	else:
		add_cat = type_dict[word_val[0]]
		add_cat.append(word_val[1].rstrip())
		type_dict[word_val[0]] = add_cat
'''
readinfile1 = for_lists.splitlines()


for_frames_list= []
for a_thing in readinfile1:
	if a_thing != '\n':
		new_a_string = "start! "+a_thing+" end!"
		for_frames_list.append(new_a_string.split())


print("making frames")
#Mintz 2003 did NOT use utterance boundaries!! most of our frequent frames use utterance boundaries
FRAMES = OrderedDict() #gets dictionary of frames, keys being frames values are words in frames
#NEEDS TO BE TYPES!!!  categories are with types!!!
group_list = []
for split_line in for_frames_list:
	for y in range(len(split_line)):
		group = []
		if (y+2) < len(split_line):
			key_thing = str(split_line[y]+' '+split_line[y+2])
			if key_thing not in FRAMES:
				group.append(split_line[y+1])
				FRAMES[key_thing] = group
			elif key_thing in FRAMES:
				new_val = []
				if split_line[y+1] not in FRAMES.get(key_thing):
					new_val.extend(FRAMES.get(key_thing))
					new_val.append(split_line[y+1])
					FRAMES[key_thing] = new_val
					

ff_FRAMES = OrderedDict()
# token_set = set(train_tokens)
# make_freq = []

#now making it frequent, needs to have .5% of types and .1% of tokens
for ff_frame in FRAMES:
	if len(set(FRAMES[ff_frame]))>=(.005*len(type_list)) and len(FRAMES[ff_frame]) >=(.001*len(token_list)):
		ff_FRAMES[ff_frame] = FRAMES[ff_frame]
#for ff_thing in ff_FRAMES.keys():
print(ff_FRAMES.keys())
infile.close()
#need to find/make file with all types with category

########################################################################
sys.exit("stopping now")
########################################################################
#add coinflip for which ambiguous category?
#test lists for pairwise:

list1 = ['a','b','c','1']
list2 = ['a','b','d','2']
list3 = ['a','c','d','3']

true_list1 = ['a','b','noun']
true_list2 = ['c','b','verb']
#itertools combinations combinations('ABCD', 2)

list_list = [list1, list2, list3]
list_true = [true_list1, true_list2]

pair_list = []
pair_true = []
#need to do frames? like to do frames and then turn them into lists with name of frame at end
#also need categories.  types!


#make pairs
for x in list_list:
	name = x.pop() #keeps name so can keep track of which category is which
	pairx = list(combinations(x,2))
	pairx.append(name)
	pair_list.append(pairx)
	
for y in list_true:
	name = y.pop()
	pairy = list(combinations(y,2))
	pairy.append(name)
	pair_true.append(pairy)

outfile = open('pairwise_test_may5_2015.txt','w')

#len(set(A).intersection(B))
for sec in pair_list:
	sec_name = sec.pop()
	true_cat = []
	count = 0
	for true in pair_true:
		true_name = true.pop()
		new = len(set(sec).intersection(true))
		if new > count:
			count = new
			true_cat = true
			true.append(true_name)
		else:
			true.append(true_name)
	outfile.write(str(sec_name)+ " & ")
	outfile.write(str(true_name)+ "  ")
	intersec = set(sec).intersection(true_cat)
	if len(intersec) != 0:
		recall = float(len(intersec))/float(len(true_cat))
		precision = float(len(intersec))/float(len(sec))
		outfile.write("\n\trecall: ")
		outfile.write(str(recall)+"\t")
		outfile.write("precision: ")
		outfile.write(str(precision)+"\n")
		sec.append(sec_name)
	else:
		outfile.write("no intersection\n")
		sec.append(sec_name)
	
outfile.close()




