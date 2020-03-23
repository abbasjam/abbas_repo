import xlsxwriter
import glob
workbook = xlsxwriter.Workbook('write_dict.xlsx')
worksheet = workbook.add_worksheet()
col=0
answer = {}
final_dict = {}
counter = 1
read_files = glob.glob("*.txt")

for txtfile in read_files:
    f = open(txtfile, 'r')
    for line in f:
        if (line == "\n"):
            counter+=1
            answer={}
            continue
        k, v = line.strip().split(':')
        answer[k.strip()] = v.strip()
        final_dict[counter] = answer
    f.close()
print (final_dict)
row = 0
worksheet.write(0,1,'Name')
worksheet.write(0,2,'Age')
worksheet.write(0,3,'Sex')
datalist=[]
for itm in final_dict:
    na=final_dict[itm]["Name"]
    ag=final_dict[itm]["Age"]
    sx=final_dict[itm]["Sex"]
    datalist.append(na)
    datalist.append(ag)
    datalist.append(sx)
    print (datalist)
    row += 1
    worksheet.write(row,0,itm)
    for col, prop in enumerate(datalist):
        worksheet.write(row,col+1,prop)
    datalist=[]
workbook.close()












