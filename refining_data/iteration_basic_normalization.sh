#!/usr/bin/env bash

# For iteration of basic_normalizatioin.sh


DIR="divided/long_contents"

for dir in AA AB AC AD AE
do 
	for i in {00..99} 
	do 
		MIDDLE_PATH=${dir}"/wiki_"$i

		ls_command=`ls ${DIR}"/"$MIDDLE_PATH`
		for j in $ls_command
		do	
			./basic_normalization.sh $j $MIDDLE_PATH
		done
	done
done

for i in {00..62}
do
	MIDDLE_PATH2="AF/wiki_"$i
	ls_command2=`ls ${DIR}"/"$MIDDLE_PATH`
	for j in $ls_command2
	do	
		./basic_normalization.sh $j $MIDDLE_PATH2
	done
done

