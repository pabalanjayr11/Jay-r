from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import pymysql
import datetime

#function

def clear():
    fName_entry.delete(0,END)
    lName_entry.delete(0, END)
    gmail_entry.delete(0, END)
    username_entry.delete(0, END)
    password_entry.delete(0, END)

def connect_db():
    if fName_entry.get()=='' or lName_entry.get()=='' or gmail_entry.get()=='' or username_entry.get()=='' or password_entry.get()=='':
        messagebox.showerror('Error', 'All fields are required!')
    else:
        try:
            con = pymysql.connect(host='localhost', user='root', password='@Pabalan12345')
            mycursor = con.cursor()
        except:
            messagebox.showerror('Error', 'Database Connectivity Issue, Please Try Again!')
            return

        try:
            query = 'create database account_registration'
            mycursor.execute(query)
            query = 'use account_registration'
            mycursor.execute(query)
            query = 'create table account_list(id int auto_increment primary key not null, fname varchar(50), lname varchar(50), gmail varchar(100), username varchar(50), password varchar(50), reg_date date)'
            mycursor.execute(query)
        except:
            mycursor.execute('use account_registration')

        query = 'select * from account_list where username=%s'
        mycursor.execute(query,(username_entry.get()))

        row = mycursor.fetchone()
        if row != None:
            messagebox.showerror('Error', 'Username Already Exist')
        else:
            query = 'insert into account_list(fname,lname,gmail,username,password,reg_date) values(%s,%s,%s,%s,%s,%s)'
            mycursor.execute(query,(fName_entry.get(),lName_entry.get(),gmail_entry.get(),username_entry.get(),password_entry.get(), datetime.date.today()))
            con.commit()
            con.close()
            messagebox.showinfo('Success', 'Registration Successful')
            clear()
            signup_window.destroy()
            import loginPage

def login_page():
    signup_window.destroy()
    import loginPage


#design
signup_window = Tk()
signup_window.geometry("1366x768+80+30")
signup_window.resizable(False,False)
signup_window.title("Signup Page")


bg = ImageTk.PhotoImage(file="2.png")
bg_label = Label(signup_window, image=bg)
bg_label.place(x=0, y=0)

heading = Label(signup_window,text="CREATE AN ACCOUNT", font=("Microsoft Yahei Light", 18, "bold"), bg="#02c37e", fg="#243136")
heading.place(x=140, y=120)

fname_label = Label(signup_window, text="First Name:", bg="#02c37e", fg="#253237")
fname_label.place(x=70, y=200)
fName_entry = Entry(signup_window,width=49, font=("Microsoft Yahei Light", 11, "bold"), bg="#253237", fg="#02c37e", bd=0)
fName_entry.place(x=70, y=220)



lname_label = Label(signup_window, text="FLast Name:", bg="#02c37e", fg="#253237")
lname_label.place(x=70, y=250)
lName_entry = Entry(signup_window,width=49, font=("Microsoft Yahei Light", 11, "bold"), bg="#253237", fg="#02c37e", bd=0)
lName_entry.place(x=70, y=270)



gmail_label = Label(signup_window, text="Gmail:", bg="#02c37e", fg="#253237")
gmail_label.place(x=70, y=300)
gmail_entry = Entry(signup_window,width=49, font=("Microsoft Yahei Light", 11, "bold"), bg="#253237", fg="#02c37e", bd=0)
gmail_entry.place(x=70, y=320)



username_label = Label(signup_window, text="Username:", bg="#02c37e", fg="#253237")
username_label.place(x=70, y=350)
username_entry = Entry(signup_window,width=49, font=("Microsoft Yahei Light", 11, "bold"), bg="#253237", fg="#02c37e", bd=0)
username_entry.place(x=70, y=370)



password_label = Label(signup_window, text="Password:", bg="#02c37e", fg="#253237")
password_label.place(x=70, y=400)
password_entry = Entry(signup_window,width=49, font=("Microsoft Yahei Light", 11, "bold"), bg="#253237", fg="#02c37e", bd=0)
password_entry.place(x=70, y=420)



signupBtn = Button(signup_window, text="Sign up", font=("Open Sans", 16, "bold"), bg="#253237", fg="#02c37e", activeforeground="#02c37e", activebackground="#253237", cursor="hand2", bd=0, width=34, command=connect_db)
signupBtn.place(x=68, y=470)


loginLabel = Label(signup_window, text="Already have an account?",font=("Open Sans", 9, "bold"), fg="#253237", bg="#02c37e")
loginLabel.place(x=70, y=530)

loginBtn = Button(signup_window, text="Login now!", font=("Open Sans", 9, "bold underline"), bg="#02c37e", fg="blue", activeforeground="blue", activebackground="#02c37e", cursor="hand2", bd=0, command=login_page)
loginBtn.place(x=220, y=530)


signup_window.mainloop()