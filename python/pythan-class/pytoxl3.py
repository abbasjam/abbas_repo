print ("Python to excel Process")
print ("----------------------")
import xlwt
wbv=xlwt.Workbook()
wsv=wbv.add_sheet("data")
data=[[100,"Vani","MCA"],[101,"Karthi","MCA"],[102,"Anand","M.Sc"]]
        
for i,row in enumerate(data):
    for j,col in enumerate(row):
        print(i,j,col)
        wsv.write(i,j,col)
wbv.save("info2.xls")
