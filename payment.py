import sqlite3
from tkinter import *
import tkinter as tk
from tkinter import messagebox 
from PIL import Image, ImageTk
from tkinter.ttk import *


conn = sqlite3.connect("payments.db")
cursor = conn.cursor()


cursor.execute('''
CREATE TABLE IF NOT EXISTS payments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    card_number TEXT NOT NULL,
    cvv TEXT NOT NULL,
    aadhaar_number TEXT NOT NULL,
    wash_type TEXT NOT NULL,
    amount INTEGER NOT NULL
)
''')
conn.commit()


root = Tk()
root.title("Payment")
root.configure(background="white")
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))


image_path_payment = "/Users/sayali/Desktop/Spyder/Project/deluxe.jpg"  
image_payment = Image.open(image_path_payment)
image_payment = image_payment.resize((w, h), Image.LANCZOS)
background_image = ImageTk.PhotoImage(image_payment)
background_label = tk.Label(root, image=background_image)
background_label.image = background_image
background_label.place(x=0, y=0)


frame_payment = tk.Frame(root, bg='#2874A6', height=550, width=400, bd=5, relief="raised")
frame_payment.place(x=600, y=150)

label_title = tk.Label(frame_payment, bg='red', text='Payment', font=('Medieval', 20), fg='white')
label_title.place(x=150, y=10)


label_type_of_wash = tk.Label(frame_payment, text="Type of Wash:", font=('Georgia', 12), bg='#2874A6', fg='white')
label_type_of_wash.place(x=30, y=70)

type_of_wash = StringVar()
type_of_wash.set("Select Wash Type")  
wash_types = ["Select a wash", "Basic Wash", "Premium Wash", "Deluxe Wash"]
dropdown = OptionMenu(frame_payment, type_of_wash, *wash_types, command=lambda _: update_amount())
dropdown.place(x=160, y=70)


label_card_number = tk.Label(frame_payment, text="Card Number:", font=('Georgia', 12), bg='#2874A6', fg='white')
label_card_number.place(x=30, y=120)
entry_card_number = tk.Entry(frame_payment)
entry_card_number.place(x=160, y=120)


label_cvv = tk.Label(frame_payment, text="CVV:", font=('Georgia', 12), bg='#2874A6', fg='white')
label_cvv.place(x=30, y=170)
entry_cvv = tk.Entry(frame_payment)
entry_cvv.place(x=160, y=170)


label_cardholder_name = tk.Label(frame_payment, text="Aadhaar Card No:", font=('Georgia', 12), bg='#2874A6', fg='white')
label_cardholder_name.place(x=30, y=220)
entry_cardholder_name = tk.Entry(frame_payment)
entry_cardholder_name.place(x=160, y=220)


label_amount = tk.Label(frame_payment, text="Amount:", font=('Georgia', 12), bg='#2874A6', fg='white')
label_amount.place(x=30, y=270)
entry_amount = tk.Entry(frame_payment)
entry_amount.place(x=160, y=270)


def update_amount():
    wash_type = type_of_wash.get()
    if wash_type == "Select a wash": 
        amount = 0
    elif wash_type == "Basic Wash":
        amount = 350
    elif wash_type == "Premium Wash":
        amount = 450
    elif wash_type == "Deluxe Wash":
        amount = 599
    else:
        amount = ""
    entry_amount.delete(0, END)
    entry_amount.insert(0, amount)


def process_payment():
    card_number = entry_card_number.get()
    cvv = entry_cvv.get()
    aadhaar_number = entry_cardholder_name.get()
    wash_type = type_of_wash.get()
    amount = entry_amount.get()

   
    if len(card_number) != 10 or not card_number.isdigit():
        messagebox.showwarning("Invalid Input", "Card Number must be 10 digits.")
        return
    if len(cvv) != 4 or not cvv.isdigit():
        messagebox.showwarning("Invalid Input", "CVV must be 4 digits.")
        return
    if len(aadhaar_number) != 12 or not aadhaar_number.isdigit():
        messagebox.showwarning("Invalid Input", "Aadhaar Number must be 12 digits.")
        return

   
    cursor.execute('''
    INSERT INTO payments (card_number, cvv, aadhaar_number, wash_type, amount)
    VALUES (?, ?, ?, ?, ?)
    ''', (card_number, cvv, aadhaar_number, wash_type, amount))
    conn.commit()

   
    messagebox.showinfo("Payment Status", "Payment Successful!")
    
def Contactus():
    from subprocess import call
    call(['python','Contact us.py'])


button_pay = tk.Button(frame_payment, bg='green', font=('Medieval', 12), text="Pay Now", command=process_payment)
button_pay.place(x=160, y=320)


header_frame = tk.Frame(root, bg='Black', height=60, width=w)
header_frame.place(x=0, y=0)
header_label = tk.Label(header_frame, text='BrotoMotiv Car Wash... ', font=('Medieval', 30), bg='#800000', fg='white')
header_label.place(x=600, y=10)


home_button = tk.Button(root, text="Home", font=("Marker", 10), bg='black')
home_button.place(x=1040, y=30)
login_button = tk.Button(root, text="Login", font=("Marker", 10), bg='black')
login_button.place(x=1100, y=30)
types_button = tk.Button(root, text="Types Of Washes", font=("Marker", 10), bg='black')
types_button.place(x=1160, y=30)
types_button = tk.Button(root, text="Payment", font=("Marker", 10), bg='black')
types_button.place(x=1275, y=30)
contact_button = tk.Button(root, text="Contact us", command=Contactus,font=("Marker", 10), bg='black')
contact_button.place(x=1350, y=30)


footer_frame = tk.Frame(root, bg='Black', height=60, width=w)
footer_frame.place(x=0, y=h-60)
label_footer = tk.Label(footer_frame, text='Privacy & Policy | Contact | Terms and Conditions', font=('Medieval', 10), bg='black', fg='white')
label_footer.place(x=650, y=10)

root.mainloop()


conn.close()