from tkinter import *
from PIL import  Image, ImageTk
root = Tk()

# tips

# IMPORTANT LABEL OPTIONS
# text - adds the text
# bd - background
# fg - foreground
# font - set font
# padx - X padding
# pady - Y padding
# relief - Border Styling - SUNKEN, RAISED, GROOVE, RIDGE

# IMPORTANT PACK OPTIONS
# anchor = nw
# side = top, bottom, left, right
# fill
# padx
# pady
root.geometry("1200x600")
root.title('Pritha')


title_label = Label(text = "Pritha", padx=25, pady=50, bg='brown', fg = 'white', font=('comicsansms',20, "bold"), borderwidth=3, relief=SUNKEN)
title_label.pack(side=TOP, anchor="nw", fill=X)

image = Image.open(r"D:\SY MSc DS & BDA\Sem III\Mini Project\GUI\paper_texture296.jpg")
photo = ImageTk.PhotoImage(image = image)
photo_label = Label(image=photo)
photo_label.pack()


root.mainloop()