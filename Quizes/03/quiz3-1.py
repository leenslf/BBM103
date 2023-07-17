# Leen Said 2220356194
import sys
# get input of the base number
first = int(sys.argv[1])
# get input of the power 
second = int(sys.argv[2])
# compute the number
number=first**second
# turn integer to string
str_number=str(number)
# create an empty tuple
tuplee=()
sum=0
# loop that terminates when the number of digits = 1
print("Output : ",first,"^",second,"= ",end='')
while len(str_number)>1:
    # add the digits to the tuple
    for i in str_number:
        tuplee=tuplee+(i,)
    # sum the contents of the tuple
    for k in range(len(tuplee)): # ('3','2')
        sum=sum+int(tuplee[k])
        # A = 1
        # # create a result list
        # result = []
        # for i in range(0, len(tuplee[k]), A):
        #     # convert to int, after the slicing process
        #     result.append(int(tuplee[i : i + A]))

        # print("The resultant list : " + str(result))
    # set the the number to the sum of contents of tuple
    str_number=str(sum)
    # empty the tuple
    tuplee=()
    # set sum back to zero to compute a new sum if needed
    sum=0
    
# print the output
print(str_number)