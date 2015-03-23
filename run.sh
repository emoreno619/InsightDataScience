#!/bin/bash
############################################################################################
############################################################################################
##
##	Program title:	run.sh
##
##	Purpose:	Script to run both word_mapper.py and word_reducer.py, and to
##			sort the intermediary data between them
##
##	Programmer:	Eduardo Moreno
##
##	Date:		03/22/15
##
##	input:		all files in ./wc_input/
##
##	output:		two files, wc_result.txt (the # of each word's occurence in the
##			input files) and med_result.txt (the running median of words per
##			line throughout the input files). Both files are output to
##			./wc_output/
##
##	notes:		1) output file wc_result.txt will be overwritten each time run.sh
##						2) output file med_result.txt will always be appended, so it will
##			   			 log running median across multiple executions of run.sh
##						3) intermediary file ./temp/map_result.txt will always be overwritten
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
##	word_reducer.py will:
##
##				1) take the output of key-value pairs from word_mapper.py
##				   (i.e., each word and a value of 1) stored in
##				   ./temp/map_result.txt
##
##				2) reduce the input key-value pairs to a single unique key-
##				   value pair for unique key, so values of all like keys
##				   are summed and stored as one value in a key-value pair
##				3) see file for further details and documentation
##
############################################################################################
############################################################################################
##
###############################   Declaration of Variables  ###############################
##
############################################################################################
##
	declare -a list1	# to empty intermediary output file (./temp/map_result.txt)
	declare -a files	# to hold files name from input directory (./wc_input/)
	files="./wc_input/*"	# fills files with the name of each file in input directory
	list1=()
##
############################################################################################
############################################################################################
##
## optional echoing of input files to word_mapper.py
##	 echo $files
##	 echo "Reading input..."
##
## ensures map_result.txt is empty by overwriting its contents for each execution of script
##
	$list1 > ./temp/map_result.txt
##
############################################################################################
##
################################# 	Map phase 	###################################
##
############################################################################################
##
## loops through each file in input directory and passes it as argument to word_mapper.py
## see word.mapper.py for more details on how words are mapped and median calculated
##
## outputs wc_result.tx (the # of each word's occurence in the input files) and
## med_result.txt (the running median of words per line throughout the input files). Both
## files are output to ./wc_output/
##
##
	for file in $files
	do
		list1=("${list1[@]}" $file)
		python word_mapper.py $file
	done
##
############################################################################################
############################################################################################
##
############################### 	Reduce Phase      #################################
##
############################################################################################
##
## 	Hadoop simulation
##
##	Invokes bash's sort (which sorts in place, so somewhat scalable) on aggregated
##	text from files in input directory (map_result.txt) and outputs that sort to a file
##	(map_result2.txt) to be passed to word_reducer.py
##
	cat ./temp/map_result.txt | sort > ./temp/map_result2.txt
##
##
##	PREFERRED reduce method, using word_reducer.py I wrote. Almost portable to Hadoop.
##
##	I encountered some difficulty running the MapReduce application (both .py files)
##	on an hdfs cluster. The most success I had was successfully completing the job
##	but only receiving an empty output file. When I ran on the cluster, I modified
##	the .py files to take input from sys.stdin and to output to stdout rather than
##	to .txt files. Running on hdfs would be better for scalability because it allows
##	the job to be parallelized and worked on across many machines as well as avoid the
##	need to make a copy of all data (as I do with the intermediary file,
##	map_result.txt).
##
	python word_reducer.py ./temp/map_result2.txt
##
##	ALTERNATIVE reduce method, using bash's uniq -c
##
##		1) Slower
##		2) Doesn't format correctly, formats as (value, key) i.e., (number of ##		   occurences \t word) rather than (key, value)
##
##	#cat ./temp/map_result2.txt | uniq -c > ./wc_output/wc_result2.txt
##
##
##
	echo "Job done!"
############################################################################################
############################################################################################
############################################################################################
