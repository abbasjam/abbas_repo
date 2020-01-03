print ("List Manipulations")
print ("------------------")

x=[100,"BSS",99.9,89+9j]
print ("Value of x is :",x)

x.append("Python")
print ("After Appending the single value:",x)

y=[100,200,300,400,500]
x.append(y)
print ("After Append the list:",x)
print (x[5])
print (x[5][2])
print (x[2])


z=[1,2,3,4,5]
x.extend(z)
print ("After Extending z x is :",x)

x.insert(2,"Python")
print("After inserting x is :",x)

z1=[12,13,14]
x.insert(3,z1)
print ("After inserting x is:",x)
