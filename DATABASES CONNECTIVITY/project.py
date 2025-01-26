from tkinter import* 
from tkinter import ttk
import tkinter.messagebox
import mysql.connector as mc

def reset():
    id.set("") 
    name.set("")
    address.set("")
    salary.set("")

def show():
    conn=mc.connect(host="localhost",user="root",password="1234",database="company")
    cur=conn.cursor()
    cur.execute("select * from employee")
    data=cur.fetchall()
    if len(data)!=0:
        table.delete(*table.get_children())
        for row in data:
            table.insert("",END,values=row)
    conn.close()

def add():
    conn=mc.connect(host="localhost",user="root",password="1234",database="company")
    cur=conn.cursor()
    cur.execute("insert into employee (name,address,salary) values (%s,%s,%s)",(
        name.get(),
        address.get(),
        salary.get()
    ))
    conn.commit()
    show()
    conn.close()
    tkinter.messagebox.showinfo("Result","Add Successfully")
    reset()


def info(e):
    viweinfo=table.focus()
    singledata=table.item(viweinfo)
    row=singledata['values']
    print(row)
    id.set(row[0])
    name.set(row[1])
    address.set(row[2])
    salary.set(row[3])

def update():
    conn=mc.connect(host="localhost",user="root",password="1234",database="company")
    cur=conn.cursor()
    cur.execute("update employee set name=%s,address=%s,salary=%s where id=%s",(
        name.get(),
        address.get(),
        salary.get(),
        id.get()
    ))
    conn.commit()
    show()
    conn.close()
    tkinter.messagebox.showinfo("Result","Update Successfully")
    reset()

def delete():
    conn=mc.connect(host="localhost",user="root",password="1234",database="company")
    cur=conn.cursor()
    cur.execute("delete from employee where id=%s",(id.get(),))
    conn.commit()
    show()
    conn.close()
    tkinter.messagebox.showinfo("Result","Delete Successfully")
    reset()     

def exit():
    exit=tkinter.messagebox.askyesno("Result","Confirm if you want to exit")
    if exit>0:
        win.destroy()
        return

win=Tk()
win.geometry("1420x800+0+0")
win.title("Education2All")
win.config(background="red")


id=StringVar()
name=StringVar()
address=StringVar()
salary=StringVar()


main_frame=Frame(win,bd=10,relief=RIDGE,width=2160,height=600)
main_frame.pack(pady=50)

title_frame=Frame(main_frame,bd=5,width=1300,height=100,relief=RIDGE)
title_frame.grid(row=0,column=0)

Labtitle=Label(title_frame,text="CRUD Operation in Mysql",font=("times new roman",50),background="blue",fg="white")
Labtitle.grid(row=0,column=0)

mid_frame=Frame(main_frame,bd=5,width=1240,height=800,relief=RIDGE,background="yellow")
mid_frame.grid(row=2,column=0)

from_frame=Frame(mid_frame,bd=5,width=1240,height=300,relief=RIDGE,background="brown")
from_frame.grid(row=0,column=0)

Button_frame=Frame(mid_frame,bd=5,width=1240,height=70,relief=RIDGE,background="white")
Button_frame.grid(row=1,column=0)

table_frame=Frame(mid_frame,bd=5,width=1240,height=300,relief=RIDGE,background="brown")
table_frame.grid(row=2,column=0)

#_____________________LEBEL__________________________
idlebel=Label(from_frame,text="ID",font=("tims new roman",20),width=20)
namelebel=Label(from_frame,text="Name",font=("tims new roman",20),width=20)
addresslebel=Label(from_frame,text="Address",font=("tims new roman",20),width=20)
salarylebel=Label(from_frame,text="Salary",font=("tims new roman",20),width=20)

idlebel.grid(row=0,column=0,padx=10,pady=10)
namelebel.grid(row=1,column=0,padx=10,pady=10)
addresslebel.grid(row=2,column=0,padx=10,pady=10)
salarylebel.grid(row=3,column=0,padx=10,pady=10)

#_____________________ENTRY______________________________
identry=Entry(from_frame,font=("times new roman",20),state="readonly",textvariable=id)
nameentry=Entry(from_frame,font=("times new roman",20),textvariable=name)
addressentry=Entry(from_frame,font=("times new roman",20),textvariable=address)
salaryentry=Entry(from_frame,font=("times new roman",20),textvariable=salary)
identry.grid(row=0,column=1)
nameentry.grid(row=1,column=1)
addressentry.grid(row=2,column=1)
salaryentry.grid(row=3,column=1)

#___________________BUTTON_____________________
addbtn=Button(Button_frame,text="Insert",font=("times new roman",15),width="20",command=add)
viewbtn=Button(Button_frame,text="View Record",font=("times new roman",15),width="20",command=show)
updatebtn=Button(Button_frame,text="Modify",font=("times new roman",15),width="20",command=update)
deletebtn=Button(Button_frame,text="Delete",font=("times new roman",15),width="20",command=delete)
resetbtn=Button(Button_frame,text="Reset",font=("times new roman",15),width="20",command=reset)
exitbtn=Button(Button_frame,text="Exit",font=("times new roman",15),width="20",command=exit)
addbtn.grid(row=0,column=0)
viewbtn.grid(row=0,column=1)
updatebtn.grid(row=0,column=2)
deletebtn.grid(row=0,column=3)
resetbtn.grid(row=0,column=4)
exitbtn.grid(row=0,column=5)

#______________________TREE VIEW______________
style=ttk.Style()
style.configure("mystyle.treeview",font=("times new roman",20),rowheight="50")
style.configure("mystyle.treeview.Heading",font=("times new roman",22,"bold"))
style.layout("mystyle.treeview",[('mystyle.treeview.treearea',{'sticky':'nswe'})])
scrool_bar=Scrollbar(table_frame,orient=VERTICAL)
table=ttk.Treeview(table_frame,height=5,style="mystyle.treeview",columns=("id","name","address","salary"),yscrollcommand=scrool_bar.set)
scrool_bar.pack(side=RIGHT,fill=Y)

table.bind("<ButtonRelease-1>",info)

table.heading("id",text="Employe ID")
table.heading("name",text="Name")
table.heading("address",text="Address")
table.heading("salary",text="Salary")

table['show']="headings"

table.column("id",width=248)
table.column("name",width=248)
table.column("address",width=248)
table.column("salary",width=248)

table.pack(fill=BOTH,expand=1)




win.mainloop()