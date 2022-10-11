from tkinter import *

root = Tk()

canvas_width = 1200
canvas_height = 600

root.geometry(f"{canvas_width}x{canvas_height}")
root.title("Title")

can_widget = Canvas(root, width=canvas_width, height=canvas_height)
can_widget.pack()

# The line goes from point x1, y1 to x2,y2
can_widget.create_line(580,0,580,600, fill = "red")
can_widget.create_line(620,0,620,600, fill = "red")

# Top left, bottom right
can_widget.create_rectangle(3,5,700,300, fill="blue")

can_widget.create_text(600,300, text = "Pritha", fill="red")

can_widget.create_oval(344,233,244,455)
root.mainloop()
