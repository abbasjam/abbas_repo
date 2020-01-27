import matplotlib.pyplot as p
import psutil
def create_plot(ptype):
    if ptype=='swap':
        x=["Tot_Swap_Mem","Used","Free","Usage%","_swapped_in","swapped _out"]
    if ptype=='virtual':        
       x=['Total_Physical_Memory','Memory _given_Without_Swap']
    if ptype=='virtual_other':
       x=['usage %','used','free','active','inactive','buffers','catched','shared','slab']
    return x

p.style.use('fivethirtyeight')
f=p.figure()

ans1=psutil.virtual_memory()

p1=f.add_subplot(311)
ans1=psutil.virtual_memory()
x1=create_plot('virtual')
y1=[]
y1.append(ans1[0]/(1024**2))
y1.append(ans1[1]/(1024**2))
p.bar(x1,y1,width=0.03)
p.title('Virtual Memory usage Main_Metrices Details')
p.ylabel("Memory usage in MB")


p1=f.add_subplot(312)
y2=[]
x2=create_plot('virtual_other')
for i in range(2,len(ans1)):
    if i==2:
        y2.append(ans1[i])
    else:
	y2.append(ans1[i]/(1024**2))
p.bar(x2,y2,width=0.2)
p.title("Virtual memory usage Dtails Main_Metrices")
p.ylabel("Memory usage in MB")

p2=f.add_subplot(313)
x3=create_plot('swap')
ans=psutil.swap_memory()
y3=[]
for i in ans:
    y3.append(i)
p.bar(x3,y3,color=('b','r','g','y','r','g'),width=0.2)
p.title('Swap Memory Details')
p.ylabel("Memory usage in bytes")



p.subplots_adjust(hspace=0.3,wspace=0.3)
p.show()        

