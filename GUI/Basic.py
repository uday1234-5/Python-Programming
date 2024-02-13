# import tkinter as tk
# root = tk.Tk()
# root.geometry("200x100")
# root.title("First App")
# root.minsize(100,50)
# def my_fun():
#     data = lb.cget('text')
#     if data == "HELLO":
#         lb.config(text = "World")
#     else:
#         lb.config(text = "HELLO")

#     # lb.config(text = "Hi")
# print("JAI SHREE SITARAM")

# lb = tk.Label(root, text = 'My first python output in gui')#Label Class hai
# lb.pack()
# bt = tk.Button(root, text = 'Click Here', command = my_fun)
# bt.pack()

# root.mainloop()


from tkinter import *
root = Tk()
root.geometry("500x500")
root.maxsize(800,800)
root.minsize(500,100)
root.title("Greeting Message")
def my_funct():
    data = lb.cget('text')
    if data == "HELLO":
        lb.config(text="World",fg = 'red')
    else:
        lb.config(text="HELLO")
lb = Label(root,text = "Greeting Message here..",bg="yellow")
lb.pack()
bt = Button(root,text = "Click me",command = my_funct)
bt.pack()
root.mainloop()