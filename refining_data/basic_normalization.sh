#!/usr/bin/env bash 


# Author: hyunyoung2(github id)
# This shell script is for nomarlizing wikimedia's korean language.

# Input file name
FILENAME="wiki_"$1 #"wiki_00"

# The directory of input file name
DIR=$2 #"AA"

# The location of directory

# The replica of data/wikimedia/20180124/raw_wiki/plaintxt/AA ... AF
REPLICA_ROOT="original/${DIR}"
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
NORMALIZATION_ROOT="normalized/${DIR}"
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
sed -e "s/‘/'/g" -e "s/’/'/g" -e "s/′/'/g" -e "s/“/\"/g" -e "s/”/\"/g" -e "s/\`/'/g" -e "s/´/'/g" \
    -e 's/."/. "/g' -e "s/.'/. '/g" \
    -e 's/.../. /g' -e 's/~/ ~ /g' -e 's/. / . /g' \
    -e 's/([^)]*)//g' -e 's/()//g' -e 's/( )//g' \
    -e 's/"//g' -e "s/'//g" -e 's/, / /g' \
    -e 's/…/ /g' \
    -e 's/·/ /g' -e 's/•/ /g' -e 's/-/ /g' \
    -e 's/\!/ \! /g' -e 's/\?/ \? /g' -e 's/\;/ /g' -e 's/\:/ /g' -e 's/*/ /g' -e 's/|/ /g' \
    -e 's/«/ /g' -e 's/»/ /g' -e 's/</ /g' -e 's/>/ /g' \
    -e 's/≪//g' -e 's/≫//g' -e 's/『//g' -e 's/』//g' -e 's/〈//g' -e 's/〉//g' -e 's/\《//g' -e 's/\》//g' $INPUT > $OUTPUT

echo "normalizing is done!!" 

# -e 's/·/ - /g' -e 's/•/ - /g' -e 's/-/ - /g' \
# -e 's/=/ /g'
# -e 's/「//g' -e 's/」//g' -e 's/＜//g' -e 's/＞//g' 
