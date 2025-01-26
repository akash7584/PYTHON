import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='1234')
print(mydb.connection_id)
cur=mydb.cursor()
cur.execute("create database Employee")