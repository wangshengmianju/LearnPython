# -*- coding=utf-8 -*-
#this pro is to work on a PC alone

# we generate teaching-plans by random function
import os, sys, re, random
from tkinter import *
from tkinter.scrolledtext import ScrolledText

Returns = 10
base_dir = os.path.dirname(__file__)   #get current path
tipsFile = open(base_dir+'/teachingTips.txt', encoding='utf-8')
teachTips = [ ]
begin = 9
going = 4
for line in tipsFile:
    teachTips.append(line)

def generateTips(tipsCounts,begin,going,teachTips):
    # we need a file to save the result autoly
    designOutput = open(base_dir+'/tipsOutput.txt', 'w', encoding='utf-8')

    # maybe we can make a generator, but now let's just take easy
    teachTips1 = teachTips.copy()
    beginNum = random.randint(0, begin-1)
    begintips = teachTips1[beginNum]
    designOutput.write("时间分配\n5分钟。\n")
    designOutput.write(begintips)
    del teachTips1[beginNum]
    tipsCounts = tipsCounts - 1

    if beginNum < going - 1:
        going = 3
    timeCounts = 85
    while timeCounts > 0:
        for x in range (0, Returns, 1):
           designOutput.write('\n')
        if timeCounts == 5: 
            time = 5
        elif random.randint(0,10) > 6:
            time = 10
        else: time = 5
        timeCounts = timeCounts - time
        designOutput.write("时间分配\n"+str(time) + "分钟。\n")
        tipsCounts = tipsCounts - 1
        goingNum = random.randint(going-1, tipsCounts-1)
        goingtip = teachTips1[goingNum]
        designOutput.write(goingtip)
        del teachTips1[goingNum]
        tipsCounts = tipsCounts - 1
    
    designOutput.close()

def showTips():
    global Returns,begin,going 
    Returns = int(blacklineSet.get())
    begin = int(beginSet.get())
    going = int(goingSet.get())
    tipsCounts = len(teachTips)
    generateTips(tipsCounts,begin,going,teachTips)
    with open(base_dir+'/tipsOutput.txt',encoding='utf-8') as file:
        contents.delete('1.0',END)
        contents.insert(INSERT, file.read())

top = Tk()
top.title('CoursewareDesignGenerator')

contents = ScrolledText()
contents.pack(side=BOTTOM, expand=True, fill=BOTH)

Button(text='generate', command=showTips, fg='white', bg='red', font=('Arial',12)).pack(side=RIGHT,expand=0)

container1 = Frame()
container1.pack(side=LEFT,expand=0)

Label(master=container1,text='how many begins do you have?').pack(expand=0,anchor='nw')
Label(master=container1,text='where does the body begin?').pack(expand=0,anchor='w')
Label(master=container1,text='how many blacklines do you want?').pack(expand=0,anchor='sw')
beginSet = Entry()
beginSet.insert(0, '9')
beginSet.pack(expand=0,anchor='n')
goingSet = Entry()
goingSet.insert(0, '4')
goingSet.pack(expand=0,anchor='center')
blacklineSet = Entry()
blacklineSet.insert(0, '10')
blacklineSet.pack(expand=0,anchor='s')

top.mainloop()