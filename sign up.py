from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
from tkinter.ttk import *
import sqlite3
import re
from tkinter import messagebox as ms

root = Tk()
root.title("Home")
root.configure(background="black")
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))

image2 = Image.open("//Users/sayali/Desktop/Spyder/Project/login2.jpg")
image2 = image2.resize((1200, 800), Image.LANCZOS)
background_image = ImageTk.PhotoImage(image2)
background_label = tk.Label(root, image=background_image)
background_label.image = background_image
background_label.place(x=0, y=60)

name = tk.StringVar()
Email = tk.StringVar()
PhoneNo = tk.StringVar()
username = tk.StringVar()
password = tk.StringVar()

db = sqlite3.connect('Carwash.db')
cursor = db.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS REGISTER'
               "(Name TEXT, Email TEXT, PhoneNo TEXT, UserName TEXT, Password TEXT)")
db.commit()

def password_check(passwd):
    SpecialSym = ['$','@','#','%']
    val = True

    if len(passwd) < 6:
        print('Length should be at least 6')
        val = False

    if len(passwd) > 20:
        print("Length should not be greater than 20")
        val = False

    if not any(char.isdigit() for char in passwd):
        print('Password should have at least one numerical')
        val = False

    if not any(char.isupper() for char in passwd):
        print("Password should have at least one uppercase letter")
        val = False

    if not any(char.islower() for char in passwd):
        print("Password should have at least one lowercase letter")
        val = False

    if not any(char in SpecialSym for char in passwd):
        print('Password should have at least one of the symbols $@#%')
        val = False
    if val:
        return val

def insert():
    fname = name.get()
    email = Email.get()
    mobile = PhoneNo.get()
    un = username.get()
    pwd = password.get()

    with sqlite3.connect('Carwash.db') as db:
        c = db.cursor()

    regex = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if re.search(regex, email):
        a = True
    else:
        a = False

    if fname.isdigit() or (fname == ""):
        ms.showinfo("Message", "Please enter Valid Name")
    elif email == "" or a == False:
        ms.showinfo("Message", "Please Enter valid Email")
    elif len(mobile) < 10 or len(mobile) > 10:
        ms.showinfo("Message", "Please Enter 10 Digit Number")
    elif un == "":
        ms.showinfo("Message", "Please Enter Valid Username")
    elif pwd == "":
        ms.showinfo("Message", "Please Enter Valid Password")
    elif pwd == "" or (password_check(pwd)) != True:
        ms.showinfo("Message", "password must contain at least 1 uppercase, 1 lowercase, 1 special symbol, 1 number is required")
    else:
        try:
            conn = sqlite3.connect('Carwash.db')
            with conn:
                cursor = conn.cursor()
                cursor.execute('INSERT INTO REGISTER (Name, Email, PhoneNo, UserName, Password) VALUES (?, ?, ?, ?, ?)',
                               (fname, email, mobile, un, pwd))
                conn.commit()
                ms.showinfo('Success!', 'Account created Successfully!')
        except sqlite3.Error as e:
            ms.showinfo('Error!', f'Error occurred: {e}')
        finally:
            conn.close()

frame = tk.Frame(root, bg='#2874A6', height=800, width=350)
frame.place(x=1100, y=60)

label = tk.Label(frame, bg='red', text='Sign in', font=('Medieval', 20), fg='white')
label.place(x=145, y=10)

def login():
    from subprocess import call
    call(['python', 'login.py'])

def typesOfwashes():
    from subprocess import call
    call(['python', 'Types Of Washes.py'])

def payment():
    from subprocess import call
    call(['python', 'payment.py'])
    
def Contactus():
    from subprocess import call
    call(['python','Contact us.py'])

label = tk.Label(frame, text="Enter Name:", bg='black', fg='white')
label.place(x=25, y=62)
entry = tk.Entry(frame, textvariable=name)
entry.place(x=110, y=60)

label = tk.Label(frame, text="E-mail:", bg='black', fg='white')
label.place(x=30, y=102)
entry = tk.Entry(frame, textvariable=Email)
entry.place(x=110, y=100)

label = tk.Label(frame, text="Phone No:", bg='black', fg='white')
label.place(x=30, y=142)
entry = tk.Entry(frame, textvariable=PhoneNo)
entry.place(x=110, y=140)

label = tk.Label(frame, text="UserName:", bg='black', fg='white')
label.place(x=30, y=182)
entry = tk.Entry(frame, textvariable=username)
entry.place(x=110, y=180)

label = tk.Label(frame, text="Password:", bg='black', fg='white')
label.place(x=30, y=222)
entry = tk.Entry(frame, textvariable=password, show='*')
entry.place(x=110, y=220)

button = tk.Button(frame, font=('Medieval', 12), text="Create Account", command=insert, bg='black')
button.place(x=120, y=300)


address_heading_label = tk.Label(frame, text="Address:", bg='black', fg='white', font=('Arial', 22, 'bold'), justify='center')
address_heading_label.place(x=120, y=400)


address_label = tk.Label(frame, text="Brotomotiv Car Wash,\nDehu Phata,\nAlandi Devachi,\nPune-412105,\nMaharashtra, India.",
                         bg='#800000', fg='white', font=('Arial', 20), justify='center')
address_label.place(x=80, y=450)

frame = tk.Frame(root, bg='#800000', height=60, width=3000)
frame.place(x=0, y=0)
label = tk.Label(frame, text='BrotoMotiv Car Wash... ', font=('Medieval', 30), bg='#800000', fg='white')
label.place(x=600, y=10)

button = tk.Button(root, text="Home", font=("Marker", 10), bg='black')
button.place(x=1040, y=30)

button = tk.Button(root, text="Login", command=login, font=("Marker", 10), bg='black')
button.place(x=1100, y=30)

button = tk.Button(root, text="Types Of Washes", command=typesOfwashes, font=("Marker", 10), bg='black')
button.place(x=1160, y=30)

types_button = tk.Button(root, text="Payment", command=payment, font=("Marker", 10), bg='black')
types_button.place(x=1275, y=30)

button = tk.Button(root, text="Contact us", command=Contactus, font=("Marker", 10), bg='black')
button.place(x=1350, y=30)

footer_frame = tk.Frame(root, bg='#800000', height=60, width=w)
footer_frame.place(x=0, y=h-60)
label_footer = tk.Label(footer_frame, text='Privacy & Policy | Contact | Terms and Conditions', font=('Medieval', 10), bg='#800000', fg='white')
label_footer.place(x=650, y=10)

root.mainloop()
