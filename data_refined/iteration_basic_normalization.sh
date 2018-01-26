#!/usr/bin/env bash

# For iteration of basic_normalizatioin.sh


for dir in AA AB AC AD AE
do 
	for i in {00..99} 
	do 
		./basic_normalization.sh $i $dir
	done
done

for i in {00..62}
do
	./basic_normalization.sh $i AF
done
