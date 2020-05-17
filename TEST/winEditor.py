from tkinter import *
from tkinter.scrolledtext import ScrolledText

def load():
    with open(filename.get()+'.txt') as file:
        contents.delete('1.0',END)
        contents.insert(INSERT,file.read())

def save():
    with open(filename.get()+'.txt','w') as file:
        file.write(contents.get('1.0',END))

top = Tk()
top.title('Simple Editor')

contents = ScrolledText()
contents.pack(side=BOTTOM, expand=True, fill=BOTH)

filename = Entry()
filename.pack(side=LEFT, expand=TRUE, fill=X)

Button(text='Open',command=load).pack(side=LEFT)
Button(text='save',command=save).pack(side=LEFT)

mainloop()