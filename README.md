# InsightDataScience
coding challenge submission



	Program title:	InsightCodingChallenge

	Purpose:	run.sh runs both word_mapper.py and word_reducer.py. the former
			      splits, cleans and sorts input text data into its respective words
			      the latter counts each word's frequency from input text data.
			      word_mapper.py also calculates and stores running median of words 
			      per line in text data

	Programmer:	Eduardo Moreno

	Date:		03/22/15

	input:		all files in ./wc_input/

	output:		two files, wc_result.txt (the  of each word's occurence in the
			input files) and med_result.txt (the running median of words per
			line throughout the input files). Both files are output to
			./wc_output/

	notes:		1) output file wc_result.txt will be overwritten each time run.sh
						2) output file med_result.txt will always be appended, so it will
			   			 log running median across multiple executions of run.sh
						3) intermediary file ./temp/map_result.txt will always be overwritten

	dependencies:	python

	word_mapper.py will:
				1) take all files in ./wc_input/ as input
				2) clean the text of punctuation and capitilization
				3) write each word, a \t and the value 1 to a file
				   (./temp/map_result.txt)
				4) calculate running median of number of words per line
				   and store those medians in ./wc_output/med_result.txt
				5) see file for further details and documentation

	word_reducer.py will:

				1) take the output of key-value pairs from word_mapper.py
				   (i.e., each word and a value of 1) stored in
				   ./temp/map_result.txt

				2) reduce the input key-value pairs to a single unique key-
				   value pair for unique key, so values of all like keys
				   are summed and stored as one value in a key-value pair
				3) see file for further details and documentation
