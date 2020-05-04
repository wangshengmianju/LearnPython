# -*- coding: utf-8 -*-

import os, sys, re

fileTobeParered = open('Zero/testtext.txt')  #open file


#read in meassage line by line, but we need to classify the message by dates
messageLog = { }
messageDate = '0'
message = [ ]
pat1 = '([0-9]+ [A-Z][a-z]+) '
pat2 = '谢谢教员'
beginBlock = 0
for line in fileTobeParered:  
    if beginBlock:                  #check if it's a valuable message
        if re.match(pat2, line):    #check if we should end this block
            beginBlock = 0
            message.pop()
            messageLog[messageDate] = message
            continue
        message.append(line)        #this is a valuabel message and we haven't crossed the block
    elif re.match(pat1, line):
        messageDate = re.match(pat1, line).group(1)
        messageLog[messageDate] = [ ]
        beginBlock = 1
    else: pass


#we need a container with names
checkList00 = ['杨昊爸爸','a哥哥']
def addPostfix(name):
    return name + '(家长)\n'
checkList = list(map(addPostfix,checkList00))


#we need a file to save the result autoly
fileToOutput = open('Zero/Outtext.txt','w')
for name in checkList:
    fileToOutput.write(str(messageLog.count(name))+'\n')



print(checkList)
print(messageLog)
