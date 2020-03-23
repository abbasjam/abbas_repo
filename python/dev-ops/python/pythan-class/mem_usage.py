import psutil
import pymysql
import datetime
import matplotlib.pyplot as p
def draw_mem_graph(y1):
    xaxis=['Tot_mem','mem_given_without_swap','usage %','used','free','active','inactive','buffers','catched','shared','slab']
    p.bar(xaxis,y1,width=0.3)
    p.xlabel("Memory Usage")
    p.ylabel("Memory details  in GB")
    p.title("Memory Usage Details")
    p.show()
try:
    x=psutil.virtual_memory()
    y=[]
    for i in x:
        j=0
        y.append(i/(1024**2))
        if j==2:
            y[2]=i
    print y
    '''conn=pymysql.connect("localhost","vani","vani123","monitoring")
    cur=conn.cursor()
    cdate=datetime.datetime.now()
    cur.execute("insert into men__usage values('%s','%d','%f','%d','%d','%d','%d','%d','%d','%d','%d','%d')"%(cdate,y[0],y[1],y[2],y[3]),y[4],y[5],y[6],y[8],y[9],y[10])
    conn.commit()
    conn.close()'''
except pymysql.err.InternalError:
    print "Database Conncection Error"
else:
    draw_mem_graph(y)


