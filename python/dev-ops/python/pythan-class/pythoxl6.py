print ("Python to excel Process")
print ("----------------------")
import xlwt
wbv=xlwt.Workbook()
wsv=wbv.add_sheet("data")
wsv.write_merge(0,4,0,6,"Column merge")
wbv.save("info6.xls")
