#### importing modules to work with
from tkinter import *
from tkinter import  messagebox as ms
from tkinter import ttk

## importing sqlite database to save ;ogin information
import sqlite3

#creating and attaching database and cursor to a variable for easy use
db = sqlite3.connect('password.db')
cursor = db.cursor()
cursor.execute(("CREATE TABLE IF NOT EXISTS admin (username TEXT NOT NULL, password TEXT NOT NULL)"))

## creating Tkinter window interface
main = Tk()
main.title("PASSWORD AUTH APP")
main.geometry('400x300')







##Placement of items on main window

intro_label = Label(main, text = "LOGIN PAGE", font= 'Sans 20 bold')
intro_label.grid(row=0, column=0, columnspan=6,pady=(10, 0), sticky=W)

user_name_input = Entry(main, bd=3, font= 'none 15 bold' )
user_name_input.grid(row=2, column=0, columnspan=6, pady=15, sticky=W)
password_input =Entry(main, bd=3, font= 'none 15 bold')
password_input.grid(row=3, column=0, columnspan=6, pady=15, sticky=W)
user_name_input.insert(0, "Enter username")
password_input.insert(0, "Enter password")


#function to make input clear when asked to input username and password
def entryclear(e):
    if user_name_input.get() == 'Enter username' or password_input.get() == 'Enter password':
        user_name_input.delete(0, END)
        password_input.delete(0, END)

        password_input.configure(show='*')


user_name_input.bind("<Button-1>", entryclear)
password_input.bind("<Button-1>", entryclear)


## creating function for main window interface login button and commanding function to the login button
def login():
    find_user = ('SELECT * FROM admin WHERE username = ? and password = ?')
    cursor.execute(find_user, [(user_name_input.get()), (password_input.get())])
    result = cursor.fetchall()

    if result:
        ms.showinfo('Success!', 'You are Logged in!')

    else:
        ms.showerror('Error!', 'Login information does not exist.')

# Login button on main window
login_button = Button(main, text='LOGIN',font=("Helvetica 10 bold"),width=20, fg='black', bg='green' , command=login)
login_button.grid(row=4, column=0, pady=15, sticky=W)



#### creating function for create button in main window
## if its a new user. log in information has to be created first using the create button

def create_account():
    sub = Toplevel()
    main.withdraw()
    sub.title("PASSWORD AUTH APP")
    sub.geometry('400x300')
    intro_label = Label(sub, text="LOGIN PAGE", font='Sans 20 bold')
    intro_label.grid(row=0, column=0, columnspan=6, pady=(10, 0), sticky=W)

    user_name_input1 = Entry(sub, bd=3, font='none 15 bold')
    user_name_input1.grid(row=2, column=0, columnspan=6, pady=15, sticky=W)
    password_input1 = Entry(sub, bd=3, font='none 15 bold')
    password_input1.grid(row=3, column=0, columnspan=6, pady=15, sticky=W)
    login_button = Button(sub, text='LOGIN', font=("Helvetica 10 bold"), width=20, fg='black', bg='green',command=create_account)
    login_button.grid(row=4, column=0, pady=15, sticky=W)


    ### creating function to create new account

    def create_new():
        if user_name_input1.get() != '' and password_input1.get() != '' :
            find_customer = ('SELECT * FROM admin WHERE username = ?')
            cursor.execute(find_customer, [(user_name_input1.get())])
            if cursor.fetchall():
                ms.showerror('Error!', 'Username Unavailable try a different one.')
            else:
                insert = 'INSERT INTO admin(username,password) VALUES(?,?)'
                cursor.execute(insert, [(user_name_input1.get()), (password_input1.get())])
                db.commit()

                # cursor.close()
                # db.close()

                ms.showinfo('Success!', 'Account Created!')
                main.deiconify()
                sub.withdraw()
    create_new_button = Button(sub, text='CREATE NEW', font=("Helvetica 10 bold"), width=20, fg='black', bg='green',command= lambda : (create_new(),main.deiconify()))
    create_new_button.grid(row=4, column=0, pady=15, sticky=W)


#### create account button on main window
create_info = Button(main, text='CREATE ACCOUNT',font=("Helvetica 10 bold"),width=20, fg='black', bg='lightblue' , command=create_account)
create_info.grid(row=5, column=0, pady=15, sticky=W)










main.mainloop()