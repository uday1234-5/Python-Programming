from tkinter import *

root = Tk()

root.geometry("1000x70")
root.title("My first App")
root.maxsize(400,700)
root.minsize(100,200)

photo = PhotoImage(file="ima.png")

# photo.pack()
lb = Label(image = photo)
lb.pack()

root.mainloop()
