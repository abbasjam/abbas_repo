print ("List Manipulations")
print ("------------------")

x=[100,"BSS",99.9,89+9j,True,"Python","Vani"]
print ("Value of x is :",x)

print ("Using While loop")
print ("-----------------")
i=0
l=len(x)
print ("Total Number of Elements are :",l)
while i<l:
    print (x[i])
    i=i+1


print ("Using for loop")
print ("--------------")
for i in x:
    print (i)
