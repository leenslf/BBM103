# Leen Said 2220356194
import sys

def diamond(n):
    listdiamond = [" "*(n-(1+i))+"*"+"*"*i*2 for i in range(n)]
    listdiamond +=  [" "*(1+(n-2-k))+"*"+"*"*k*2 for k in range(n-2,-1,-1)]
    for q in listdiamond:
        print(q)

num=sys.argv[1]
diamond(int(num))