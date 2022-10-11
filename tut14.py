from tkinter import *

root = Tk()
root.title("Pritha")
root.geometry("1200x600")

def harry(event):
    print(f"You clicked on a button at {event.x}, {event.y}")

widget = Button(root, text = "Click me Please")
widget.pack()

widget.bind('<Button-1>', harry)
widget.bind('<Double-1>', quit)
root.mainloop()