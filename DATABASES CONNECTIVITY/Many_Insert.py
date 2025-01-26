import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='1234',db='Employee')
cur=mydb.cursor()
sql="insert into manager(id,name,address,salary)values(%s,%s,%s,%s)"
val=[(100,'sky','itahar','120000.20'),(200,'prince','bihar','50000.20'),(300,'argha','malda','40000.20'),(400,'shubhankar','kolkata','70000.20'),(500,'akash','kolkata','80000.20')]
cur.executemany(sql,val)
mydb.commit()