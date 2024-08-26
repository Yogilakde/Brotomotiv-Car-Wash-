from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
from tkinter.ttk import *
from tkvideo import tkvideo

root = Tk()
root.title("Types Of Washes")
root.configure(background="white")
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))


video_label = tk.Label(root)
video_label.pack()
player = tkvideo("/Users/sayali/Desktop/Spyder/Project/video1.mp4", video_label, loop=1, size=(w, h))
player.play()


column_width = 450
column_spacing = 20


frame_basic = tk.Frame(root, bg='black', width=column_width, borderwidth=2, relief='solid')
frame_basic.place(x=25, y=70)

def payment():
    from subprocess import call
    call(['python', 'payment.py'])

image_path_basic = "/Users/sayali/Desktop/Spyder/Project/basic.jpg"
image_basic = Image.open(image_path_basic)
image_basic = image_basic.resize((column_width, 270), Image.LANCZOS)
photo_basic = ImageTk.PhotoImage(image_basic)
label_basic_image = tk.Label(frame_basic, image=photo_basic, bg='#f0f0f0')
label_basic_image.image = photo_basic
label_basic_image.pack()

label_basic_text = tk.Label(frame_basic, text='Basic Wash :-\n\nDescription:\nA standard exterior wash designed to remove surface dirt and grime.\nOften includes a pre-soak, soap application, and rinse.\n\nTypical Services:\n- Exterior wash with soap and water\n- Rinse\n- Air or towel drying',
                            font=('Georgia', 13), bg='red', justify='left')
label_basic_text.pack(pady=48)

button_basic = tk.Button(frame_basic, text='Basic Wash..', font=('Georgia', 20), bg='red',command=payment)
button_basic.pack()

# Column 2: Premium Wash
frame_premium = tk.Frame(root, bg='black', width=column_width, borderwidth=2, relief='solid')
frame_premium.place(x=25 +  column_width + column_spacing, y=70)

image_path_premium = "/Users/sayali/Desktop/Spyder/Project/premium.jpg"
image_premium = Image.open(image_path_premium)
image_premium = image_premium.resize((column_width, 270), Image.LANCZOS)
photo_premium = ImageTk.PhotoImage(image_premium)
label_premium_image = tk.Label(frame_premium, image=photo_premium, bg='#f0f0f0')
label_premium_image.image = photo_premium
label_premium_image.pack()

label_premium_text = tk.Label(frame_premium, text='Premium Wash :-\n\nDescription:\n An upgraded version of the Basic Wash with additional services \n to enhance the car\'s appearance and cleanliness.\nMay include interior cleaning as well as exterior services.\n\nTypical Services:\n- Everything in the Basic Wash\n- Wheel cleaning\n- Underbody wash\n- Wax application or polish\n- Tire shine\n- Interior vacuuming\n- Window cleaning',
                              font=('Georgia', 13), bg='red', justify='left')
label_premium_text.pack(pady=10)

button_premium = tk.Button(frame_premium, text='Premium Wash..', font=('Georgia', 20), bg='white',command=payment)
button_premium.pack()

# Column 3: Deluxe Wash
frame_deluxe = tk.Frame(root, bg='black', width=column_width, borderwidth=2, relief='solid')
frame_deluxe.place(x=25 + 2  * (column_width + column_spacing), y=70)

image_path_deluxe = "/Users/sayali/Desktop/Spyder/Project/deluxe.jpg"
image_deluxe = Image.open(image_path_deluxe)
image_deluxe = image_deluxe.resize((column_width, 270), Image.LANCZOS)
photo_deluxe = ImageTk.PhotoImage(image_deluxe)
label_deluxe_image = tk.Label(frame_deluxe, image=photo_deluxe, bg='#f0f0f0')
label_deluxe_image.image = photo_deluxe
label_deluxe_image.pack()

label_deluxe_text = tk.Label(frame_deluxe, text='Deluxe Wash :-\n\nDescription:\nThe most comprehensive wash package, providing thorough cleaning and\n detailing of both the exterior and interior of the vehicle.\nAimed at maintaining the car\'s condition and providing a near showroom finish.\n\nTypical Services:\n- Everything in the Premium Wash\n- Clay bar treatment for removing contaminants\n- Carpet and upholstery cleaning\n- Dashboard and console cleaning and conditioning\n- Seat cleaning and conditioning (leather or fabric)\n- Detailed cleaning of crevices and hard-to-reach areas\n- Engine cleaning',
                             font=('Georgia', 12), bg='red', justify='left')
label_deluxe_text.pack(pady=18)

button_deluxe = tk.Button(frame_deluxe, text='Deluxe Wash..', font=('Georgia', 20), bg='white',command=payment)
button_deluxe.pack()
def payment():
    from subprocess import call
    call(['python', 'payment.py'])

# Header and Footer
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
types_button = tk.Button(root, text="Payment", command=payment,font=("Marker", 10), bg='black')
types_button.place(x=1275, y=30)
contact_button = tk.Button(root, text="Contact us", font=("Marker", 10), bg='black')
contact_button.place(x=1350, y=30)

# footer_frame = tk.Frame(root, bg='Black', height=60, width=w)
# footer_frame.place(x=0, y=h-60)
footer_frame = tk.Frame(root, bg='Black', height=60, width=w)
footer_frame.place(x=0, y=h-60)
label_footer = tk.Label(footer_frame, text='Privacy & Policy | Contact | Terms and Conditions', font=('Medieval', 10), bg='black', fg='white')
label_footer.place(x=650, y=10)

root.mainloop()
