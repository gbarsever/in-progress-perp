#!/usr/bin/python

from collections import OrderedDict
import itertools
from math import log10



frame_or_no = input("do you want to determine perplexity over frames or categories?\nFor frames enter f, for categories enter c:\n")
for file_num in range(0,10,1):
	if frame_or_no == "f":
		infile1 = open('./input_corpora/'+str(file_num)+'chunck_train_ff_engNEW.txt','r')
		infile2 = open('./input_corpora/'+str(file_num)+'chunck_test_ff_engNEW.txt','r')#
		readinfile1 = infile1.readlines()
		readinfile2 = infile2.readlines()
		infile1.close()
		infile2.close()
		test_cats = []
	elif frame_or_no == "c":
		infile1 = open(str(file_num)+'chunck_train_gold_engNEW.txt','r')
		infile2 = open(str(file_num)+'chunck_test_gold_engNEW.txt','r')#
		readinfile1 = infile1.readlines()
		readinfile2 = infile2.readlines()
		infile1.close()
		infile2.close()
	else:
		print("you entered something weird.  boo.\n")
		break



	train_utt_list = []
	for_frames_list_a = []
	for_cat_list_a = []
	for a_thing in readinfile1:
		if a_thing != '\n':
			train_utt_list.append(a_thing.split())
			new_a_string = "start! "+a_thing+" end!"
			for_frames_list_a.append(new_a_string.split())
			for_cat_list_a.append(new_a_string.split())

	test_utt_list = []		
	for_frames_list_c = []
	for_cat_list_c = []
	for c_thing in readinfile2:
		if c_thing != '\n':
			test_utt_list.append(c_thing.split())
			new_c_string = "start! "+c_thing+" end!"
			for_frames_list_c.append(new_c_string.split())
			for_cat_list_c.append(new_c_string.split())



	train_tokens = []
	train_utt_list_set = set()
	for sent in train_utt_list:
		for thing in sent:
			train_tokens.append(thing)
			train_utt_list_set.add(thing)
	train_utt_list_words = list(train_utt_list_set)



	test_utt_list_set = set()
	for sent in test_utt_list:
		for thing in sent:
			test_utt_list_set.add(thing)
	test_utt_list_words = list(test_utt_list_set)



	mega_set = set()

	mega_list = []
	for x in test_utt_list_words:
		mega_set.add(x)
	for x in train_utt_list_words:
		mega_set.add(x)

	mega_list = list(mega_set)



	FRAMES = OrderedDict() #gets dictionary of frames, keys being frames values are words in frames
	#DONT FORGET TO MAKE START AND END FRAMING ELEMENTS

	group_list = []
	for split_line in for_frames_list_a:#uses tokens
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
	token_set = set(train_tokens)
	make_freq = []
	#now making it frequent, needs to have .5% of types and .1% of tokens
	for ff_frame in FRAMES:
		if len(set(FRAMES[ff_frame]))>=(.005*len(train_utt_list_set)) and len(FRAMES[ff_frame]) >=(.001*len(train_tokens)):
			ff_FRAMES[ff_frame] = FRAMES[ff_frame]
	#for ff_thing in ff_FRAMES.keys():
		#print(ff_thing)
	
#~*~*~*~*~*~*~~*~*
#*~*~*~*~*~*~*~*~okay this is to get the categories from an output file 
	if frame_or_no =="c":
		#all in one category
		test_cats = []
		for test_sent in test_utt_list:
			for pair in test_sent:
				word = pair.split("**")
				if word[1] not in test_cats:
					test_cats.append(word[1])
		for train_sent in train_utt_list:
			for pair in train_sent:
				word = pair.split("**")
				cat_dict['one_cat'] = [str(word[0]).rstrip()]
				checklist.append(pair)					
		
	'''
		infile_cats = open("collapsed_cats.txt", "r")
		readinfile_cats = infile_cats.readlines()
		infile_cats.close()
		from_file_list = []
		test_cats = []
		for file_cat in readinfile_cats:
			if file_cat != "\n":
				from_file_list.append(file_cat.rstrip())
		cat_dict = OrderedDict()
		checklist = []
		for test_sent in test_utt_list:
			for pair in test_sent:
				word = pair.split("**")
				if word[1] not in test_cats:
					test_cats.append(word[1])
		for train_sent in train_utt_list:
			for pair in train_sent:
				word = pair.split("**")
				for cat_thing in from_file_list:
					if str(cat_thing) == str(word[1]).rstrip():
						working_list = []
						if str(cat_thing) in cat_dict.keys():
							working_list = cat_dict[str(cat_thing)]
							working_list.append(str(word[0]).rstrip())
							cat_dict[str(cat_thing)] = working_list
						else:
							cat_dict[str(cat_thing)] = [str(word[0]).rstrip()]
				checklist.append(pair)
		print("num of categories", len(cat_dict.keys()))
		for element in cat_dict.keys():
			print(element, len(cat_dict[element]))
		#break	
		'''

	#some words are at the beginning or the end so they are not taken in between framing elements
	#print(test_cats)

	
	#make probabilities table/dictionary to grab from before.  okay so go thru 
	
	prob_dict_first = {}
	prob_dict_last = {}
	prob_dict_mid = {}#may only need one with key cat1_cat2
	#
	count = 0
	count_l = 0
	ends = 0
	for category in test_cats:#MAKE TEST CATS!!!!!!!!!!!!!!!!!!
		for sentence in for_cat_list_a:
			sent_cat_f = sentence[1].split("**")
			if category == sent_cat_f[1]:#start-word(['category
				count +=1
			else:
				count = 0
			sent_cat_l = sentence[-2].split("**")
			for pos in range(1,len(sentence)-1,1):
				word_plus_cat_end2 = sentence[pos].split("**")
				if word_plus_cat_end2[1] == category:
					count_l +=1
			if sent_cat_l[1] == category:
				ends +=1##
		#print("ok!", category)
		prob_dict_last[category] = ((count_l +.5)/(ends+.5))	
		prob_dict_first[category] = count
#only need to do middle parts (should still check if words are in training if not in test)
	new_count = 0
	other_count = 0
	for one_category in test_cats:
		for other_category in test_cats:
			for sentence in for_cat_list_a:
				for x in range(1, len(sentence)-2,1):
					word_plus_cat = sentence[x].split("**")
					word_plus_cat_other = sentence[x+1].split("**")
				for pos in range(1,len(sentence)-1,1):
					any_word_cat = sentence[pos].split("**")
					if any_word_cat[1] == one_category:
						other_count += 1
				if one_category == word_plus_cat[1] and other_category == word_plus_cat_other[1]:
					new_count += 1
					name = str(one_category)+"_"+str(other_category)
					if name not in prob_dict_mid.keys():
						prob_dict_mid[name] = (new_count+.5)/(other_count+.5)
						#print("okay!, middle!", name)
		
	

	#for each utterance, do test training, how many frame options how many utterances, what is the combinations required
	#get perplexity for each utternance (in test set), and then average them
	#for utterance!	 find out how many combinations could there be in utterance, can give a mean and stdev
	#list out all the possible strategies, (cartesian, select them at frequency based one, coherent category (hand shape v movement) (or phonemes, framing unit that are smaller than whole sign)
	#stop!! no more average!  go back to doing entire test set
	print("omgosh now the fun stuff is starting!")

	#cat_dict_TEST = {"PN":["GALIA"],"V":["HATE", "HEAT", "GO", "PLAY", "LOVE"], "N":["POPCORN", "DOG"] }
	def perplexity(n,x):
		'''returns perplexity from probability, n needs to include starts and stops'''
		count = 0
		perplex = 0
		predone = 0
		count+= len(n)
		count = count-2
		#count+=2#for start and end
		predone = (-1/count)*x
		perplex = 10**(predone)
		return perplex#do without the logs, see what you get


	def probability_run(n,g, r):
		'''combines probability elements for multiple test sentences'''
		previous = 0#these are becoming very tiny numbers, need to fix with logs
		total = 0
		for sent in n:
			previous = perplexity(sent,first_element(sent,g,r)+middle_elements(sent,g,r)+last_element(sent,r))
			total += previous
		average = total/len(n)#average perplexity over all utterances
		print("AVERAGE!", average)
		outfile.write("eng average for ff for file number "+str(file_num)+" "+str(average))
		return average

	def probability_run_cat(n,g, r):
		'''combines probability elements for multiple test sentences'''
		previous = 0#these are becoming very tiny numbers, need to fix with logs
		total = 0
		for sent in n:
			previous = perplexity(sent,(first_element_cat(sent,g,r)+middle_elements_cat(sent,g,r)+last_element_cat(sent,r)))
			total += previous
		average = total/len(n) #average perplexity for utterance
		print("AVERAGE!", average)
		outfile2.write("eng average for gold for file number "+str(file_num)+" "+str(average))
		return average

	
	#test: start-w1-w2-w3-end
	def first_element(test, g,r):
		'''returns probability of frist word in test sentence'''
		first_word = test[1]#changing this first
		category = str(test[0]+' '+test[2])
		count = 0
		utt_prob_start = 0
		in_cat = 0
		final_first = 0
		for sentence in r:
			if test[0] == sentence[0] and test[2] == sentence[2]:
				count +=1
		utt_prob_start = (count+.5)/(len(r)+.5)#.5 for smoothing
		#trying other smoothing
		if category in g and first_word in g[category]:
			in_cat = (g[category].count(first_word))/(len(g[category]))
		else:
			in_cat = 1
		final_first = utt_prob_start*in_cat
		return log10(final_first)

	def middle_elements(test, g,r):
		'''returns probability of middle words in test sentence (will revise to section)'''
		cat_instances = 0
		following_cat = 0
		previous = 0
		if len(test) >3:
			for num in range(1,(len(test)-2),1):#fix for frames?
				category = str(test[num-1]+' '+test[num+1])
				next_category = str(test[num]+' '+test[num+2])
				count = 0
				new_count = 0
				utt_prob = 0
				for sentence in r:
					for x in range(len(sentence)-3):
						if sentence[x] == test[num-1] and sentence[x+2] == test[num+1]:
							count += 1
						if sentence[x] == test[num-1] and sentence[x+2] == test[num+1] and sentence[x+1] == test[num] and sentence[x+3] == test[num+2]:
							new_count += 1
				cat_instances = count
				following_cat = new_count
				one_word_prob = (new_count+.5)/(count+.5)#.5 for smoothing
				#trying to fix something, testing for other smoothing
				if next_category in g and test[num+1] in g[next_category]:
					in_cat = (g[next_category].count(test[num+1]))/(len(g[next_category]))
				else:
					in_cat = 1
				if previous == 0:
					previous = log10(one_word_prob*in_cat)
				else:
					previous = previous + log10(one_word_prob*in_cat)
		else:
			previous = 0
		return previous

	def last_element(test,r):
		'''returns probability of last element in test sentence'''
		count = 0
		ends = 0
		category = str(test[-3]+' '+test[-1])
		last_prob = 0
		for sentence in r:
			for x in range(len(sentence)-2):
				if sentence[x] == test[-3] and sentence[x+2] == test[-1]:
					count +=1
			if sentence[-3] == test[-3] and sentence[-1] == test[-1]:
				ends +=1
		last_prob = (ends+.5)/(count+.5)
		return log10(last_prob)


	def first_element_cat(test, g,r):#~*~*~*~*~**~**~fix for utterances two words or less!!!
		'''returns probability of frist word in test sentence'''
		word_plus_cat = test[1].split("**")
		if test[1] in checklist:#checklist should be from training words
			first_word = word_plus_cat[0]
			category = word_plus_cat[1]
		else:
			first_word = word_plus_cat[0]
			category = "own_cat"+str(first_word)
		count = 0
		utt_prob_start = 0
		in_cat = 0
		final_first = 0
		if test[1] in checklist:
			count = prob_dict_first[category]
		utt_prob_start = (count+.5)/(len(r)+.5)#.5 for smoothing
		#trying other smoothing
		if category in g and first_word in g[category]:
			in_cat = (g[category].count(first_word))/(len(g[category]))
		else:
			in_cat = 1
		final_first = log10(utt_prob_start*in_cat)
		#print("first ok!")
		return final_first
	#d = reg_cat
	def middle_elements_cat(test, g,r):
		'''returns probability of middle words in test sentence (will revise to section)'''
		cat_instances = 0
		following_cat = 0
		previous = 0
		if len(test)>3:
			for num in range(1,(len(test)-2),1):
				word_plus_cat = test[num].split("**")
				if test[num] in checklist:
					category = word_plus_cat[1]
				else:
					category = "own_cat"+str(word_plus_cat[0])
				word_plus_nextcat = test[num+1].split("**")
				if test[num+1] in checklist:
					next_category = word_plus_nextcat[1]
				else:
					next_category = "own_cat"+str(word_plus_nextcat[0])
				one_word_prob = 1
				if test[num] in checklist and test[num+1] in checklist and str(category)+"_"+str(next_category) in prob_dict_mid.keys():
					one_word_prob = prob_dict_mid[str(category)+"_"+str(next_category)]#.5 for smoothing
				#trying to fix something, testing for other smoothing
				if next_category in g and word_plus_nextcat[0] in g[next_category]:
					in_cat = (g[next_category].count(word_plus_nextcat[0]))/(len(g[next_category]))
				else:
					in_cat = 1
				if previous == 0:
					previous = log10(one_word_prob*in_cat)
				else:
					#print(one_word_prob, "one_word_prob")
					#print(in_cat, "in_cat")
					previous = previous+log10(one_word_prob*in_cat)
		else:
			previous = 0
		#print("middle ok!")
		return previous#explain balance between having lots of categories and few categories

	def last_element_cat(test,r):
		'''returns probability of last element in test sentence'''
		count = 0
		ends = 0
		last_prob = 0
		word_plus_cat = test[-2].split("**")
		if test[-2] in checklist:
			category = word_plus_cat[1]
		else:
			category = "own_cat"+str(word_plus_cat[0])
		last_prob = 1
		if test[-2] in checklist:
			last_prob = prob_dict_last[category]
		#print("last ok!")
		return log10(last_prob)


	outfile = open(str(file_num)+"perplex_w_freq_nogoldapril_ENG.txt","w")
	outfile2 = open(str(file_num)+"perplexity_gold_aslapril_ENG.txt", "w")


	if frame_or_no == "f":
		'''
		print("same deal but with frames")
		if "start! BREAK" in FRAMES:
			print(len(FRAMES["start! BREAK"]), "len of first frame in FRAMES")
		else:
			print(len(FRAMES["own_catfs-JOHN"]), "owncatfs-JOHN")
		print(FRAMES["start! BREAK"].count("fs-JOHN"))
		print(len(FRAMES["fs-JOHN WINDOW"]), "len of second frame in FRAMES")
		print(FRAMES["fs-JOHN WINDOW"].count("BREAK"))
		print(len(FRAMES["BREAK end!"]), "len of third frame in FRAMES")
		print(FRAMES["BREAK end!"].count("WINDOW"))
		'''
		outfile.write('it is perplexity time!  okay first the FRAAMMESSSS!!!\n')
		#training is a, test is c:r
		print("perplexity for frames! ho!\n")
		print(file_num)
		outfile.write(str(perplexity(for_frames_list_c, probability_run(for_frames_list_c, FRAMES,for_frames_list_a))))
		outfile.write('~*~*~*~*~')
		print(str(perplexity(for_frames_list_c, probability_run(for_frames_list_c, FRAMES,for_frames_list_a))))
	elif frame_or_no == "c":
		'''
		print("length of dictionary entry for all words in test utterance and category")
		print(len(cat_dict["PN"]), "len of PN in cat_dict")
		print(cat_dict["PN"].count("fs-JOHN"))
		print(len(cat_dict["V"]), "len of V in cat_dict")
		print(cat_dict["V"].count("BREAK"))
		print(len(cat_dict["N"]), "len of N in cat_dict")
		print(cat_dict["N"].count("WINDOW"))
		'''
		outfile2.write("it's perplexity time!  categories!\n")
		print("perplexity for categories, ho!\n")
		print(file_num)
		#outfile2.write(str(perplexity(for_cat_list_c, probability_run_cat(for_cat_list_c, cat_dict,for_cat_list_a))))
		print(str(perplexity(for_cat_list_c, probability_run_cat(for_cat_list_c, cat_dict,for_cat_list_a))))
	else:
		print("god knows.")

