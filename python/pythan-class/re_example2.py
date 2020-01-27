import re
c=0
fp=open("demo.txt","r")
for i in fp:
    if re.search(' was ',i):
        c=c+1
print ("Total Number of occurence:",c)


