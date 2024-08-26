from tkinter import *
from tkinter.ttk import *
import tkinter as tk 
from tkvideo import tkvideo

root=tk.Tk()

w,h=root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry("%dx%d+0+0" %(w,h))

video_label=tk.Label(root)
video_label.pack()
player=tkvideo("/Users/sayali/Desktop/Spyder/Project/video1.mp4", video_label,loop=1, size=(w,h))
player.play()

root.mainloop()