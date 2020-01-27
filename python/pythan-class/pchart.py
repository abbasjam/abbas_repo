import matplotlib.pyplot as p
values=[23,27,35,15]
c=["red","green","yellow","cyan"]
la=["sports","Co-Curriculur","Academic","extra-curriculur"]
p.pie(values,labels=la,colors=c,startangle=90,shadow=True,explode=(0.1,0,0.1,0),autopct="%1.1F%%")
p.legend()
p.show()


