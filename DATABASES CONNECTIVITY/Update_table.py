import mysql.connector
mydb1=mysql.connector.connect(host='localhost',user='root',password='1234',db='employee')
cur=mydb1.cursor()
s=" update manager set address=barrackpore where address=kolkata "
cur.execute(s)
mydb1.commit()