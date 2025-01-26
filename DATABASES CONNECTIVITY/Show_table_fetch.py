import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='1234',db='employee')
cur=mydb.cursor()
S="select *from manager"
cur.execute(S)
result=cur.fetchall()
for data in result:
    print(data)