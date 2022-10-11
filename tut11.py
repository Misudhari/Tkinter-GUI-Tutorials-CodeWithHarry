from tkinter import *

root = Tk()
root.geometry("1200x600")

# functions
def getvals():
    print("it works")


# Heading
Label(root, text = "Welcome to Chaudhari Travels", font="comicsnsms 13 bold", pady=15).grid(row=0, column=3)

# Text for our form
name = Label(root, text=  "Name")
phone = Label(root, text="Phone")
gender = Label(root, text="Gender")
emergency_Contact = Label(root, text="Emergency Contact")
payment = Label(root, text="Payment Mode")

# Pack text using grid
name.grid(row=1,column=2)
phone.grid(row=2,column=2)
gender.grid(row=3,column=2)
emergency_Contact.grid(row=4,column=2)
payment.grid(row=5,column=2)

# Tkinter variables for storing values
namevalue = StringVar()
phonevalue = StringVar()
gendervalue = StringVar()
emergency_Contactvalue = StringVar()
paymentvalue = StringVar()
foodservicevalue = IntVar()

# Entries for our form
nameentry = Entry(root, textvariable=namevalue)
phoneentry = Entry(root, textvariable=phonevalue)
genderentry = Entry(root, textvariable=gendervalue)
emergency_Contactentry = Entry(root, textvariable=emergency_Contactvalue)
paymententry = Entry(root, textvariable=paymentvalue)

# Packing the entries
nameentry.grid(row = 1, column = 3)
phoneentry.grid(row = 2, column = 3)
genderentry.grid(row = 3, column = 3)
emergency_Contactentry.grid(row = 4, column = 3)
paymententry.grid(row = 5, column = 3)

# checkbox
foodservice = Checkbutton(text = "Want to prebook your meals", variable=foodservicevalue)
foodservice.grid(row=6, column=3)

# Button and packing it and assigning a command
Button(text="Submit to Chaudhari Travels", command=getvals).grid(row = 7, column= 3)
root.mainloop()