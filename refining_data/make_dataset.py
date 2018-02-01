import os 
import fnmatch

# Destination of this job
OUTPUT_DIR = "../dataset"

DESTINATION_FILE = ["contents", "title"]

OUTPUT_FILE_CONTENTS = OUTPUT_DIR+"/"+DESTINATION_FILE[0]
OUTPUT_FILE_TITLE = OUTPUT_DIR+"/"+DESTINATION_FILE[1]


def print_file(input_file, wc, wt):
    with open(input_file, "r") as f:
        temp_sentences = [x for x in f.readlines() if x != "\n"]
    
    #print(temp_sentences[0:2])
    #check title_flag
    title_flag = False
    temp_title= ""
    temp_str = ""
    
    for idx, val in enumerate(temp_sentences):
        if val.find("<doc id=") != -1 and title_flag == False:
            if val.find("title=") != -1:
                title_flag = True
                # extract the title in <doc id = ~~~
                temp_title = val[val.find("title=")+6:-2]
            else:
                print("error!")
        elif idx == 1 and title_flag == True:
            #  compare <doc id=... title="~~" with second line
            if val[:-1] == temp_title:
                wt.write(val)
                title_flag = False
            else:
                print("error!!")
        elif val.find("</doc>") != -1 and title_flag == False:
            if temp_str != "":
                wc.write(temp_str+"\n")
                temp_str = ""
            else:
                print("error!!!")
        else:
            temp_str += val[:val.find("\n")]
            #if idx < 5:
               # print(temp_str)

             
# Root dir of source
STARTING_POINT = "normalized"

# Under current dir and divied dir
# removal of normalized, 
# ["original", "normalized"] -> ["original"]
ROOT = ["long_contents"]
# Under original and normalized dir of current
DIR = ["AA"] # "AB", "AC", "AD", "AE", "AF"]
# The number of files under original/AA .. AF, total starting of file name is zero-based
# AA .. AE = 100 (00 .. 99)
# AF = 63( 00 .. 62)
NUM_FILE = [4] # 100, 63]

# prefix of each files 
WIKI_NAME = "wiki_"


with open(OUTPUT_FILE_CONTENTS, "w") as wc:
    with open(OUTPUT_FILE_TITLE, "w") as wt:
        for idx, val in enumerate(DIR):
            input_dir = STARTING_POINT+"/"+ROOT[0]+"/"+val  
            if val != "AF": # 00..99
                for k in range(NUM_FILE[0]):
                    if k < 10:
                        middle_input_dir = input_dir+"/"+WIKI_NAME+"0"+str(k)
                    else:
                        middle_input_dir = input_dir+"/"+WIKI_NAME+str(k)

                    # list files of a directory in a path
                    list_of_dir = os.listdir(middle_input_dir)
                    pattern = "wiki_*"
                    
                    if len(list_of_dir) == 0:
                        print("error!")
                        break
                    
                    list_of_dir.sort()
                    #print(list_of_dir[0:5])
                    # checking if the pattern is indentical to the variable of patterns above like "wiki_**
                    # entry is the same from a factor
                    for entry in list_of_dir:
                        if fnmatch.fnmatch(entry, pattern):
                            final_input_file = middle_input_dir+"/"+entry
                            #print(final_input_file)
                            # write the file greater than or equal to the number of four
                            print_file(final_input_file, wc, wt)

            else: #00 .. 62
                for k in range(NUM_FILE[1]):
                    if k < 10:
                        middle_input_dir = input_dir+"/"+WIKI_NAME+"0"+str(k)  
                    else:
                        middle_input_dir = input_dir+"/"+WIKI_NAME+str(k)        

                    # list files of a directory in a path
                    list_of_dir = os.listdir(middle_input_dir)
                    pattern = "wiki_*"

                    if len(list_of_dir) == 0:
                        print("error!")
                        break   

                    list_of_dir.sort()
                    # checking
                    for entry in list_of_dir:
                        if fnmatch.fnmatch(entry, pattern):
                            final_input_file = middle_input_dir+"/"+entry
                            print(final_input_file)
                            # write the file greater than or equal to the number of four
                            print_file(final_input_file, wc, wt)
                
                    
print("making dataset is done!!")          
