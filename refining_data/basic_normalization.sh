#!/usr/bin/env bash 


# Author: hyunyoung2(github id)
# This shell script is for nomarlizing wikimedia's korean language.

# Input file name
FILENAME=$1 # like wiki_000 ~ wiki_999

# The directory of input file name
DIR=$2 # like AA/wiki_00

# The location of directory

# The replica of wikimedia/raw_wiki/plaintxt/AA ... AF
REPLICA_ROOT="divided/long_contents/${DIR}"

echo $REPLICA_ROOT
if [ -d $REPLICA_ROOT ]; then 
	if [ -L $REPLICA_ROOT ]; then
		echo "${REPLICA_ROOT}(symbolic link) already exists!!!"
		echo "You don't need to make a directory for $REPLICA_ROOT"
		echo
	else
		echo "$REPLICA_ROOT is not symbolic link! BUT, You have already $REPLICA_ROOT"
		echo "You don't need to make a directory for $REPLICA_ROOT"
		echo 
	fi
else
	mkdir -p $REPLICA_ROOT
	echo "You made the directory called $REPLICA_ROOT"
	echo
fi


# The Root of data normalized
NORMALIZATION_ROOT="normalized/long_contents/${DIR}"

echo $NORMALIZATION_ROOT
if [ -d $NORMALIZATION_ROOT ]; then 
	if [ -L $NORMALIZATION_ROOT ]; then
		echo "${NORMALIZATION_ROOT}(symbolic link) already exists!!!"
		echo "You don't need to make a directory for $NORMALIZATION_ROOT"
		echo
	else
		echo "$NORMALIZATION_ROOT is not symbolic link! BUT, You have already $NORMALIZATION_ROOT"
		echo "You don't need to make a directory for $NORMALIZATION_ROOT"
		echo 
	fi
else
	mkdir -p $NORMALIZATION_ROOT
	echo "You made the directory called $NORMALIZATION_ROOT"
	echo
fi

# Final input 
INPUT=${REPLICA_ROOT}"/"${FILENAME}



# final output
OUTPUT=${NORMALIZATION_ROOT}"/"${FILENAME}


# normalizing data
sed -e 's/<nowiki>//g' -e 's/<\/nowiki>//g' -e 's/<math>//g' -e 's/<\/math>//g' \
    -e "s/‘/'/g" -e "s/’/'/g" -e "s/′/'/g" -e "s/“/\"/g" -e "s/”/\"/g" -e "s/\`/'/g" -e "s/´/'/g" \
    -e 's/\.\"/\. \"/g' -e "s/\.\'/\. \'/g" \
    -e 's/\.\.\./\. /g' -e 's/~/ ~ /g' -e 's/∼/ ∼ /g' -e 's/\. / \. /g' \
    -e 's/([^)]*)//g' -e 's/()//g' -e 's/( )//g' -e 's/(//g' -e 's/)//g' \
    -e 's/"//g' -e "s/'//g" -e 's/, / /g' \
    -e 's/…/ /g' \
    -e 's/·/ /g' -e 's/•/ /g' -e 's/-/ /g' -e 's/→/ → /g' \
    -e 's/\!/ \! /g' -e 's/\?/ \? /g' -e 's/\;/ /g' -e 's/\:/ /g' -e 's/*/ /g' -e 's/|/ /g' \
    -e 's/«/ /g' -e 's/»/ /g' \
    -e 's/「//g' -e 's/」//g' -e 's/ \[//g' -e 's/\[.*\]//g' -e 's/\]//g' \
    -e 's/≪//g' -e 's/≫//g' -e 's/『//g' -e 's/』//g' -e 's/〈//g' -e 's/〉//g' -e 's/《//g' -e 's/》//g' $INPUT > $OUTPUT


echo "normalizing is done!!" 

# sed -e 's/<nowiki>//g' -e 's/<\/nowiki>//g' \
# -e 's/ <//g' -e 's/>//g' -e 's/≥//g' -e 's/≤//g'
# -e 's/·/ - /g' -e 's/•/ - /g' -e 's/-/ - /g' \
# -e 's/=/ /g'
# -e 's/「//g' -e 's/」//g' -e 's/＜//g' -e 's/＞//g' 
