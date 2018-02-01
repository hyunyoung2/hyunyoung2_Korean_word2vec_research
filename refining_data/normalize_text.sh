#!/usr/bin/env bash 


# Author: hyunyoung2(github id)
# This shell script is for nomarlizing wikimedia's korean language.
# This shell is only used to remove the things like "<", ">" character on contents
# So, After normalizing it, the file name is contents_normalized. 

EX_DIR=".."

DATASET="dataset"

ROOT_DIR=${EX_DIR}"/"$DATASET

INPUT_FILENAME="contents"

OUTPUT_FILENAME="contents_normalized"

INPUT=${ROOT_DIR}"/"$INPUT_FILENAME

OUTPUT=${ROOT_DIR}"/"$OUTPUT_FILENAME

sed  -e 's/<//g' -e 's/>//g' $INPUT > $OUTPUT

#    -e 's/«/ « /g' -e 's/»/ » /g' -e 's/《/ 《  /g' -e '/》/ 《  /g' $FILENAME > only_wiki_00_normalized 
