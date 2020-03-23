import array
print ("Array Manipulation")
print ("-------------------")
x=array.array("i",[1,2,3,4,5])
print ("Given Array is :",x)

print ("Datatype of the array is :",x.typecode)
print ("Memory size for array variable:",x.itemsize)
print ("Buffer Infotrmation:",x.buffer_info())
