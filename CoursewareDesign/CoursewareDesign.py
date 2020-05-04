# -*- coding=utf-8 -*-

# we generate teaching-plans by random function
import os, sys, re, random

tipsFile = open('CoursewareDesign/teachingTips.txt', encoding='utf-8')
teachTips = [ ]
begin = 9
going = 4
for line in tipsFile:
    teachTips.append(line)
tipsCounts = len(teachTips)

# we need a file to save the result autoly
designOutput = open('CoursewareDesign/tipsOutput.txt', 'w', encoding='utf-8')


# maybe we can make a generator, but now let's just take easy
beginNum = random.randint(0,begin-1)
begintips = teachTips[beginNum]
#designOutput.write("时间分配\n5分钟。\n")
designOutput.write(begintips)
del teachTips[beginNum]
tipsCounts = tipsCounts - 1

if beginNum < going - 1:
    going = 3

timeCounts = 85
while timeCounts > 0:
   # for x in range (0, 10, 1):
   #     designOutput.write('\n')
    if timeCounts == 5: 
        time = 5
    elif random.randint(0,10) > 6:
        time = 10
    else: time = 5
    timeCounts = timeCounts - time
    #designOutput.write("时间分配\n"+str(time) + "分钟。\n")
    goingNum = random.randint(going - 1, tipsCounts - 1)
    goingtip = teachTips[goingNum]
    designOutput.write(goingtip)
    del teachTips[goingNum]
    tipsCounts = tipsCounts - 1
    
designOutput.close()