import os
import fnmatch
import collections
#from tqdm import tqdm

def print_file(input_file, output_file):
    with open(input_file, "r") as f:
        temp_sentences = [x for x in f.readlines() if x != "\n"]
        
    # Check if the length of files is greater than or equal to 4.
    # 2 inlcudes <doc id= ...> and </doc> 
    if len(temp_sentences) <= 5:
        return
    
    with open(output_file, "w") as wf:            
        # divide it inot each doc  
        for idx, val in enumerate(temp_sentences):     
            if val.find("<doc id=") != -1:
                wf.write(val)
            elif val.find("</doc>") != -1:
                wf.write(val)
            elif val.find("</math>") != -1:
                wf.write(val)
            ## I have to separate below
            ## 변의 둘째, 셋째 그리고 넷째 항을 왼쪽으로 옮기면 뉴튼의 운동 방정식과 비슷한 꼴의 운동방정식이 된다.
            ## formula_31
            #elif len(temp_sentences[temp_idx].split()) == -1:
            #continue
            else:
                wf.write(val)

    print(output_file, "is done!")
            
    
            
# Destination of this job
DESTINATION = "long_contents"

# Root dir of source
STARTING_POINT = "divided"

# Under current dir and divied dir
# removal of normalized, 
# ["original", "normalized"] -> ["original"]
ROOT = ["original"]
# Under original and normalized dir of current
DIR = ["AA", "AB", "AC", "AD", "AE", "AF"]
# The number of files under original/AA .. AF, total starting of file name is zero-based
# AA .. AE = 100 (00 .. 99)
# AF = 63( 00 .. 62)
NUM_FILE = [100, 63]

# prefix of each files 
WIKI_NAME = "wiki_"


for idx, val in enumerate(DIR):
    input_dir = STARTING_POINT+"/"+ROOT[0]+"/"+val
    output_dir = STARTING_POINT+"/"+DESTINATION+"/"+val
    if val != "AF": # 00..99
        for k in range(NUM_FILE[0]):
            if k < 10:
                middle_input_dir = input_dir+"/"+WIKI_NAME+"0"+str(k)
                middle_output_dir = output_dir+"/"+WIKI_NAME+"0"+str(k)
            else:
                middle_input_dir = input_dir+"/"+WIKI_NAME+str(k)
                middle_output_dir = output_dir+"/"+WIKI_NAME+str(k)
            
            # list files of a directory in a path
            list_of_dir = os.listdir(middle_input_dir)
            pattern = "wiki_*"
            
            # check if the directory is empty
            if len(list_of_dir) != 0:
                # check if the directory exits
                if not os.path.exists(middle_output_dir):
                    os.makedirs(middle_output_dir)   
            
            # checking if the pattern is indentical to the variable of patterns above like "wiki_**
            # entry is the same from a factor
            for entry in list_of_dir:
                if fnmatch.fnmatch(entry, pattern):
                    final_input_file = middle_input_dir+"/"+entry
                    final_output_file = middle_output_dir+"/"+entry
                    # write the file greater than or equal to the number of four
                    print_file(final_input_file, final_output_file)
                
    else: #00 .. 62
        for k in range(NUM_FILE[1]):
            if k < 10:
                middle_input_dir = input_dir+"/"+WIKI_NAME+"0"+str(k)
                middle_output_dir = output_dir+"/"+WIKI_NAME+"0"+str(k)
            else:
                middle_input_dir = input_dir+"/"+WIKI_NAME+str(k)
                middle_output_dir = output_dir+"/"+WIKI_NAME+str(k)
            
            # list files of a directory in a path
            list_of_dir = os.listdir(middle_input_dir)
            pattern = "wiki_*"
            
            # check if the directory is empty
            if len(list_of_dir) != 0:
                # check if the directory exits
                if not os.path.exists(middle_output_dir):
                    os.makedirs(middle_output_dir)      
             
            # checking
            for entry in list_of_dir:
                if fnmatch.fnmatch(entry, pattern):
                    final_input_file = middle_input_dir+"/"+entry
                    final_output_file = middle_output_dir+"/"+entry
                    #print(final_input_file, final_output_file)
                    # write the file greater than or equal to the number of four
                    print_file(final_input_file, final_output_file)
                    
print("finally everywork is done!!")
