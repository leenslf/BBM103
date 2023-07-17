#Name: Leen Said
#Student no: 2220356194
import sys #import sys module
twoPointers = int(sys.argv[1]) #get input from user
threePointers = int(sys.argv[2])
freeThrows = int(sys.argv[3])

# multiply the points and find the total sum
score = freeThrows + (twoPointers * 2) + (threePointers * 3)
    # return score
print(score)
