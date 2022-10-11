from tkinter import *
from PIL import Image, ImageTk

root = Tk()

# gui logic
root.geometry("1200x600")

f2 = Frame(root, borderwidth=9, bg = "grey", relief=SUNKEN)
f2.pack(side=TOP, fill="x")

l2 =Label(f2,text="Pritha 2", font="Helvetica 16 bold", fg = 'red', pady = 25)
l2.pack()

f1 = Frame(root, bg="grey", borderwidth=6)
f1.pack(side=LEFT, fill="y")


l =Label(f1,text="Pritha")
l.pack()

root.mainloop()