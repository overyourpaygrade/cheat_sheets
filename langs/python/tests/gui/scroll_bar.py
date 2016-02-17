from Tkinter import *

root = Tk()
root.geometry("500x450+500+500")

scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

listbox = Listbox(root, width=100, height=30)
listbox.pack()
# bind listbox to scrollbar
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

with open('test.txt','rb') as f:
    for i in f:
        listbox.insert(END, i)

mainloop()
