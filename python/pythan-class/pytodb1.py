import pymysql
con=pymysql.connect("localhost","mgru","Hello12!","devops19")
cur=con.cursor()
cur.execute("insert into info values(101,'Anand')")
con.commit()
con.close()
