import array
print ("Array Manipulation")
print ("-------------------")
x=array.array("i",[1,2,3,4,5])
print ("Given Array is :",x)
for i in x:
    print (i)
x[0]=1.23
print (x)
