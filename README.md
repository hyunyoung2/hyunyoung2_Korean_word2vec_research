# Hyunyoung2 Korean word2vec research 

This is about how to get and collect Korean language document over Internet.

In Particular, This repository is how to get and collect text data from wikipedia.


First, IF you run shell script, "get-wikipedia.sh". 

> ./get-wikipedia.sh 

then it would download a directory that is stored with wikipedia document, 

Just in shellscript, get-wikipedia.sh, If you change the URL that you want to download from wikipedia dumpfile. 

That will is download.

That shell script will also download **[wikiextractor](https://github.com/attardi/wikiextractor)** that helps you parse wikipedia text.

Further, You can select the one between json or plaintxt after parsing the wikipedia with wikiextractor.

Second, run "normalized.sh"

> ./normailzed.sh 

That will remove the redundant text. But in shell script, you have to fix the input file path, and then it works. 



