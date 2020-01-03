import pymysql
con=pymysql.connect("localhost","mgru","Hello12!","devops19")
cur=con.cursor()
for i in range(3):
    rno=int(input("Enter the rollno:"))
    name=input("enter the name:")
    cur.execute("insert into info values('%d','%s')"%(rno,name))
con.commit()
con.close()
