# Author: hyunyoung2(github Id)
# To compare sentence vector with word vector to find out title search 
import os
import numpy as np
import collections
import random

# Where the dataset such as contents_normalzed, title 
ROOT = "./practice" # "../dataset"


# The path of files
# contents, title_label, title_predict(current directory), word_vectors
PATHS = ["contents_normalized", "title", "title_predicted", "word_vectors"]

# content literally contains a doc into a line 
# I like it which is ..\n
# dancing is good ...\n
CONTENTS = os.path.join(ROOT, PATHS[0])

# titlel literally contains title of a doc
# taste 
# Korea \t times
# delimiter is \t between words
TITLE_LABEL = os.path.join(ROOT, PATHS[1])

# title_predicted literally the words we predict as title 
# delimiter is \t between words
TITLE_PREDICTED = os.path.join(ROOT, PATHS[2])

# word_vectors literally word vectors. 
# The first line olny include -
# a pair of <the number of words without duplication, the number of dimensionality>
# delimiter is \t between words
WORD_VECTORS = os.path.join(ROOT, PATHS[3])

# split function the standard is \t, \n, and white space
def compat_splitting(line):
    return line.split()

# compare similarity between two word with consine
def similarity(v1, v2):
    n1 = np.linalg.norm(v1)
    n2 = np.linalg.norm(v2)
    return np.dot(v1, v2) / n1 / n2


# read word_vector file 
word_vectors_dic = dict()
num_word_vectors = 0
dimension_word_vectors = 0
with open(WORD_VECTORS, "r") as f:
    for idx, line in enumerate(f):
        if idx == 0: 
            tab = compat_splitting(line)
            num_word_vectors = tab[0]
            dimension_word_vectors = tab[1]
            print("< The number of words , The number of dimensionality >:", 
                  "<", num_word_vectors, "," , dimension_word_vectors, ">")
            
            continue
        try :
            #print("\nline : before splitting line[", idx, "]", line)
            tab = compat_splitting(line)
            #print("tat : after splitting line[", idx, "]", tab)
            vec = np.array(tab[1:], dtype=np.float64) # the type of data is float64
            #print("vec : after splitting line[", idx, "]", vec, type(vec), vec.dtype)
            word = tab[0]
            #print("word_vectors_dic(tab[0]) : after splitting line[", idx, "]", word)
            if np.linalg.norm(vec) == 0:
                print("np.linalg.norm(vec) is zero")
                continue
            if not word in word_vectors_dic:
                word_vectors_dic[word] = vec
        except ValueError:
            print("ValueError happens")
            continue
        except UnicodeDecodeError:
            print("Unicode DecodeError")
            continue
#  To check the length of the word_vectors_dic
print("len of word_vectors_dic:", len(word_vectors_dic))



# To get the n word vectors similar with sum_arr in a sequence of word_vectors_dic
def how_similar_sequantially(sum_arr, n):
    # sum_arr : the sum of a line vector
    # n : retrun size. 
    # prediction : list contins paris of (similarity of consine, word)
    prediction = list()
    for vector_word, vector_value in word_vectors_dic.items():
        prediction.append((similarity(sum_arr, vector_value), vector_word))
    prediction.sort(reverse = True)
    return prediction[0:5]
    
# to get n pair of word vectors similiar with sum_arr between in shuffle and in no-shuflle.
def how_similar_randomly(sum_arr, n , shuffle=True, return_size=1):
    # sum_arr : the sum of a line vector
    # n : retrun size. 
    # prediction : list contins paris of (similarity of consine, word)
    # word_list : keys of word_vectors_dic.keys()
    # paris_words : pairs of n size in word_list
    prediction = list()
    word_list = list(word_vectors_dic.keys())
    
    ##print("word_list befer shuffling:", word_list)
    
    # To shuffle words
    if shuffle == True:
        print("It will be shuffled!")
        random.shuffle(word_list)
    else: 
        print("It will not be shuffled!")
        
    ##print("word_list after shuffling:", word_list)
    
    # to pack n size from words. 
    pairs_words = [word_list[x:x+n] for x in range(0, len(word_list), n)]
    
    for pair_idx, pair_value in enumerate(pairs_words):
        ##print(pair_value, type(pair_value))
        # if the pair_value is less than n, I will not deal with it
        if len(pair_value) < n: 
            continue
        sum_pair = np.zeros(int(dimension_word_vectors), dtype=np.float64)
        
        for idx, val in enumerate(pair_value):
            ##print(val, end=" ")
            sum_pair += (word_vectors_dic[val]/n)
        ##print(sum_pair)
        prediction.append((similarity(sum_arr, sum_pair), pair_value))
    prediction.sort(reverse = True)
    return prediction[0:return_size]
        

# for contents_normalized file
with open(CONTENTS, "r") as f:
    contents_lines = [x for x in f.readlines()]
    if "\n" in contents_lines:
        print("contents_lines error!!!")

print("=== contents lines ===")
print(contents_lines[0:2])

# To store a sequence of title we sequentailly predict
SEQUENCDE_PREDICTED = os.path.join(os.getcwd(), "sequence_predicted")
##print(SEQUENCDE)

# To store a sequence of title we randomly predict
RANDOM_PREDICTED = os.path.join(os.getcwd(), "random_predicted")
##print(RANDOM)


duplication_of_word = True
size_extracted = 5

with open(SEQUENCDE_PREDICTED, "w") as ws:
    with open(RANDOM_PREDICTED, "w") as wr:
        # how to calculate the sum of word vector in a line
        for idx, line in enumerate(contents_lines):
            line_words = list()
            if duplication_of_word == True:
                line_words = compat_splitting(line)
            else:
                for counter_idx, counter_val in enumerate(collections.Counter(line.split()).most_common()):
                    line_words.append(counter_val[0])
            
            print("=== duplication of word ===")
            if duplication_of_word == True:
                print("The usage of duplication of word is permitted")
            else:
                print("The usage of duplication of word is not permitted")
                
            print("=== Before sum of vectors ===")
            print("Contents line:", line, end="")
            print("The resuling split():", line_words[0:5])

            # sum vector of a line
            sum_numarray = np.zeros((int(dimension_word_vectors)), dtype=np.float64)

            # current line.split includes duplication of words. 
            # if you want no duplicatino use the following, use duplication_of_word = False
            # the sum of word vectore in a line, the sum is average.
            for words in line_words:
                sum_numarray += (word_vectors_dic[words]/len(line_words))

            # from here on, I have to retrieve the 5 words to be similar with **sum_numarray**
            print("The sum of a line(",idx,"):", sum_numarray)
            
            print("=== Sequence words ===")  
            sequence_words = how_similar_sequantially(sum_numarray, size_extracted)
               
            print(sequence_words)
            print("A sequence of words:", end=" ")
            for seq_id, seq_word in enumerate(sequence_words):
                if seq_id < size_extracted - 1:
                    print(seq_word[1], end=" ")
                    ws.write(seq_word[1]+"\t")
                elif seq_id == (size_extracted - 1):
                    print(seq_word[1], end="\n")
                    ws.write(seq_word[1]+"\n")
                    
            print("=== Random words ===")
            #print(how_similar_sequantially(sum_numarray, 5))
            radom_words = how_similar_randomly(sum_numarray, size_extracted)
            
            print(radom_words)
           
            for ran_id, ran_word in radom_words:
                print("A random sequence of words:", end=" ")
                for ran_word_idx in range(size_extracted):
                    if ran_word_idx < size_extracted - 1:
                        print(ran_word[ran_word_idx], end = " ")
                        wr.write(ran_word[ran_word_idx]+"\t")
                    elif ran_word_idx == size_extracted - 1:
                        print(ran_word[ran_word_idx])
                        wr.write(ran_word[ran_word_idx]+"\n")
            
            print()