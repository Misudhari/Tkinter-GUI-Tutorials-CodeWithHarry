from tkinter import *
import tkinter.messagebox as tmsg

root = Tk()
root.geometry("1200x600")
root.title('Pritha')

def myfunc():
    print("Inside function")

def help():
    print('I will Help you.')
    a = tmsg.showinfo("Help", "Mithilesh will help you.")

def rate():
    print("Rate Us")
    a = tmsg.askquestion("Was your experience good?","Was your experience good?")
    print(a)
# Use this to create non dropdown menu
# mymenu = Menu(root)
# mymenu.add_command(label="File", command=myfunc)
# mymenu.add_command(label="Exit", command=quit)
#
# root.config(menu=mymenu)

yourmenubar = Menu(root)
m1 = Menu(yourmenubar, tearoff=0)
m1.add_command(label="New Project...", command=myfunc)
m1.add_command(label="New...", command=myfunc)
m1.add_separator()
m1.add_command(label="Open", command=myfunc)
m1.add_command(label="Save", command=myfunc)
yourmenubar.add_cascade(label="File", menu=m1)

m2 = Menu(yourmenubar, tearoff=0)
m2.add_command(label="Copy", command=myfunc)
m2.add_command(label="Paste", command=myfunc)
m2.add_command(label="Cut", command=myfunc)
m2.add_separator()
m2.add_command(label="Find", command=myfunc)
yourmenubar.add_cascade(label="Edit", menu=m2)

m3 = Menu(yourmenubar, tearoff=0)
m3.add_command(label="Help", command=help)
m3.add_command(label="Rate Us", command=rate)
yourmenubar.add_cascade(label="Help", menu=m3)

root.config(menu=yourmenubar)

root.mainloop()