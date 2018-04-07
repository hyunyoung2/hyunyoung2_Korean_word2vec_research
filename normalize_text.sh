#!/usr/bin/env bash 


# Author: hyunyoung2(github id)
# This shell script is for nomarlizing wikimedia's korean language.
# This version is basic version from Fasttext's get-wikimedia.sh
# This normalization mean removing a phrase beginning with "(" and endig with ")".

# If you want to know how to use sed command, visit https://www.tutorialspoint.com/unix/unix-regular-expressions.htm
# -e 's/\.\([^0-9]\)/ \1/g', That is regular expression inside the parenthesis would be back referenced by \1, \2 and so on
# remember the lien right above.

DATE=$(date +%Y%m%d)

# The location of directory
ROOT="train_data/raw_data"
NORMALIZATION="${ROOT}/normalization/${DATE}"

FILENAME=${ROOT}"/wiki_00"
# \#

sed -e "s/‘/'/g" -e "s/’/'/g" -e "s/′/'/g" -e "s/“/\"/g" -e "s/”/\"/g" -e "s/\`/ \` /g" \
    -e 's/([^)]*)//g' -e 's/( )//g' -e 's/()//g' -e 's/(//g' -e 's/)//g' \
    -e "s/''//g" -e 's/""//g' -e "s/'//g " -e 's/"//g' \
    -e 's/\. / \. /g' -e 's/다\./다 \. /g' -e 's/오\./오 \. /g' -e 's/, / , /g' -e 's/…/ … /g' -e 's/·/ · /g' -e 's/•/ • /g' \
    -e 's/\-\-/ \-\- /g' -e 's/-/ - /g' -e 's/=/ = /g' -e 's/\;/ \; /g' -e 's/\:/ \: /g' \
    -e 's/\!/ \! /g' -e 's/\?/ \? /g' -e 's/*/ /g' -e 's/|/ /g' -e 's/\// \/ /g' \
    -e 's/<br \/>/ /g' \
    -e 's/«//g' -e 's/»//g' -e 's/\《//g' -e 's/\》//g' -e 's/\[//g' -e 's/\]//g' -e 's/ </ /g' -e 's/>//g' \
    -e 's/≪//g' -e 's/≫//g' -e 's/『//g' -e 's/』//g' -e 's/〈//g' -e 's/〉//g' $FILENAME > ${FILENAME}"_normalized"

#    -e 's/«/ « /g' -e 's/»/ » /g' -e 's/《/ 《  /g' -e '/》/ 《  /g' $FILENAME > only_wiki_00_normalized 
