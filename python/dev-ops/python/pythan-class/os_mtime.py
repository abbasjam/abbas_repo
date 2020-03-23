import os
import datetime
for paths,folders,files in os.walk("/home/student/sample"):
    for f in files:
        x=os.path.join(paths,f)
        z=os.path.getmtime(x)
        ct=time.ctime(z)
        print (x,"     ",z,"    ",ct)

