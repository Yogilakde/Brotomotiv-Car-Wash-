from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
from tkvideo import tkvideo
import sqlite3
from tkinter import messagebox as ms

root = Tk()
root.title("Login")
root.configure(background='white')
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))


video_label = tk.Label(root)
video_label.pack()
player = tkvideo("/Users/sayali/Desktop/Spyder/Project/video1.mp4", video_label, loop=1, size=(w, h))
player.play()

username = StringVar()
password = StringVar()

def login():
    with sqlite3.connect('Carwash.db') as db:
        c = db.cursor()
        
        find_entry = ('SELECT * FROM REGISTER WHERE UserName=? and Password=?')
        c.execute(find_entry, [(username.get()), (password.get())])
        result = c.fetchall()
        
        if result:
            ms.showinfo("Message", "Login Successful")
            root.destroy()
            
            from subprocess import call
            call(['python', 'Types Of Washes.py'])
        else:
            ms.showerror('Oops!', 'Username or Password did not match.')


frame = tk.Frame(root, bg='#900C3F', height=250, width=325, borderwidth=5, relief='ridge')
frame.place(x=550, y=250)
label = tk.Label(frame, bg='red', text='Login..', font=('Medieval', 20), fg='white')
label.place(x=130, y=10)

label = tk.Label(frame, text='Username:', bg='black', fg='white')
label.place(x=30, y=62)
entry = tk.Entry(frame, textvariable=username)
entry.place(x=110, y=60)

label = tk.Label(frame, text='Password:', bg='black', fg='white')
label.place(x=30, y=92)
entry = tk.Entry(frame, textvariable=password, show='*')
entry.place(x=110, y=90)

button = tk.Button(frame, font=('Medieval', 12), text='Submit', command=login)
button.place(x=130, y=140)


header_frame = tk.Frame(root, bg='Black', height=60, width=3000)
header_frame.place(x=0, y=0)
label = tk.Label(header_frame, text='BrotoMotiv Car Wash... ', font=('Medieval', 30), bg='#800000', fg='white')
label.place(x=600, y=10)


button = tk.Button(root, text="Home", font=("Marker", 10), bg='black')
button.place(x=1040, y=30)
button = tk.Button(root, text="Login", font=("Marker", 10), bg='black')
button.place(x=1100, y=30)
button = tk.Button(root, text="Types Of Washes", font=("Marker", 10), bg='black')
button.place(x=1160, y=30)
types_button = tk.Button(root, text="Payment", font=("Marker", 10), bg='black')
types_button.place(x=1275, y=30)
button = tk.Button(root, text="Contact us", font=("Marker", 10), bg='black')
button.place(x=1350, y=30)

footer_frame = tk.Frame(root, bg='Black', height=60, width=w)
footer_frame.place(x=0, y=h-60)
label_footer = tk.Label(footer_frame, text='Privacy & Policy | Contact | Terms and Conditions', font=('Medieval', 10), bg='black', fg='white')
label_footer.place(x=650, y=10)

root.mainloop()