import tkinter as tk

root = tk.Tk()
root.title("To Do List")
root.geometry("300x300")

def additem():
    data = entry.get()
    list_box.insert(tk.END,data)
    entry.delete(0,tk.END)
def deleteitem():
    select_item = list_box.curselection()
    list_box.delete(select_item)
def deleteitemall():
    list_box.delete(0,tk.END)

entry = tk.Entry(root)
entry.grid(row=0,column=0)

bt_add = tk.Button(root, text='Add Item',command=additem)
bt_add.grid(row=0,column=1)

list_box = tk.Listbox(root,width=20)
list_box.grid(row=1,column=0,columnspan=2)

bt_delete = tk.Button(root,text='Delete Item',command=deleteitem)
bt_delete.grid(row=2,column=0)

bt_delete_all = tk.Button(root,text='Delete All Item',command=deleteitemall)
bt_delete_all.grid(row=2,column=1)

root.mainloop()