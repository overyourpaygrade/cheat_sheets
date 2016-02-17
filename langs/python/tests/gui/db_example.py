from tkinter import *
from tkinter import ttk
import sqlite3

con = sqlite3.connect('test.db')
cur = con.cursor()
#cur.execute('drop table if exists data')
cur.execute('create table if not exists data(t1 TEXT, i1 INT)')
con.commit()
print('DB created')

def savedata(text1, int1):
    con = sqlite3.connect('test.db')
    cur = con.cursor()
    cur.execute('INSERT INTO data (t1, i1) VALUES (?,?)', (text1, int1))
    con.commit()
    print('record inserted in data')

# Initialize
root = Tk()
root.title("Little Program To Save Data")

# This is the geomery of the box
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column = 0, row = 0, sticky = (N,W,E,S))
mainframe.columnconfigure(0, weight = 1)
mainframe.rowconfigure(0, weight = 1)

# This is the top field TXT
text1 = StringVar()
text_entry = ttk.Entry(mainframe, width = 20, textvariable=text1)
text_entry.grid(column = 2, row = 1, sticky = (N,W,E,S))

# This is the second field INT
int1 = IntVar()
int_entry = ttk.Entry(mainframe, width = 20, textvariable=int1)
int_entry.grid(column = 2, row = 2, sticky = (N,W,E,S))

# The save button and the action to take
ttk.Button(mainframe, text = "Save!", command= lambda: \
    savedata(text1.get(), int1.get())).grid(column = 3, row = 3, sticky = (W, E))

# No Clue
for child in mainframe.winfo_children(): 
    child.grid_configure(padx = 5, pady = 5)

# Start!
root.mainloop()
