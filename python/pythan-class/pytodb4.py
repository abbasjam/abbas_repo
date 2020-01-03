import pymysql
con=pymysql.connect("localhost","mgru","Hello12!","devops19")
cur=con.cursor()
cur.execute("delete from info where rollno=100")
con.commit()
con.close()
