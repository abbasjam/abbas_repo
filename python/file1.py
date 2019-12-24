f=open("classtest.py","r")
print(f.read())

f=open("classtest.py","a")
f.write("test added using new write option")

f=open("classtest.py","r")
print (f.read())


