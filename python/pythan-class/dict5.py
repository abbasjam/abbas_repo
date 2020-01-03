print ("Dictionary Manipulation")
print ("-----------------------")
y={'Rollno':100,'Name':"Vani",'Mark':99}
print ("value of y is:",y)

v=y.pop('Name')
print ("Deleted Value is :",v)
print ("After Deleting y is :",y)
y.popitem()
print ("after popitem() y is:",y)

