from tkinter import *
from PIL import Image, ImageTk

root = Tk()

canvas_width = 1200
canvas_height = 600

root.geometry(f"{canvas_width}x{canvas_height}")


# for jpg
image = Image.open(r"D:\SY MSc DS & BDA\Sem III\Mini Project\GUI\paper_texture296.jpg")
photo = ImageTk.PhotoImage(image = image)
photo_label = Label(image=photo)
photo_label.pack()

# can_widget = Canvas(root, width=canvas_width, height=canvas_height)
# can_widget.pack()
#
#
# can_widget.create_line(580,0,580,600, fill = "white")
# can_widget.create_line(620,0,620,600, fill = "white")

root.mainloop()