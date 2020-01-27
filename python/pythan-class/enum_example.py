print ("Python to excel Process")
print ("----------------------")
data=[[100,"Vani","MCA"],[101,"Karthi","MCA"],[102,"Anand","M.Sc"]]
'''for i,row in enumerate(data):
    print (i,row)
    for j,col in enumerate(row):
        print(j,col)'''
        
for i,row in enumerate(data):
    for j,col in enumerate(row):
        print(i,j,col)
