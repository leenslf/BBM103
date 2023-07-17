# Leen Said  2220356194
import sys

# sys arguments to read the inout and write the output
inp = sys.argv[1]
out = sys.argv[2]
# Function to read the lines from the input text file
def read():
    f0 = open(inp, "r")
    read = f0.readlines()
    return read

#  Function to write the output to the output text file
def export():
    f1 = open(out, "a")
    return f1 

lines = []
# read lines in the input file and sort them
for l in read():
    lines.append(l)
    lines.sort()

message_id=[]
# message_id list contains the message id of every single line
for k in lines:
    message_id.append(k[0:4])
# we need to turn message_id into a set that cannot contain duplicates
# this way we can identify the dictinct message_id numbers we have
message_id_set = set(message_id)

# create a dictionary where the keys are the message_id and the values 
# are a list of lists of messages with identical message_id
dictionary_of_messages={}
common_message_id=[]
for num in message_id_set:
    for message in lines:
        if message[0:4] == num:
            common_message_id.append(message)
    dictionary_of_messages[num] = common_message_id
    common_message_id=[]

# sort message_id_set in the ascending order
sorted_set=sorted(message_id_set)
e=export()
nums=1
for i in sorted_set:
    write_this=("Message ",str(nums),"\n")
    nums+=1
    e.writelines(write_this)
    write_this = dictionary_of_messages[str(i)]
    e.writelines(write_this)