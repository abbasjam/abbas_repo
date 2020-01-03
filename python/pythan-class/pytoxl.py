print ("Python to excel Process")
print ("----------------------")
import xlwt
wbv=xlwt.Workbook()
wsv=wbv.add_sheet("Information")
wsv.write(0,0,100)
wsv.write(0,1,"Vani")
wsv.write(0,2,"MCA")
wsv.write(1,0,101)
wsv.write(1,1,"Gokul")
wsv.write(1,2,"B.E")
wbv.save("info.xls")


