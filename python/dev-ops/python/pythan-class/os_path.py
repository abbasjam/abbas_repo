import os
for paths,folders,files in os.walk("/home/student/oswalk"):
    for f in files:
        x=os.path.join(paths,f)
        print (x)
