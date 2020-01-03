print ("Dictionary Manipulation")
print ("-----------------------")
x={100:"BSS",101:99,102:"Python"}
y={'Rollno':100,'Name':"Vani",'Mark':99}
z={1000:100,'Name':"Python",2000:"Good"}
print ("Value of x is:",x)
print ("value of y is:",y)
print ("Value of z is :",z)
print (y['Name'])
print (z[1000])

print ("Using for  loop")
print ("----------------")
for i in x:
    print (i,x[i])
