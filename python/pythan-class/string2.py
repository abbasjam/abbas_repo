print ("String Manipulations")
print ("-------------------")

x="Brain Stack solutions"
print ("Value of x is:",x)
print ("value of x[6] is :",x[6])

print ("Using while Loop")
print ("----------------")
l=len(x)
print ("Total Number of characters are:",l)
i=0
while i<l:
    print (i,x[i])
    i=i+1


print ("Using for Loop")
print ("--------------")
for i in x:
    print (i)
