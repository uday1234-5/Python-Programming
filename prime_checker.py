from tkinter import *
                                    
class primechecker:
    def __init__(self,mainwindow):
        self.mainwindow = mainwindow
        self.mainwindow.geometry('500x200')
        lb = Label(mainwindow, text = 'Enter the Number', fg='red',bg='yellow')
        lb.pack()
        self.name = Entry(mainwindow)
        self.name.pack()
        self.name1 = Entry(mainwindow)
        self.name1.pack()
        bt = Button(mainwindow, text='Enter',fg='black', bg='light green',command=self.action)
        bt.pack()
        
        self.out = Label(self.mainwindow, text='', fg='red',bg='black')
        self.out.pack()
        self.name.delete(0,END)
        
        
    def action(self):
        data = self.name.get()
        x=0
        if int(data)>1:
            for i in range(2,int(data)):
                if int(data)%i==0:
                    x+=1
        if x==0:
            self.out.config(bg='yellow',text=f'{data} is a prime no. ')
        else:
            self.out.config(bg='yellow',text=f'{data} is a not a prime no. ')

# MAIN - CODE
root = Tk()
root.configure(background='black')
exe = primechecker(root)
root.mainloop()
