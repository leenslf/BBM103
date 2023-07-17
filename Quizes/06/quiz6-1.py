# Leen Said 2220356194
import sys
num=int(sys.argv[1])
def diamond_upper(n,sub,counter):
    if n==counter:
        return
    print((" "*(n-sub))+"*"+("*"*counter*2))
    
    return diamond_upper(n,sub+1,counter+1)

def diamond_lower(n,sub,counter):
    if n==counter+1:
        return
    print((" "*sub)+"*"+("*"*(n-sub-1)*2))
    
    return diamond_lower(n,sub+1,counter+1)

sub=1
counter=0
diamond_upper(num,sub,counter)
diamond_lower(num,sub,counter)