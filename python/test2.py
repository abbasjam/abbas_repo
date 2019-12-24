
x=[12,13,12]
y=x.copy()
print ("y value of ",y)
print ("x value of ",x)

for i in x:
    for j in y:
        if i==j:
            del y[i]
        else:
            print(i)

