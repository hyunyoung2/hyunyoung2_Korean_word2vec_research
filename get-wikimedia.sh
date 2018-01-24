#!/usr/bin/env bash

# Author: hyunyoung2(github id)

# To download Korean wikipedia dump file from htts://dump.wikimedia.org/kowiki
# The latest one of the "htts://dump.wikimedia.org/kowiki"
# The file name of kowiki is "kowiki-latest-pages-articles.xml.bz2"
URL="https://dumps.wikimedia.org/kowiki/latest/kowiki-latest-pages-articles.xml.bz2"

TRUE="true"
FALSE="false"


# To Check if the directory is there
check_dir () {
   # -d is to check if $1 is a directory 
   if [ -d $1 ]; then
       # -L is to check if $1 is symbolic link
       if [ -L $1 ]; then
           echo "${1}(symbolic link) already exists!!"
           echo "You don't need to make a directory for ${1}"
           echo ""
           return $FALSE
       else
           echo "$1 is not symbolic link"
           echo "But, $1 already exstis!"
           echo ""
           return $FALSE
       fi
   else
      mkdir -p $1
      echo "saving data in $1"
      return $TRUE
   fi
}


# +"%Y%m%d" is for format control of date command
NOW=$(date +"%Y%m%d")

# Root Directory to save data such as wiki dump file, open source(Wikiextractor), the parsed wiki dump file
ROOT="data/wikimedia/${NOW}"
# To check if the directory aleary exist
# -d is to check if $ROOT is a directory
if [ -d $ROOT ]; then
    # -L is to check if $ROOT is symbolic link
    if [ -L $ROOT ]; then 
       echo "${ROOT}(symbolic link) already exists!!"
       echo "You don't need to make a directory for $ROOT"
       echo 
    else
       echo "$ROOT is not symbolic link"
       echo "BUT, $ROOT already exist!"
       echo "You don't need to make a directory for $ROOT"
       echo ""
    fi 
else 
    mkdir -p $ROOT
    echo "saving data in $ROOT"
    wget -c $URL -P $ROOT 
    echo "Precessing ""${ROOT}"/"kowiki-latest-pages-articles.xml.bz2"	
    echo ""
fi

# git clone  Open source of wikiextractor
PARSING="${ROOT}/parsing"
if [ -d "$PARSING" ]; then
    if [ -L "$PARSING" ]; then 
       echo "${PARSING}(symbolic link) already exsits!!"
       echo "You don't need to make a directory for ${PARSING}"
       echo ""
    else 
       echo "$PARSING is not symbolic link"
       echo "BUT, ${PARSING} already exists!"
       echo "You don't need to make a directory for ${PARSING}"   
       echo ""
    fi
else 
    mkdir -p "${PARSING}"
    echo "saving wikiextractor opensource in ${PARSING}"
    git clone "https://github.com/attardi/wikiextractor.git" "${PARSING}"
    echo "git clont wikiextractor is saved in""$PARSING"
    echo ""
fi

# parse wikimedia with wikiextractor
WIKI_BY_WIKIEXTRACTOR="${ROOT}/raw_wiki"
# json type of the parsed file
JSON="${WIKI_BY_WIKIEXTRACTOR}/json"
# plaintext type of the parsed file
PLAINTEXT="${WIKI_BY_WIKIEXTRACTOR}/plaintxt"

echo $WIKI_BY_WIKIEXTRACTOR

## To choose JSON or PLAINTEXT
read -r -p "Choose what type of text(e.g. j: json, p: plaintext(basic setting of wikiextrator), etc.): " choice
case "$choice" in
    j ) echo "your choice is JSON";;
    p ) echo "your choice is PlainText";;
    * ) echo "Invalid answer"; exit 1;;
esac

# To get parsed wiki
if [ -d "$WIKI_BY_WIKIEXTRACTOR" ]; then 
    echo "${WIKI_BY_WIKIEXTRACTOR}(symlink) already exsits!!"
    echo "You don't need to make a directory for $WIKI_BY_WIKIEXTRACTOR" 
    echo ""
else
    mkdir -p $WIKI_BY_WIKIEXTRACTOR
    echo "saving the parsed wiki in ${WIKI_BY_WIKIEXTRACTOR}"
fi

if [ "$choice" = "j" ]; then 
    if [ -d "$JSON" ]; then 
        python3 ${PARSING}"/"WikiExtractor.py -o $JSON --json ${ROOT}"/"kowiki-latest-pages-articles.xml.bz2
    else 
        mkdir $JSON
        python3 ${PARSING}"/"WikiExtractor.py -o $JSON --json ${ROOT}"/"kowiki-latest-pages-articles.xml.bz2
   fi    
else
   if [ -d "$PLAINTEXT "]; then
       python3 ${PARSING}"/"WikiExtractor.py -o $PLAINTEXT ${ROOT}"/"kowiki-latest-pages-articles.xml.bz2 
   else 
       mkdir $PLAINTEXT
       python3 ${PARSING}"/"WikiExtractor.py -o $PLAINTEXT ${ROOT}"/"kowiki-latest-pages-articles.xml.bz2 
   fi
fi


