from tkinter import *
root = Tk()
#Width x Height
root.geometry("500x500")
root.title("My first app")
#Width , Height
root.maxsize(800,800)
root.minsize(100,100)
def my_func1():
    data = lb.cget('text')
    data += 1
    lb.config(text = data,fg = 'red')
def my_func2():
    data = lb.cget('text')
    data -= 1
    lb.config(text = data,fg = "green")
lb = Label(root,text = 0)
lb.pack()
bt1 = Button(root,text=" + ",command = my_func1)
bt1.pack()
bt2 = Button(root,text=" - ",command = my_func2)
bt2.pack()
root.mainloop()