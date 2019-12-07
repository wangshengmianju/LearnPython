#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:beili

# 使用Tkinter前需要先导入
from tkinter import *
from tkinter import ttk
import tkinter 

#先申明随机点名的动作函数
def rollName(*args):
    yourName.set("蒋智")
    return
 
# 第1步，实例化object，建立窗口window,给定窗口的显示标题
window = tkinter.Tk()
window.title('Bingoooooooooo!')
# 第2步，设定窗口大小（长 * 宽）
window.geometry('720x500')
# 第3步，添加主题框架（因为主窗口本身不是主题的一部分，因此建议使用框架来放置内容）,并将其置入。
mainFrame = ttk.Frame(window,padding="3 3 12 12")
mainFrame.grid(column=0, row=0, sticky=(N,W,E,S) )
window.columnconfigure(0,weight=1)
window.rowconfigure(0,weight=1)

# 第4步，在主框架内绘制标签。标签显示变量
yourName = StringVar()
l = ttk.Label(mainFrame, textvariable=yourName, background='green', font=('Arial', 32))
l.grid()
# 说明： bg为背景，font为字体，width为长，height为高，这里的长和高是字符的长和高，比如height=2,就是标签有2个字符这么高
for child in mainFrame.winfo_children(): child.grid_configure(padx=5, pady=5)
# 第6步，主窗口循环显示
window.bind('<Return>', rollName)
window.mainloop()
# 注意，loop因为是循环的意思，window.mainloop就会让window不断的刷新，如果没有mainloop,就是一个静态的window,传入进去的值就不会有循环，mainloop就相当于一个很大的while循环，有个while，每点击一次就会更新一次，所以我们必须要有循环
# 所有的窗口文件都必须有类似的mainloop函数，mainloop是窗口文件的关键的关键。