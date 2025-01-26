import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='1234',db='Employee')
cur=mydb.cursor()
cur.execute("create table Manager(id int,name varchar(30),address varchar(30),salary float)");