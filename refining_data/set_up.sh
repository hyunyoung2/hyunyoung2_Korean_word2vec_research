#!/usr/bin/env bash

# Author: hyunyoung2(github id)

# This shell script is for setting up of normalizing original file of wikimedia and divided a file into each file of doc tage(<doc id=...> ... </doc>


WIKIMEDIA="../wikimedia/raw_wiki/plaintxt"

if [ -d $WIKIMEDIA ]; then
     # -L is to check if $ROOT is symbolic link
    if [ -L $WIKIMEDIA ]; then
       echo "${WIKIMEDIA}(symbolic link) already exists!!"
       cp -r ../wikimedia/raw_wik/plaintxt/* ./original 
       echo "cp all is done!!"
       echo
    else
       echo "$WIKIMEDIA is not symbolic link"
       echo "BUT, $WIKIMEDIA already exist!"
       cp -r ../wikimedia/raw_wik/plaintxt/* ./original 
       echo "cp all is done!!"
       echo 
    fi
else
    echo "you don't have wikimedia directory"
    echo "execute ../get-wikimedia.sh"  
    echo "parse wikimedia into palintext with wikimedia"
    exit
fi

./iteration_basic_normalization.sh

python3 divided.py 
