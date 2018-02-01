# Data refined. 

This directory is for refinding text file, after calling **get-wikimedia.sh**.

Ahead of calling **sample_normalization.sh**, you have to copy from data dic which is the destination of **get-wikimedia.sh**


If you want to divide the wiki files into each file including a dog tag(\<dog =id...\> ... \</dog\>)


execute **basic_set_up.sh**

> $ ./set_up.sh


If you run **set_up.sh**, 

First, copy the plaintxt of wikiextractors in **wikimedia dir** under original directory(divided_originally.py)

Second, each contend surrounded by certain tags like \<dog id=..\> and \</dog\> will be separate. 

Third, the short one of each contents surronded by the tags above is removed. 

Fourth, it will first normalize it. 

Fifth, it will makes dataset with another normalizing such as contents and title. 
