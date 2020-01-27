try:
    print ("Exception Handling")
    print ("------------------")
    import pymysql
    con=pymysql.connect("localhost","mgru","Hello12","devops19")
    x=input("Enter the number:")
    y=input("Enter the number:")
    x=int(x)
    y=int(y)
    z=x/y
    print ("Divided value is:",z)
except ValueError:
    print ("Instead of giving number you are trying to give string!!!!!")
except ZeroDivisionError:
    print ("trying to divide the number by zero which is not possible in System!!!!!!!!!!!!!!!!")
except :
    print ("Contact System Admin!!!!!!!!!!!!!!")


