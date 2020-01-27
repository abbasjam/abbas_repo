import psutil
import pymysql
import datetime
import matplotlib.pyplot as p
def draw_network_io_graph(y1):
    xaxis=['bytes_sent','bytes_recv','pack_sent','pack_recv','Tot_Err_in_recv','Tot_err_in_send',"incoming_pac_dropout",'outgoing_packes_dropout']
    p.bar(xaxis,y1,width=0.3)
    p.xlabel("Networking I/O Attributes")
    p.ylabel("Total Count in number")
    p.title("Network I/O Attributes")
    p.show()
try:
    x=psutil.net_io_counters()
    y=[]
    for i in x:
        y.append(i)
    print y
    '''conn=pymysql.connect("localhost","vani","vani123","monitoring")
    cur=conn.cursor()
    cdate=datetime.datetime.now()
    cur.execute("insert into disk_usage values('%s','%d','%d','%d','%f')"%(cdate,y[0],y[1],y[2],y[3]))
    conn.commit()
    conn.close()'''
except pymysql.err.InternalError:
    print "Database Conncection Error"
else:
    draw_network_io_graph(y)




