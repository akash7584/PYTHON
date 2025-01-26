import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='1234',db='employee')
cur=mydb.cursor()
D="delete from manager where id=200"
cur.execute(D)
mydb.commit()