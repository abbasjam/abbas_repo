import pymysql
con=pymysql.connect("localhost","mgru","Hello12!","devops19")
cur=con.cursor()
cur.execute("create table info (rollno int,name varchar(20))")
con.commit()
con.close()
