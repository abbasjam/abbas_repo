import re
fp=open("mailids.txt","r")
c=[]
for i in fp:
   x=re.findall('[\w\.]+@[\w\.]+',i)
   print (x)
   if len(x)!=0:
       for j in x:
           c.append(j)
print (c)    


