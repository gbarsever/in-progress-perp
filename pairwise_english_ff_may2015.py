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
#print(ff_FRAMES.keys())
print("# FF", len(ff_FRAMES.keys()))
infile.close()
#need to find/make file with all types with category

########################################################################
#sys.exit("stopping now")
########################################################################
#add coinflip for which ambiguous category?
#test lists for pairwise:
''' test case
list1 = ['a','b','c','1']
list2 = ['a','b','d','2']
list3 = ['a','c','d','3']

true_list1 = ['a','b','noun']
true_list2 = ['c','b','verb']
#itertools combinations combinations('ABCD', 2)

list_list = [list1, list2, list3]
list_true = [true_list1, true_list2]
'''

#pair_list = []
pair_dict_guess = OrderedDict()
#pair_true = []
pair_dict_true = OrderedDict()
#need to do frames? like to do frames and then turn them into lists with name of frame at end
#also need categories.  types!


#make pairs
#make over for dictionaries
for x in ff_FRAMES.keys():
	#name = x.pop() #keeps name so can keep track of which category is which
	pairx = list(combinations(ff_FRAMES[x],2))
	#pairx.append(name)
	pair_dict_guess[x] = pairx
	
for y in type_dict.keys():
	#name = y.pop()
	pairy = list(combinations(type_dict[y],2))
	#pairy.append(name)
	pair_dict_true[y] = pairy

outfile = open('pairwise_test_may5_2015_nobound.txt','w')
prec = []
rec = []
#len(set(A).intersection(B))
for sec in pair_dict_guess.keys():
	sec_name = sec
	true_cat = []
	count = 0
	for true in pair_dict_true.keys():
		true_name = true
		new = len(set(pair_dict_guess[sec]).intersection(pair_dict_true[true]))
		if new > count:
			count = new
			true_cat = pair_dict_true[true]
			#true.append(true_name)
	outfile.write(str(sec_name)+ " & ")
	outfile.write(str(true_name)+ "  ")
	intersec = set(pair_dict_guess[sec]).intersection(true_cat)
	if len(intersec) != 0:
		recall = float(len(intersec))/float(len(true_cat))
		precision = float(len(intersec))/float(len(pair_dict_guess[sec]))
		prec.append(precision)
		rec.append(recall)
		outfile.write("\n\trecall: ")
		outfile.write(str(recall)+"\t")
		outfile.write("precision: ")
		outfile.write(str(precision)+"\n")
	else:
		outfile.write("no intersection\n")
av_prec = sum(prec)/len(prec)
av_rec = sum(rec)/len(rec)

print("average precision", av_prec)
print("average recall", av_rec)
outfile.write("\n************\nav precision: "+str(av_prec)+"\tav:recall: "+str(av_rec))
outfile.close()




