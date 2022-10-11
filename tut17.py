from tkinter import *

root = Tk()
root.geometry("1200x600")
root.title('Pritha')

def myfunc():
    print("Inside function")

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

root.config(menu=yourmenubar)

root.mainloop()