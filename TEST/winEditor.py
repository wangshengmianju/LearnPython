import os
from tkinter import *
from tkinter.scrolledtext import ScrolledText

base_dir = os.path.dirname(__file__)   #get current path

def load():
    with open(os.path.join(base_dir, filename.get())+'.txt') as file:
        contents.delete('1.0',END)
        contents.insert(INSERT,file.read())

def save():
    with open(os.path.join(base_dir, filename.get())+'.txt',"w") as file:
        file.write(contents.get('1.0',END))
top = Tk()
top.title('Simple Editor')

contents = ScrolledText()
contents.pack(side=BOTTOM, expand=True, fill=BOTH)

filename = Entry()
filename.pack(side=LEFT, expand=TRUE, fill=X)

Button(text='Open',command=load).pack(side=LEFT)
Button(text='save',command=save).pack(side=RIGHT)

top.mainloop()