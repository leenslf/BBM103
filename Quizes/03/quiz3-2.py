# Leen Said 2220356194
import sys

# get input
inp=(sys.argv[1])
# split the string at comma
list_1=inp.split(",")
# slice list every other word 
list_2=list_1[0:len(list_1)+1:2]
# remove every 3rd number from the list
num=len(list_2)//3
for k in range(0,num):
    u=2+(3*k)-(1*k)
    z=list_2[u]
    list_2.remove(z)

# remove every 7th number from the list
num_2=len(list_2)//7
for i in range(0,num_2):
    w=6+(7*i)-(1*i)
    y=list_2[w]
    

# print the output
print("Output : ",end="")
for q in list_2:
    print(q,end=" ")
