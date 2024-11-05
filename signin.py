from tkinter import *
from PIL import ImageTk


#Functionality part
def signup_page():
    login_window.destroy()
    import signup
    
def hide():
    openeye.config(file='closeye.png')
    passwordEntry.config(show='*')
    eyeButton.config(command = show)

def show():
    openeye.config(file='openeye.png')
    passwordEntry.config(show='')
    eyeButton.config(command = hide)

def user_enter(neth):
    if usernameEntry.get()=="Username":
        usernameEntry.delete(0,END)

def password_enter(neth):
    if passwordEntry.get()=="Password":
        passwordEntry.delete(0,END)


#GUI part and create the window.
login_window = Tk()
login_window.geometry("990x660+50+50")
login_window.resizable(0,0)
login_window.title("NETH - Login page")

#import the image.
bgImage = ImageTk.PhotoImage(file='bg.jpg')
bgLabel = Label(login_window, image= bgImage)
bgLabel.place(x=0, y=0)

#create the heading of your login page.
heading = Label(login_window, text= "USER LOGIN",font =('Arial',23,'bold'),bg='White',fg='red')
heading.place(x=605, y=120)

#create the user name box and we can type in it.
usernameEntry = Entry(login_window, width=25, font =('Microsoft Yahei UI Light',11,'bold'),bd=0,fg='firebrick1')
usernameEntry.place(x=580, y=200)
usernameEntry.insert(0, 'Username')
#call the fuction when we click the user_name box.
usernameEntry.bind('<FocusIn>', user_enter)

#create a line after user_name box.
frame1 = Frame(login_window, width=250, height=2, bg='firebrick1')
frame1.place(x = 580, y = 222)

#create the password box and we can type in it
passwordEntry = Entry(login_window, width=25, font =('Microsoft Yahei UI Light',11,'bold'),bd=0,fg='firebrick1')
passwordEntry.place(x=580, y=260)
passwordEntry.insert(0, 'Password')
#call the function when we click the password box.
passwordEntry.bind('<FocusIn>', password_enter)

#create a line after password box.
frame2 = Frame(login_window, width=250, height=2, bg='firebrick1')
frame2.place(x = 580, y = 282)

#import the openeye image for the web page.
openeye = PhotoImage(file='openeye.png')
eyeButton = Button(login_window, image=openeye, bd=0, bg='white', activebackground='white',
                    cursor='hand2', command=hide)
eyeButton.place(x=800, y=255)


#create a forgot password text.
forgetButton = Button(login_window, text='Forgot Password?', bd=0, bg='white', activebackground='white',
                    cursor='hand2', font =('Microsoft Yahei UI Light',9,'bold'),fg='red',activeforeground='red')
forgetButton.place(x=715, y=295)

#create the login button.
loginButton = Button(login_window, text = 'Login',font=('Open Sans',16,'bold'),fg="white",
                     bg = 'firebrick1',activeforeground='white',activebackground='red', cursor='hand2', bd=0, width=19)
loginButton.place(x=578, y=350)

#create the OR  label.
orLabel=Label(login_window, text='---------------OR---------------', font=('Open Sans', 16), 
              fg = 'firebrick1', bg='white')
orLabel.place(x=583, y=400)

#import facebook logo.
facebook_logo = PhotoImage(file='facebook.png')
fbLabel = Label(login_window, image=facebook_logo, bg='white')
fbLabel.place(x=640, y=440)

#import google logo.
google_logo = PhotoImage(file='google.png')
googleLabel = Label(login_window, image=google_logo, bg='white')
googleLabel.place(x=690, y=440)

#import twitter logo.
twitter_logo = PhotoImage(file='twitter.png')
twitterLabel = Label(login_window, image=twitter_logo, bg='white')
twitterLabel.place(x=740, y=440)

#create the signup label.
signupLabel=Label(login_window, text='Dont have an account?', font=('Open Sans', 9, 'bold'), 
              fg = 'firebrick1', bg='white')
signupLabel.place(x=590, y=500)

#create the newaccount button.
newaccountButton = Button(login_window, text = 'Create new one',font=('Open Sans',9,'bold underline'),fg="blue",
                     bg = 'white',activeforeground='blue',activebackground='white', cursor='hand2', bd=0, command=signup_page)
newaccountButton.place(x=727, y=500)


login_window.mainloop()