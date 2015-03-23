#!/usr/bin/python
############################################################################################
############################################################################################
##
##	Program title:	word_reducer.py
##
##	Purpose:	Sums values of all like keys (the same word) and stores the number
##			of occurences of that word from input files as one value in a key-
##			value pair
##
##	Programmer:	Eduardo Moreno
##
##	Date:		03/22/15
##
##	input:		all files in ./temp/map_result.txt
##
##	output:		one file, wc_result.txt (the # of each word's occurence in the
##			input files)
##
##	dependencies:	python
##
##	word_reducer.py will:
##
##				1) take the output of key-value pairs from word_mapper.py
##				   (i.e., each word and a value of 1) stored in
##				   ./temp/map_result.txt
##				2) reduce the input key-value pairs to a single unique key-
##				   value pair for unique key, so values of all like keys
##				   are summed and stored as one value in a key-value pair
##				3) see file for further details and documentation
##
############################################################################################
############################################################################################
##
#################################  Dependency import  ##################################
##
############################################################################################

import sys

############################################################################################
##
###############################   Function Definition  ###############################
##
############################################################################################

def reducer():

############################################################################################
##
############################ Variable Declaration and Definition ##########################
##
############################################################################################


	##	file output new set of condensed key-value pairs with word occurence
	##	frequencies
	f1=open('./wc_output/wc_result.txt', 'w+')

	##	file input containing sorted key-value pairs of word from text
	f2=open(sys.argv[1], 'r+')

	##	stores running total of occurence for a given key or word (thisKey)
	countTotal = 0

	##	stores previous key or word, to determine once the current key is different
	oldKey = None

############################################################################################
############################################################################################
############################################################################################


	##for each line (so each key-value pair) in file of sorted key-value pairs
	for line in f2:

		###########################################################################
		####	cleaning, checking and storing key-value pairs
		###########################################################################

		##split that data into its respective keys and value and store in a list
		##"data"
		data = line.strip().split("\t")


		## error checking in case of dirty data that is not key-value pair, exit
		if len(data) != 2:
			continue

		## list elements of "data" are stored in variables, thisKey and thisCount
		thisKey, thisCount = data

		###########################################################################
		####	summation of values for a given key and output to file
		###########################################################################

		## check to see if end of current key or word has been reached, and if so
		## write new key-value pair to file, containing sum of matching keys or
		## words from original input
		if oldKey and oldKey != thisKey:
			f1.write("{0}\t{1}\n".format(oldKey, countTotal))
			#print "{0}\t{1}".format(oldKey, countTotal)

			#reset countTotal because next key's sum will begin
			countTotal = 0

		#oldKey always set to currentKey, countTotal always incremented
		oldKey = thisKey
		countTotal += int(thisCount)

	##once loop is completed must still record final key!
	if oldKey != None:
		f1.write("{0}\t{1}\n".format(oldKey, countTotal))
		#print "{0}\t{1}".format(oldKey, countTotal)

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

reducer()

############################################################################################
##
##################################  End Function Call  ##################################
##
############################################################################################
