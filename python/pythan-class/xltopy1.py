print ("excel to python process")
print ("-----------------------")
import xlrd
wbv=xlrd.open_workbook("info1.xls")
ns=wbv.nsheets
sn=wbv.sheet_names()
print ("Number of sheets in the info1.xls is:",ns)
print ("sheet Names are :",sn)
wsv=wbv.sheet_by_name("Information")
nr=wsv.nrows
nc=wsv.ncols
data=[]
print ("total number of rows contain data:",nr)
print ("Total number of colums contain data:",nc)
for i in range(nr):
    for j in range(nc):
        v=wsv.cell(i,j).value
        print (v)
        data.append(v)
print (data)
