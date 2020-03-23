import array
print ("Array Manipulation")
print ("-------------------")
x=array.array("i",[1,2,3,4,5])
print ("Given Array is :",x)
y=x.tolist()
print ("y is :",y)
x.pop(1)
print ("after pop(1):",x)
x.pop()
print ("after pop():",x)
x.remove(4)
print ("after remove(4):",x)

