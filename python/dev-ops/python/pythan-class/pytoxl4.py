print ("Python to excel Process")
print ("----------------------")
import xlwt
wbv=xlwt.Workbook()
wsv=wbv.add_sheet("data")
heading=["Rollno","Name","Qualification"]
hf=xlwt.easyxf('font:bold on;align: wrap on,vert center,horiz center')
for i,value in enumerate(heading):
    wsv.write(0,i,value,hf)
    
data=[[100,"Vani","MCA"],[101,"Karthi","MCA"],[102,"Anand","M.Sc"]]
        
for i,row in enumerate(data):
    for j,col in enumerate(row):
        print(i,j,col)
        wsv.write(i+1,j,col,hf)
wbv.save("info3.xls")
