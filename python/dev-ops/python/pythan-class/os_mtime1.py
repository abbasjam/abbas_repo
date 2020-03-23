import os
import datetime
for paths,folders,files in os.walk("/home/student/sample"):
    for f in files:
        x=os.path.join(paths,f)
        z=os.path.getmtime(x)
        df=datetime.datetime.fromtimestamp(z)
        d=df.date()
        print (x,"     ",z,"    ",df,"    ",d)

