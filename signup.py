from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import pymysql


def clear():
    emailEntry.delete(0, END)
    usernameEntry.delete(0, END)
    passwordEntry.delete(0, END)
    confirmpasswordEntry.delete(0, END)
    check.set(0)

def connect_database():
    if emailEntry.get()=='' or usernameEntry.get()=='' or passwordEntry.get()=='' or confirmpasswordEntry.get()=='':
        messagebox.showerror('NETH - Error','All Fields Are Required. ')
    elif passwordEntry.get() != confirmpasswordEntry.get():
        messagebox.showerror('NETH - Error','Passwords are not same. ')
    elif check.get()==0:
        messagebox.showerror('NETH - Error','Please Accept Terms and Conditions. ')
    else:
        try:
            con = pymysql.connect(host='localhost', user='root', password='neth.20051115')
            mycursor = con.cursor()
        except:
            messagebox.showerror('NETH - Error', 'Database Connectivity Issue, Please Try Again')
            return
        
        try:
            # Create the database if it doesn't exist
            query = 'create database if not exists userdata'
            mycursor.execute(query)

            # Use the userdata database
            query = 'use userdata'
            mycursor.execute(query)

            # Create the data table if it doesn't exist
            query = 'create table if not exists data(id int auto_increment primary key not null, email varchar(50), username varchar(100), password varchar(20))'
            mycursor.execute(query)
        except:
            mycursor.execute('use userdata')

        query='select * from data where username=%s'
        mycursor.execute(query,(usernameEntry.get()))

        row = mycursor.fetchone()
        if row != None:
            messagebox.showerror('Error', 'username Already exists')

        else:
            query = 'insert into data(email, username, password) values(%s, %s, %s)'
            mycursor.execute(query,(emailEntry.get(), usernameEntry.get(), passwordEntry.get()))
            con.commit()
            con.close()
            messagebox.showinfo('Success', 'Registration is successful')
            clear()
            signup_window.destroy()
            import signin


def login_page():
    signup_window.destroy()
    import signin
     
#create the screen.
signup_window = Tk()
signup_window.title("NETH - Signup page") 
signup_window.resizable(False, False)

#import the image for the screen.
background=ImageTk.PhotoImage(file='bg.jpg')
bgLabel=Label(signup_window, image=background)
bgLabel.grid()

#create a frame.
frame = Frame(signup_window, bg = 'white')
frame.place(x=554, y=100)

#create the heading of your signup page.
heading = Label(frame, text= "CREATE AN ACCOUNT",font =('Arial',18,'bold')
                ,bg='White',fg='red')
heading.grid(row=0, column=0, padx=10, pady = 10)

#create the email label.
emailLabel = Label(frame, text='Email', font=('Microsoft Yahei UI Light',10,'bold'),
                   bg= 'white', fg='firebrick1')
emailLabel.grid(row=1, column=0, sticky='w', padx=30, pady=(10,0))

#create the email box.
emailEntry = Entry(frame, width=30, font=('Microsoft Yahei UI Light',10,'bold'),
                   fg='white', bg='red')
emailEntry.grid(row=2, column=0, sticky='w', padx=30)

#create the username label.
usernameLabel = Label(frame, text='Username', font=('Microsoft Yahei UI Light',10,'bold'),
                   bg= 'white', fg='firebrick1')
usernameLabel.grid(row=3, column=0, sticky='w', padx=30, pady=(10,0))

#create the username box.
usernameEntry = Entry(frame, width=30, font=('Microsoft Yahei UI Light',10,'bold'),
                   fg='white', bg='red')
usernameEntry.grid(row=4, column=0, sticky='w', padx=30)

#create the password label.
passwordLabel = Label(frame, text='Password', font=('Microsoft Yahei UI Light',10,'bold'),
                   bg= 'white', fg='firebrick1')
passwordLabel.grid(row=5, column=0, sticky='w', padx=30, pady=(10,0))

#create the password box.
passwordEntry = Entry(frame, width=30, font=('Microsoft Yahei UI Light',10,'bold'),
                   fg='white', bg='red')
passwordEntry.grid(row=6, column=0, sticky='w', padx=30)

#create the confirmpassword label.
confirmpasswordLabel = Label(frame, text='Confirm Password', font=('Microsoft Yahei UI Light',10,'bold'),
                   bg= 'white', fg='firebrick1')
confirmpasswordLabel.grid(row=7, column=0, sticky='w', padx=30, pady=(10,0))

#create the confirmpassword box.
confirmpasswordEntry = Entry(frame, width=30, font=('Microsoft Yahei UI Light',10,'bold'),
                   fg='white', bg='red')
confirmpasswordEntry.grid(row=8, column=0, sticky='w', padx=30)

#create a variable call check
check = IntVar()

#create the checkbutton
termsandconditions = Checkbutton(frame, text='I agree to the Terms and conditions',font=('Open Sans', 10, 'bold'),
                                 fg = 'firebrick1' , bg='white', activebackground='white', activeforeground='firebrick1',
                                 cursor='hand2', variable = check)
termsandconditions.grid(row=9, column=0,pady = 10, padx=15)

#create the sign up button
signupButton = Button(frame, text='Signup',font=('Open Sans', 16, 'bold'),
                bd=0, bg='firebrick1', fg='white',activebackground='firebrick1', activeforeground='white', width = 17, command=connect_database)
signupButton.grid(row=10, column=0, pady=10)

#create already account label.
alreadyaccount = Label(frame, text="Don't have an account?", font=('Open Sans',9, 'bold'),
                       bg='white', fg='firebrick1')
alreadyaccount.grid(row=11, column=0, sticky='w', padx=30, pady=10)

#create the login button.
loginButton=Button(frame, text='log in', font=('Open Sans', 9, 'bold underline'),
                   bg = 'white', fg='blue', bd = 0, cursor='hand2', activebackground='white',
                   activeforeground='blue', command=login_page)
loginButton.place(x=170, y=400)


signup_window.mainloop()