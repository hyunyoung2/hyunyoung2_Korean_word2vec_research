# divid document 
# <doc id=...> ... <doc> is a document
import os
from tqdm import tqdm

def print_file(input_file, output_dir):
    with open(input_file, "r") as f:
        temp_sentences = [x for x in f.readlines()]

    # for numbering
    num_idx = 0

    # divide it inot each doc  
    for idx, val in tqdm(enumerate(temp_sentences)):
        if val.find("<doc id=") != -1:
            if num_idx < 10:
                # location_file = the location of file + file name
                write_file = os.path.join(output_dir, WIKI_NAME+"0"+str(num_idx)+"0")
            elif num_idx < 100:
                write_file = os.path.join(output_dir, WIKI_NAME+"0"+str(num_idx))
            else: 
                write_file = os.path.join(output_dir, WIKI_NAME+str(num_idx))
            with open(write_file, "w") as wf:
                temp_idx = idx
                while temp_sentences[temp_idx].find("</doc>") == -1:
                    wf.write(temp_sentences[temp_idx])
                    temp_idx += 1
                wf.write(temp_sentences[temp_idx])
            num_idx += 1
        else:
            continue

# Under current dir and divied dir
ROOT = ["original",  "normalized"]
# Under original and normalized dir of current
DIR = ["AA", "AB", "AC", "AD", "AE", "AF"]
# The destination of dividing
DESTINATION = "divided"

# The number of files under original/AA .. AF, total starting of file name is zero-based
# AA .. AE = 100 (00 .. 99)
# AF = 63( 00 .. 62)
NUM_FILE = [100, 63]
# prefix of each files 
WIKI_NAME = "wiki_"

# for test of fucntion of print_file        
# path ="original/AA/wiki_00"
# path2 = "divided"+"/"+path
# print_file(path, path2)
for i in range(len(ROOT)):
    input_file = ""
    input_file += ROOT[i]
    for j in range(len(DIR)):
        middle_file = input_file+"/"+DIR[j]
        if DIR[j] != "AF": # 00 .. 99
            for k in range(NUM_FILE[0]):
                if k < 10:
                    final_input_file = middle_file+"/"+WIKI_NAME+"0"+str(k)
                else:
                    final_input_file = middle_file+"/"+WIKI_NAME+str(k)
                dest = DESTINATION+"/"+final_input_file
                # check if the directory exits
                if not os.path.exists(dest):
                    os.makedirs(dest)
                # print file
                print_file(final_input_file, dest)
        else: # 00 .. 62
            for k in range(NUM_FILE[1]):
                if k < 10:
                    final_input_file = middle_file+"/"+WIKI_NAME+"0"+str(k)
                else:
                    final_input_file = middle_file+"/"+WIKI_NAME+str(k)
                dest = DESTINATION+"/"+final_input_file
                # check if the directory exits
                if not os.path.exists(dest):
                    os.makedirs(dest)
                # print file
                print_file(final_input_file, dest)

print("all print file are done!!")
