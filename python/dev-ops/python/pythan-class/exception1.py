import pymysql
con=pymysql.connect("localhost","mgru","Hello12","devops19")
print ("Exception Handling")
print ("-----------------")
x=input("Enter the number:")
y=input("Enter the number:")
x=int(x)
y=int(y)
z=x/y
print ("Divided value is:",z)

