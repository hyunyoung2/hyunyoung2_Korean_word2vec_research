#!/usr/bin/env bash

# Author: hyunyoung2(github id)

# This shell script is for setting up of normalizing original file of wikimedia and divided a file into each file of doc tage(<doc id=...> ... </doc>


WIKIMEDIA="../wikimedia/raw_wiki/plaintxt"
DESTINATION="./original"

if [ -d $WIKIMEDIA ]; then
    if [ -d $DESTINATION ]; then 
	echo "There is already $DESTINATION" 
	#exit
    else
        cp -avr ${WIKIMEDIA} $DESTINATION
	echo "cp all is done!!"
    fi
else
    echo "you do not have wikimedia directory"
    echo "execute ../get-wikimedia.sh"
    echo "parse wikimedia into palintext with wikimedia"
    exit
fi

DIVIDED="./divided/original"

if [ -d $DIVIDED ]; then
    echo "There is already $DIVIDED"
    #exit
else
    python3 divided_originally.py
fi

LONG_CONTENTS="./divided/long_contents"

if [ -d $LONG_CONTENTS ]; then
    echo "There is already $LONG_CONTENTS"
    #exit
else
    python3 long_contents.py
fi

# if you want to normalize wikipedia article after divided it

NORMALIZED="./normalized/long_contents"

if [ -d $NORMALIZED ]; then 
    echo "There is already $NORMALIZED" 
    #exit
else 
    ./iteration_basic_normalization.sh
fi

DATASET="../dataset"

if [ -d $DATASET ]; then 
	echo "you have already the $DATASET"
	#exit
else 
	mkdir $DATASET
	echo "you created ${DATASET}!!"
	python3 make_dataset.py
	./normalize_text.sh
fi 
