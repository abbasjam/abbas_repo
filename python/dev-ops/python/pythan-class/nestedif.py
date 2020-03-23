x=int(input("Enter the value for x:"))
y=int(input("Enter the value for y:"))
z=int(input("Enter the value for z:"))
a=int(input("Enter the value for a:"))
if x>y:
    if x>z:
        if x>a:
            print ("x is greatest among all")
        else:
            print ("x is not greater of a")
    else:
        print ("x is not greater than z")
else:
    print ("x is not greater than y")


if x>y and x>z and x>a:
    print ("x is greatest")
else:
    print ("x is not greater")

