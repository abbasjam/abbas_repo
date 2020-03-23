import pymysql
con=pymysql.connect("localhost","mgru","Hello12!","devops19")
cur=con.cursor()
cur.execute("select * from info")
results=cur.fetchall()
print (results)

con.close()
