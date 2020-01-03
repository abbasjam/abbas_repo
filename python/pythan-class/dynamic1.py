print ("Functions")
print ("----------")

def addition(*x):
    print (x)   
    s=0
    for i in x:
        s=s+i
    return s
    

a=addition(20,10)
print ("Added value is:",a)
b=addition(4,5,6)
print ("Added value is :",b)
