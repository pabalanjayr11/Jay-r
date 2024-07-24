from tkinter import *
import pymysql
from tkinter import ttk

# Function to fetch data from database
def fetch_data():
    try:
        con = pymysql.connect(host='localhost', user='root', password='@Pabalan12345')
        mycursor = con.cursor()
        mycursor.execute('use account_registration')
        mycursor.execute('select * from account_list')
        data = mycursor.fetchall()
        return data
    except:
        return None

# Function to display data in table
def display_data():
    data = fetch_data()
    if data:
        tree.delete(*tree.get_children())
        for row in data:
            tree.insert('', END, values=row)

# Design
table_window = Tk()
table_window.geometry("990x660+270+70")
table_window.resizable(False, False)
table_window.title("Account List Page")


table_window.configure(bg='#f0f0f0')

top_frame = Frame(table_window, bg='#02c37e', height=50)
top_frame.pack(fill=X)

left_frame = Frame(table_window, bg='#02c37e', width=50)
left_frame.pack(side=LEFT, fill=Y)

right_frame = Frame(table_window, bg='#02c37e', width=50)
right_frame.pack(side=RIGHT, fill=Y)

bottom_frame = Frame(table_window, bg='#02c37e', height=50)
bottom_frame.pack(side=BOTTOM, fill=X)

# Create table
tree = ttk.Treeview(table_window, columns=(1, 2, 3, 4, 5, 6), show='headings', height=20)
tree.pack(side=LEFT, fill=BOTH, expand=1)

# Set column widths
tree.column(1, width=50)
tree.column(2, width=100)
tree.column(3, width=100)
tree.column(4, width=200)
tree.column(5, width=100)
tree.column(6, width=100)

# Set column headings
tree.heading(1, text='ID')
tree.heading(2, text='First Name')
tree.heading(3, text='Last Name')
tree.heading(4, text='Gmail')
tree.heading(5, text='Username')
tree.heading(6, text='Registration_Date')

# Set styles for the table
style = ttk.Style()
style.theme_use('default')
style.configure('Treeview', background='#253237', foreground='#02c37e', rowheight=25, font=('Arial', 12))
style.configure('Treeview.Heading', background='#d9d9d9', foreground='#253237', font=('Arial', 12, 'bold'))
style.map('Treeview', background=[('selected', '#007bff'), ('active', '#e6e6e6')])


# Display data in table
display_data()

table_window.mainloop()