print ("List Manipulations")
print ("------------------")

x=[100,"BSS",99.9,89+9j,"Python",100,200,100,567,100,"CSS"]
print ("Given List is:",x)

x.remove("Python")
print ("After the remove() x is:",x)

d=x.pop()
print ("After pop() x is :",x)
print ("Poped value is :",d)



x.clear()
print ("after clear() x is:",x)
