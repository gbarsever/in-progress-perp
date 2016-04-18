#this will make type list and will make chuncks (find chunk code!)

infile = open("final_to_perplex.txt", "r")
readinfile = infile.read()
infile.close()
infile3 = open("better_perplex_eng.txt", "r")
readinfile3 = infile3.read()
infile3.close()
infile_adult = open("clean_adult_eng_gold.txt", "r")
readinadult = infile_adult.read()
outfile = open("better_types.txt", "w")
outfile2 = open("better_tokens.txt", "w")
outfile3 = open("better_tokens_eng.txt", "w")
outfile4 = open("better_tokens_adult.txt","w")
#
split_adult = readinadult.split()
split_file = readinfile.split()
split_file_eng = readinfile3.split()
big_list_eng = []
big_list = []

big_set = set()

big_list_adult =[]

for l in split_adult:
	big_list_adult.append(l)


for k in big_list_adult:
	outfile4.write(str(k)+"\n")

for x in split_file:
	big_set.add(x)
	big_list.append(x)

for y in big_set:
	outfile.write(str(y)+"\n")

for z in big_list:
	outfile2.write(str(z)+"\n")

for p in split_file_eng:
	big_list_eng.append(p)
	
for q in big_list_eng:
	outfile3.write(str(q)+"\n")