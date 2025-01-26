import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='1234',db='resort')
cur=mydb.cursor()
#1st....Create Database.....
create="create database resort"
cur.execute(create)
#2nd....create table.....
table="create table room(id int,location varchar(30),rent float,fllor int)"
cur.execute(table)
#3rd.... insert 10 records.....
insert="insert into room(id,location,rent,fllor)values(%s,%s,%s,%s)"
val=[(150,'raiganj',2000,1),
     (151,'malda',3000,2),
     (152,'adra',2500,3),
     (153,'kolkata',4000,4),
     (154,'puruliya',5000,5),
     (155,'medinapur',2800,6),
     (156,'itahar',6000,7),
     (157,'siliguri',7000,8),
     (158,'bankura',8000,9),
     (159,'barrackpore',1000,10)]
cur.executemany(insert,val) 
mydb.commit()
#4th.....Fetch all records.......
# fetch="select *from room"
# cur.execute(fetch)
# result=cur.fetchall()
# for data in result:
#     print(data)
#5th......update rent....
# update="update room set rent=rent+600 where rent<3000"
# cur.execute(update)
# mydb.commit()
#6th......delete record... id=154....
# delet="delete from room where id=154"
# cur.execute(delet)
# mydb.commit()