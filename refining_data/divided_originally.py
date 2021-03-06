# divid document 
# <doc id=...> ... <doc> is a document
import os
#from tqdm import tqdm

def print_file(input_file, output_dir):
    with open(input_file, "r") as f:
        temp_sentences = [x for x in f.readlines()]
    
    # for numbering
    num_idx = 0
    
    # divide it inot each doc  
    for idx, val in enumerate(temp_sentences):
        if val.find("<doc id=") != -1:
            if num_idx < 10:
                # location_file = the location of file + file name
                write_file = os.path.join(output_dir, WIKI_NAME+"0"+"0"+str(num_idx))
            elif num_idx < 100:
                write_file = os.path.join(output_dir, WIKI_NAME+"0"+str(num_idx))
            else: 
                write_file = os.path.join(output_dir, WIKI_NAME+str(num_idx))
            with open(write_file, "w") as wf:
                temp_idx = idx
                while temp_sentences[temp_idx].find("</doc>") == -1:
                    if temp_sentences[temp_idx].find(",\n") != -1:
                        wf.write(temp_sentences[temp_idx][:temp_sentences[temp_idx].find("\n")]+" \n")
                    elif temp_sentences[temp_idx].find(".\n") != -1:
                        wf.write(temp_sentences[temp_idx][:temp_sentences[temp_idx].find("\n")]+" \n")
                    ## I have to separate below
                    ## sdfsdjsl</math>
                    #elif temp_sentences[temp_idx].find("</math>") != -1:
                        #continue
                    ## 우변의 둘째, 셋째 그리고 넷째 항을 왼쪽으로 옮기면 뉴튼의 운동 방정식과 비슷한 꼴의 운동방정식이 된다.
                    ## formula_31
                    #elif len(temp_sentences[temp_idx].split()) == -1:
                        #continue
                    else:
                        wf.write(temp_sentences[temp_idx])
                    temp_idx += 1
                wf.write(temp_sentences[temp_idx])
            num_idx += 1
            print(write_file, "is done!!")
        else:
            continue

# Under current dir and divied dir
# removal of normalized, 
# ["original", "normalized"] -> ["original"]
ROOT = ["original"]
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
    input_dir = ROOT[i]
    for j in range(len(DIR)):
        middle_dir = input_dir+"/"+DIR[j]
        if DIR[j] != "AF": # 00 .. 99
            for k in range(NUM_FILE[0]):
                if k < 10:
                    final_input_file = middle_dir+"/"+WIKI_NAME+"0"+str(k)
                else:
                    final_input_file = middle_dir+"/"+WIKI_NAME+str(k)
                dest = DESTINATION+"/"+final_input_file
                # check if the directory exits
                if not os.path.exists(dest):
                    os.makedirs(dest)
                # print file
                print_file(final_input_file, dest)
        else: # 00 .. 62
            for k in range(NUM_FILE[1]):
                if k < 10:
                    final_input_file = middle_dir+"/"+WIKI_NAME+"0"+str(k)
                else:
                    final_input_file = middle_dir+"/"+WIKI_NAME+str(k)
                dest = DESTINATION+"/"+final_input_file
                # check if the directory exits
                if not os.path.exists(dest):
                    os.makedirs(dest)
                # print file
                print_file(final_input_file, dest)
                
print("all print file are done!!")
