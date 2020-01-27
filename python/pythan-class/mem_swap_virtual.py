import matplotlib.pyplot as p
import psutil
def create_plot(ptype):
    if ptype=='swap':
        x=["TSM","TSU","FS0","Usage%","_swapped_in","swapped _out"]
    if ptype=='virtual':        
        x=['Phy_Mem','Mem_Without_Swap','usage %','used','free','active','inactive','buffers','catched','shared','slab']
    return x

p.style.use('fivethirtyeight')
f=p.figure()

p1=f.add_subplot(211)
ans1=psutil.virtual_memory()
x1=create_plot('virtual')
y1=[]
for i in ans1:
    j=0
    y1.append(i/(1024**2))
    if j==2:
        y1[2]=i
p.bar(x1,y1,width=0.2)
p.title('Virtual Memory Details')
p.xlabel("Virtual memory usage")
p.ylabel("Memory usage in MB")

p2=f.add_subplot(212)
x=create_plot('swap')
ans=psutil.swap_memory()
y=[]
for i in ans:
    y.append(i)
p.bar(x,y,color=('b','r','g','y','r','g'),width=0.2)
p.title('Swap Memory Details')
p.xlabel("Swap Memory Usage")
p.ylabel("Memory usage in bytes")



p.subplots_adjust(hspace=0.3,wspace=0.3)
p.show()        

