import pymysql
con=pymysql.connect("localhost","mgru","Hello12!","devops19")
cur=con.cursor()
cur.execute("update info set name='Vanikarth' where rollno=100")
con.commit()
con.close()
