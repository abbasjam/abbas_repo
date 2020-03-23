f=open("classtest.py","r")
print(f.read())
print("Tested")
f=open("classtest.py","a")
f.write("test added using new write option")

f=open("classtest.py","r")
print (f.read())
