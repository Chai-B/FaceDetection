import tkinter as tk
from tkinter import Label
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image,ImageTk
import main_opencv as moc
import cv2 as cv
import sys


win = tk.Tk()

win.title('face detector')
win.geometry('700x200')

menu=tk.Menu(win)
win.config(menu=menu)
filemenu = tk.Menu(menu)
menu.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='New',command=win)
filemenu.add_command(label='Open...')
filemenu.add_separator()
filemenu.add_command(label='Exit', command=win.quit)
helpmenu = tk.Menu(menu)
menu.add_cascade(label='Help', menu=helpmenu)
helpmenu.add_command(label='About')




lbl=tk.Label(win, text="Face Detection", fg='white', font=("Helvetica", 22))
lbl.pack()

def upload():
    path = tk.filedialog.askopenfilename(filetypes=[("Image files","*.png *.jpg *.jpeg")])
    if len(path):
        moc.image(path)
    else:
        msg4="No file is chosen !! Please choose a file."
        mesg4=messagebox.showerror('Error',msg4)
        

msg="This is a simple Face detection tool made with OpenCV and Python."
msg2="Made by- Chai-B"
msg3="Pls select source for Face detection"

mesg = tk.Message(win,text=msg,width= 650) 
mesg2=tk.Message(win,text=msg2,width=650)
mesg3=tk.Message(win,text=msg3,width=650)
mesg.pack()
mesg2.pack()
mesg3.pack()


button1=tk.Button(win,text='Exit',width=10,command=win.destroy)
button2=tk.Button(win,text='Choose Image',width=20,command=upload)
button3=tk.Button(win,text='Open Camera',width=20,command=moc.capture)


button3.pack()
button2.pack()
button1.pack()

win.mainloop()
