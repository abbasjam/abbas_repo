print ("Python to excel Process")
print ("----------------------")
import xlwt
wbv=xlwt.Workbook()
wsv=wbv.add_sheet("Information")
data=[[100,"Vani","MCA"],[101,"Karthi","MCA"],[102,"Anand","M.Sc"]]
r=0
c=0
for i in data:
    print (i)
    for j in i:
        print(j)
        wsv.write(r,c,j)
        c=c+1
    c=0
    r=r+1
wbv.save("info1.xls")


