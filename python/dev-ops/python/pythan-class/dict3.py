print ("Dictionary Manipulation")
print ("-----------------------")
y={'Rollno':100,'Name':"Vani",'Mark':99}
print ("value of y is:",y)

x=y.copy()
print ("copied dictionary x is:",x)

val=y.get('Mark')
print ("Value using get() :",val)
y.clear()
print ("after clear() is:",y)
