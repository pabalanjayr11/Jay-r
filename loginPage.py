from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import pymysql

#function

def login_user():
    if username_entry.get()=='' or password_entry.get()=='':
        messagebox.showerror('Error', 'All fields are required!')
    else:
        try:
            con = pymysql.connect(host='localhost', user='root', password='@Pabalan12345')
            mycursor = con.cursor()
        except:
            messagebox.showerror('Error', 'Connection is not established try again!')
            return

        query = 'use account_registration'
        mycursor.execute(query)
        query = 'select * from account_list where username=%s and password=%s'
        mycursor.execute(query, (username_entry.get(), password_entry.get()))
        row = mycursor.fetchone()
        if row == None:
            messagebox.showerror('Error', 'Invalid Username or Password')
        else:
            messagebox.showinfo('Success', 'Login is successful')

        login_window.destroy()
        import table


def username_enter(event):
    if username_entry.get()=="Username:":
        username_entry.delete(0,END)

def password_enter(event):
    if password_entry.get()=="Password:":
        password_entry.delete(0,END)


def hide():
    openEye.config(file="hidden.png")
    password_entry.config(show="*")
    eyeBtn.config(command = show)

def show():
    openEye.config(file="view.png")
    password_entry.config(show="")
    eyeBtn.config(command=hide)


def signup_page():
    login_window.destroy()
    import signupPage


#design
login_window = Tk()
login_window.geometry("1366x768+80+30")
login_window.resizable(0,0)
login_window.title("Login Page")

bg = ImageTk.PhotoImage(file="1.png")
bg_label = Label(login_window, image=bg)
bg_label.place(x=0, y=0)

heading = Label(login_window,text="User Login", font=("Microsoft Yahei Light", 23, "bold"), bg="#03c27e", fg="#253237")
heading.place(x=975, y=150)

username_entry = Entry(login_window,width=33, font=("Microsoft Yahei Light", 15, "bold"), bg="#03c27e", fg="#253237", bd=0)
username_entry.place(x=850, y=250)
username_entry.insert(0, "Username:")
username_entry.bind("<FocusIn>", username_enter)

line1 = Frame(login_window, width=400, height=2, bg="#253237")
line1.place(x=850, y=275)


password_entry = Entry(login_window,width=33, font=("Microsoft Yahei Light", 15, "bold"), bg="#03c27e", fg="#253237", bd=0)
password_entry.place(x=850, y=310)
password_entry.insert(0, "Password:")
password_entry.bind("<FocusIn>", password_enter)

line2 = Frame(login_window, width=400, height=2, bg="#253237")
line2.place(x=850, y=335)

openEye = PhotoImage(file="view.png")
eyeBtn = Button(login_window, image = openEye, bd=0, bg="#03c27e", activebackground="white", cursor="hand2", command=hide)
eyeBtn.place(x=1220, y=305)


loginBtn = Button(login_window, text="Login", font=("Open Sans", 16, "bold"), bg="#253237", fg="#03c27e", activeforeground="white", activebackground="#253237", cursor="hand2", bd=0, width=30, command=login_user)
loginBtn.place(x=853, y=360)


orLabel = Label(login_window, text="--------------------------OR--------------------------",font=("Open Sans", 16), fg="#253237", bg="#03c27e")
orLabel.place(x=850, y=450)

fb = PhotoImage(file="facebook.png")
fbLabel = Label(login_window, image=fb, bg="#03c37f")
fbLabel.place(x=950, y=550)

google = PhotoImage(file="google.png")
googleLabel = Label(login_window, image=google, bg="#03c37f")
googleLabel.place(x=1035, y=550)

twitter = PhotoImage(file="twitter.png")
twitterLabel = Label(login_window, image=twitter, bg="#03c37f")
twitterLabel.place(x=1120, y=550)

signupLabel = Label(login_window, text="Don't have account yet?",font=("Open Sans", 9, "bold"), fg="#253237", bg="#03c27e")
signupLabel.place(x=850, y=630)

signupBtn = Button(login_window, text="Sign up here!", font=("Open Sans", 9, "bold underline"), bg="#03c27e", fg="blue", activeforeground="blue", activebackground="#02c37e", cursor="hand2", bd=0, command=signup_page)
signupBtn.place(x=990, y=630)

login_window.mainloop()