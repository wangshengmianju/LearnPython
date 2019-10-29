#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

#function
'''def multiply(x,y,*z):
    M=1
    for i in z:
        M=M*i
    return M*x*y

print(multiply(10,20,0.3))'''

#Hanoi Tower
hanoiSet = set(["A", "B", "C"])
moves = {"moveSteps": 0, "moveAction":[]}
def Hanoi(n):
    if not isinstance(n, int):
        return print("need int, please")
    if n <= 0:
        return print("how many disks are there ?!!")
    Hanoi_iter(n, "A", "C")
    moveActions = "\n".join(moves["moveAction"])
    print("you need %s steps:\n%s" %(moves["moveSteps"], moveActions))
    return

def Hanoi_iter(n,From,To):
    if n == 1:
        moves["moveSteps"] += 1
        return moves["moveAction"].append (From + "--->" + To)
    midTower = list(hanoiSet - set([From, To]))[0]
    Hanoi_iter(n-1, From, midTower)
    moves["moveSteps"] += 1
    moves["moveAction"].append (From + "--->" + To)
    Hanoi_iter(n-1, midTower, To)
    return

Hanoi(6)
