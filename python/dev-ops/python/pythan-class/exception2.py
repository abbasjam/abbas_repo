try:
    print ("Exception Handling")
    print ("-----------------")
    x=input("Enter the number:")
    y=input("Enter the number:")
    x=int(x)
    y=int(y)
    z=x/y
    print ("Divided value is:",z)
except ValueError:
    print ("Instead of giving number you are trying to give string!!!!!")


