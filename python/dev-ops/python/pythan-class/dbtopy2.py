import pymysql
con=pymysql.connect("localhost","mgru","Hello12!","devops19")
cur=con.cursor()
cur.execute("select * from info where rollno>=102")
rc=cur.rowcount
print ("Total number of records fetched:",rc)
for i in range(rc):
    result=cur.fetchone()
    print (result)
con.close()
