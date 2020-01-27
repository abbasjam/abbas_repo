from Tkinter import *
import matplotlib.pyplot as p
import psutil,os
def draw_virtual_main_graph():
    ans1=psutil.virtual_memory()
    x1=['Total_Physical_Memory','Memory _given_Without_Swap']
    y1=[]
    y1.append(ans1[0]/(1024**2))
    y1.append(ans1[1]/(1024**2))
    p.bar(x1,y1,width=0.03)
    p.title('Virtual Memory usage Main_Metrices Details')
    p.xlabel("VM Main Metrices")
    p.ylabel("Memory usage in MB")
    p.show()

def draw_virtual_other_graph():
    ans1=psutil.virtual_memory()
    y2=[]
    x2=['usage %','used','free','active','inactive','buffers','catched','shared','slab']
    for i in range(2,len(ans1)):
        if i==2:
            y2.append(ans1[i])
        else:
	    y2.append(ans1[i]/(1024**2))
    p.bar(x2,y2,width=0.2)
    p.title("Virtual memory usage Dtails Other_Metrices")
    p.xlabel("VM Other Metrics")
    p.ylabel("Memory usage in MB")
    p.show()

def draw_swap_graph():
    x3=["Tot_Swap_Mem","Used","Free","Usage%","_swapped_in","swapped _out"]
    ans=psutil.swap_memory()
    y3=[]
    for i in ans:
        y3.append(i)
    p.bar(x3,y3,color=('b','r','g','y','r','g'),width=0.2)
    p.title('Swap Memory Details')
    p.xlabel("Swap Memory")
    p.ylabel("Memory usage in bytes")
    p.show()    

    
def draw_network_io_graph():
    x=psutil.net_io_counters()
    y=[]
    for i in x:
        y.append(i)
    xaxis=['bytes_sent','bytes_recv','pack_sent','pack_recv','Tot_Err_in_recv','Tot_err_in_send',"incoming_pac_dropout",'outgoing_packes_dropout']
    p.bar(xaxis,y,width=0.3)
    p.xlabel("Networking I/O Attributes")
    p.ylabel("Total Count in number")
    p.title("Network I/O Attributes")
    p.show()

def draw_disk_usage_graph():
    x=psutil.disk_usage("/")
    y=[]
    for i in x:
        y.append(i/(1024**3))
    y[len(y)-1]=x[3]
    xaxis=['Totalspace','Used','Free','usage in %']
    p.bar(xaxis,y,color=['b','r','g','y'],width=0.3)
    p.xlabel("Disk Usage")
    p.ylabel("Disk space in GB")
    p.title("Disk Usage Details")
    p.show()

def draw_cpu_times_graph():
    x=psutil.cpu_times()
    y=[]
    for i in x:
        y.append(i/60)
    y.append(psutil.cpu_count(logical=True))
    y.append(psutil.cpu_count(logical=False))
    xaxis=['TSIUM','TSIKM','Idle_time','TSPIPPIUM','TS_I/O','TSFSHI',"TSFSSI","TSFOOSIVE",'TSFVOS','TSFRNG','LCPU','PHCPU']
    p.bar(xaxis,y,width=0.3)
    p.xlabel("CPU Times Details")
    p.ylabel("CPU Times in minutes")
    p.title("CPU - Usage - Time Details")
    p.show()

i=1
while(i!=5):
    os.system("clear")
    print ("1.virtual memory")
    print ("2.Network details")
    print ("5.Exit")
    i=input("Enter the Choice:")
    if i==1:
        draw_virtual_main_graph()
    if i==2:
        draw_network_io_graph()


  

