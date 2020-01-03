print ("Python to excel Process")
print ("----------------------")
import xlwt
wbv=xlwt.Workbook()
wsv=wbv.add_sheet("data")
wsv.write_merge(0,0,0,6,"Column merge")
wbv.save("info4.xls")
