import os
if (os.access("/home/student/os_mtime1.py",os.X_OK)):
    print ("Executable file")
else:
    print ("Not Executable file")

