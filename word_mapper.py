#!/usr/bin/python
############################################################################################
############################################################################################
##
##	Program title:	word_mapper.py
##
##	Purpose:	Splits each line the file into its words, cleans data of
##			punctuation and capitalization and stores each word in
##			./temp/map_result.txt with a value of 1. Also, calculates the
##			running median number of words per line, storing those medians
##			in ./wc_output/med_result.txt
##
##	Programmer:	Eduardo Moreno
##
##	Date:		03/22/15
##
##	input:		all files in ./wc_input/
##
##	output:		two files, map_result.txt (each word in the input files, \t, 1)
##			and med_result.txt (the running median of words per line
##			throughout the input files). The first is stored in ./temp/ and
##			the second in ./wc_output/
##
##	dependencies:	python
##
##	word_mapper.py will:
##				1) take all files in ./wc_input/ as input
##				2) clean the text of punctuation and capitilization
##				3) write each word, a \t and the value 1 to a file
##				   (./temp/map_result.txt)
##				4) calculate running median of number of words per line
##				   and store those medians in ./wc_output/med_result.txt
##				5) see file for further details and documentation
##
############################################################################################
############################################################################################
##
###############################   Import Dependencies  ###############################
##
############################################################################################

import sys
from string import maketrans

############################################################################################
##
###############################   Function Definition  ###############################
##
############################################################################################


def mapper():

############################################################################################
##
#########################  Variables Declaration and Definition  #########################
##
############################################################################################

## 	string cleaning variables for translation()
	intab = " "
	outtab = " "
	trantab = maketrans(intab, outtab)

##	current line number
	n = 1

##	index of median number of indices, used for calculating running median
	indexmid = 0

##	arrays to store number of words per line (wc) and each median per line (rmed)
	wc = []
	rmed = []

##	file output for running medians
	f1=open('./wc_output/med_result.txt', 'a')

##	file output for record of each word, to be passed to reduce
	f2=open('./temp/map_result.txt', 'a')

##	file input containing text to be analyzed
	f3=open(sys.argv[1], 'r')

############################################################################################
############################################################################################
############################################################################################

## for each line in file, break line into words, and produce number of words
	for line in f3:

		#words in each line stored in list "data"

		data = line.strip().split(" ")

		###########################################################################
		####	Calculate and Store Running Median
		###########################################################################

		#appends number of words of a line to wc[] and prevents empty line from
		#submitting length of 1
		if data[0] != '':
			wc.append(len(data))
		else:
			wc.append(0)

		#sorts array with word counts of each line, to calculate median
		wc.sort()

		#calculates median, if even number of lines, median is ave between two
		#center elements, else median is middle element
		if (n%2 == 0):
			currMedian = float((wc[indexmid]+wc[indexmid+1])/float(2))
			indexmid += 1
		else:
			currMedian = float(wc[len(wc)/2])

		#output of median to median list and file

		rmed.append(currMedian)
		n += 1

		f1.write("{0}\n".format(currMedian))

		###########################################################################
		####	String Cleanup, Formatting and Output
		###########################################################################

		#for each word in a line
		for word in data:

			#all characters made lowercase
			word = str.lower(word)

			#all punctuation characters are removed
			word = word.translate(trantab, '~`!@#$%^&*()_-+={}[]\|;\':\",./<>?')

			#cleaned words are now paired with a 1 and written to file,
			#./temp/map_result.txt
			if len(word) > 0:
				wc_pair = "{0}\t{1}".format(word, 1) #for word_reducer.py
				f2.write("{0}\n".format(wc_pair))

				#Optional remanants for utilizing alternative reduce (uniq)
				#wc_pair = "{0}\t".format(word)		#for uniq -c
				#print wc_pair

	f1.close()
	f2.close()
############################################################################################
##
############################### End Function Definition  ###############################
##
############################################################################################
############################################################################################
############################################################################################
############################################################################################
############################################################################################
############################################################################################
##
#################################   Function Call  ######################################
##
############################################################################################

mapper()

############################################################################################
##
##################################  End Function Call  ##################################
##
############################################################################################
