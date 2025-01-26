import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='1234',db='Employee')
cur=mydb.cursor()
sql="insert into manager(id,name,address,salary) value(%s,%s,%s,%s)"




val1=(100,'akash','raiganj',50000.00)



val2=(101,'argha','malda',60000.00)
val3=(102,'prince','puruliya',70000.00)
cur.execute(sql,val3)
mydb.commit()
