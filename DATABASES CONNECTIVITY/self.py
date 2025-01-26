from tkinter import* 
from tkinter import ttk
import tkinter.messagebox
import mysql.connector as mc



win=Tk()
win.geometry("1420x800+0+0")
win.title("Education2All")
win.config(background="red")


main_frame=Frame(win,bd=10,relief=RIDGE,width=2160,height=600)
main_frame.pack(pady=50)
