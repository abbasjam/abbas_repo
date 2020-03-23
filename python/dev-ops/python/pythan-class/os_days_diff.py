import os
import datetime
for paths,folders,files in os.walk("/home/student/sample"):
    for f in files:
        x=os.path.join(paths,f)
        z=os.path.getmtime(x)
        df=datetime.datetime.fromtimestamp(z)
        cd=df.date()
        td=datetime.datetime.today()
        td=td.date()
        diff=td-cd
        print ("Difference is :",diff)
        print ("Differece in number:",diff.days)

