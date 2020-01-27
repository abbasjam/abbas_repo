import os
for paths,folders,files in os.walk("/home/student/sample"):
    for f in files:
        x=os.path.join(paths,f)
        z=os.path.getsize(x)
        print (x,"     ",z)
