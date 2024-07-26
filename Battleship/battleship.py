from tkinter import *
import keyboard
import random
import time

def start():
    i = 0
    e = 0
    f = 0
    g = 0
    mem1 = 0
    blink = 0
    lineInc = 0
    enemyX = 0
    enemyY = 0
    hitnum = 0
    # Used to check if touching returns t/f, 100 is arbitrary
    falCheck = 100
    targ = [0 , 0]
    aim = []
    linesH = []
    linesV = []
    ships = []
    shipsLoc = []
    enemyLoc = []
    mem = []
    Emem = []
    possSpot = []
    health = [2, 3, 3, 4, 5]
    ehealth = [2, 3, 3, 4, 5]
    hit = False
    miss = False
    ehit = 0
    turn = True
    enter = False
    touching = False
    keyDown = False
    rotate = False
    loose = False

                

main = Tk()
main.title("Battleship!")
startButton = Button(main, bg = "grey", text = "START", command = start)
title = Text(main, width = 10, height = 1, relief = RAISED)
title.insert(INSERT, "BATTLESHIP")
title.config(state= DISABLED)

title.pack()
startButton.pack()
main.mainloop()
