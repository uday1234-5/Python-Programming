from tkinter import *
root = Tk()
root.geometry("300x300")
root.maxsize = (800,800)
root.minsize = (200,200)
root.title("Counter App")

lb = Label(root,text = 0,font=('comicsansms',70,'bold'))
lb.pack()

#action
def increment():
    data = lb.cget('text')
    data += 1
    if data >= 10:
        lb.config(text = data,fg = 'red')
    else:
        lb.config(text = data,fg = 'green')
def decrement():
    data = lb.cget('text')
    data -= 1
    if data >= 0:   
        lb.config(text = data)
    if data >= 10:
        lb.config(fg = 'red')
    else:
        lb.config(fg = 'green')

bt1 = Button(root,text="Increment",command = increment,bg = "pink")
bt1.pack(side = LEFT,ipadx = 10,ipady = 10,padx = 10,pady = 10)
bt1 = Button(root,text="decrement",command = decrement,bg = "cyan")
bt1.pack(side = RIGHT,ipadx = 10,ipady = 10,padx = 10,pady = 10)
root.mainloop()