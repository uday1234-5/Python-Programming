from tkinter import *
root = Tk()

root.geometry("1000x70")
root.title("My first App")
root.maxsize(400,700)
root.minsize(100,200)
def my_func():
    pass
y = Label(root,text="How are you")
y.pack()
x = Button(root,text="Click me",command = my_func)
x.pack()
y.config(Text = "I am fine")
print("Uday kushwah")
root.mainloop()
