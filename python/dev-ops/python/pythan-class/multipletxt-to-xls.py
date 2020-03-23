import xlsxwriter
import glob

read_files = glob.glob("*.txt")

workbook = xlsxwriter.Workbook('write_dict.xlsx')
worksheet = workbook.add_worksheet()
col=0

ans = {}
final_dist = {}
counter=1

read_file = glob.glob("*.txt")

for f in read_files:

    txtfile = open("f", 'r')
    for line in txtfile:
        if (line == "\n"):
            counter+=1
            answer={}
            continue
        k, v = line.strip().split(':')
        answer[k.strip()] = v.strip()
        final_dict[counter] = answer
        txtfile.close()

print (final_dict)












