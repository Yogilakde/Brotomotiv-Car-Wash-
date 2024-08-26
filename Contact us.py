from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox as ms
import sqlite3

def create_table():
    conn = sqlite3.connect('contact.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            phone TEXT NOT NULL,
            message TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def insert_contact(name, email, phone, message):
    conn = sqlite3.connect('contact.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO contacts (name, email, phone, message)
        VALUES (?, ?, ?, ?)
    ''', (name, email, phone, message))
    conn.commit()
    conn.close()

def submit_contact():
    name = name_var.get()
    email = email_var.get()
    phone = phone_var.get()
    message = message_var.get("1.0", END)

    if not name or not email or not phone or not message.strip():
        ms.showwarning("Warning", "All fields must be filled out.")
        return

    insert_contact(name, email, phone, message)
    ms.showinfo("Success", "Thanks for your feedback!")

    name_var.set("")
    email_var.set("")
    phone_var.set("")
    message_var.delete("1.0", END)

# Create the main application window
contact_root = Tk()
contact_root.title("Contact Us - BrotoMotiv Car Wash")
contact_root.configure(background="white")
w, h = contact_root.winfo_screenwidth(), contact_root.winfo_screenheight()
contact_root.geometry("%dx%d+0+0" % (w, h))

# Background Image
image_path_contact = "/Users/sayali/Desktop/Spyder/Project/1.jpg"  # Update this path as necessary
image_contact = Image.open(image_path_contact)
image_contact = image_contact.resize((w, h), Image.LANCZOS)
background_image_contact = ImageTk.PhotoImage(image_contact)
background_label_contact = tk.Label(contact_root, image=background_image_contact)
background_label_contact.image = background_image_contact
background_label_contact.place(x=0, y=0)

# Create a frame for the contact form
frame_contact = tk.Frame(contact_root, bg='white', padx=20, pady=20)
frame_contact.place(relx=0.5, rely=0.55, anchor=CENTER)

# Variables for storing user input
name_var = StringVar()
email_var = StringVar()
phone_var = StringVar()

# Name Label and Entry
label_name = tk.Label(frame_contact, text="Name:", font=("Arial", 14), bg='white')
label_name.grid(row=0, column=0, sticky="w")
entry_name = tk.Entry(frame_contact, textvariable=name_var, font=("Arial", 14))
entry_name.grid(row=0, column=1)

# Email Label and Entry
label_email = tk.Label(frame_contact, text="Email:", font=("Arial", 14), bg='white')
label_email.grid(row=1, column=0, sticky="w")
entry_email = tk.Entry(frame_contact, textvariable=email_var, font=("Arial", 14))
entry_email.grid(row=1, column=1)

# Phone Label and Entry
label_phone = tk.Label(frame_contact, text="Phone No:", font=("Arial", 14), bg='white')
label_phone.grid(row=2, column=0, sticky="w")
entry_phone = tk.Entry(frame_contact, textvariable=phone_var, font=("Arial", 14))
entry_phone.grid(row=2, column=1)

# Message Label and Text Area
label_message = tk.Label(frame_contact, text="Message:", font=("Arial", 14), bg='white')
label_message.grid(row=3, column=0, sticky="nw")
message_var = Text(frame_contact, height=5, width=30, font=("Arial", 14))
message_var.grid(row=3, column=1)

# Submit Button
button_submit = tk.Button(frame_contact, text="Submit", font=("Arial", 14), bg='green', command=submit_contact)
button_submit.grid(row=4, columnspan=2, pady=10)

# Address Frame
frame_address = tk.Frame(contact_root, bg='#800000', padx=10, pady=10)
frame_address.place(relx=0.5, rely=0.25, anchor=CENTER)

# Address Label
address_label_title = tk.Label(frame_address, text="Our Address:-", font=('Arial', 24, 'bold'), bg='#800000', fg='white')
address_label_title.pack(pady=(0, 0))

address_label = tk.Label(frame_address, text="BrotoMotiv Car Wash,\nDehu Phata,\nAlandi Devachi,\nPune-412105,\nMaharashtra, India.",
                         bg='#800000', fg='white', font=('Arial', 20), justify='center')
address_label.pack()

# Header
header_frame = tk.Frame(contact_root, bg='Black', height=60, width=w)
header_frame.place(x=0, y=0)
header_label = tk.Label(header_frame, text='BrotoMotiv Car Wash... ', font=('Medieval', 30), bg='#800000', fg='white')
header_label.place(x=600, y=10)

# Navigation Buttons
home_button = tk.Button(contact_root, text="Home", font=("Marker", 10), bg='black')
home_button.place(x=1040, y=30)
login_button = tk.Button(contact_root, text="Login", font=("Marker", 10), bg='black')
login_button.place(x=1100, y=30)
types_button = tk.Button(contact_root, text="Types Of Washes", font=("Marker", 10), bg='black')
types_button.place(x=1160, y=30)
payment_button = tk.Button(contact_root, text="Payment", font=("Marker", 10), bg='black')
payment_button.place(x=1275, y=30)
contact_button = tk.Button(contact_root, text="Contact us", font=("Marker", 10), bg='black')
contact_button.place(x=1350, y=30)

# Footer Frame
footer_frame = tk.Frame(contact_root, bg='Black', height=60, width=w)
footer_frame.place(x=0, y=h-60)
label_footer = tk.Label(footer_frame, text='Privacy & Policy | Contact | Terms and Conditions', font=('Medieval', 10), bg='black', fg='white')
label_footer.place(x=650, y=10)

# Create the database and table
create_table()

# Start the application
contact_root.mainloop()
