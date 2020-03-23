print ("Python to excel Process")
print ("----------------------")
import xlwt
wbv=xlwt.Workbook()
wsv=wbv.add_sheet("data")
wsv.write_merge(0,6,0,0,"Column merge")
wbv.save("info5.xls")
