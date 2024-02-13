from tkinter import*
root=Tk()
root.geometry("300x300")
root.maxsize(400,400)
root.minsize(100,100)
#global initialization
var=IntVar(value=0)
root.title("Counter App")
lb1=Label(root,textvariable=var,font=("comicsansms",100,"bold"),fg="green")
lb1.pack()
def my_func1():
    data=lb1.cget("text")+1
    var.set(data)
    if data>=10:
        lb1.config(fg="red")
    else:
        lb1.config(fg="green")

def my_func2():
    data=lb1.cget("text")-1
    if data>=0:
        var.set(data)
    if data>=10:
        lb1.config(fg="red")
    else:
        lb1.config(fg="green")
    
bt1=Button(root,text='Increment',command=my_func1,bg="pink",fg="black",font=("comicsansms",15,"bold"))
bt1.pack(side=LEFT,ipadx=10,ipady=10,padx=10,pady=10)
bt2=Button(root,text='Decrement',command=my_func2,bg="cyan",fg="black",font=("comicsansms",15,"bold"))
bt2.pack(side=RIGHT,ipadx=10,ipady=10,padx=10,pady=10)


root.mainloop()
