print ("file Handling")
print ("------------")
fp=open("sample1.txt","r")
i=fp.readlines()
print(i)
for j in i:
    print (j)
fp.close()
