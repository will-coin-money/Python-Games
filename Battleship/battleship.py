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
    stop = False
    down = False
    reticleImage = PhotoImage(file = r'c:\Users\EJMarine2024\Desktop\Battleship\reticle.png')
    blank = PhotoImage(file = r'c:\Users\EJMarine2024\Desktop\Battleship\blank.png')

    field = Canvas(main, width = 270, height = 530, bg = "navy")
    b1 = field.create_rectangle(1, 1, 270, 10, fill="grey", outline="grey")
    b2 = field.create_rectangle(1, 1, 10, 530, fill="grey", outline="grey")
    b3 = field.create_rectangle(1, 259, 270, 270, fill="grey", outline="grey")
    b4 = field.create_rectangle(259, 1, 271, 530, fill="grey", outline="grey")
    b5 = field.create_rectangle(1, 519, 270, 531, fill="grey", outline="grey")
    b6 = field.create_rectangle(11, 11, 258, 258, fill="lightgrey", outline="lightgrey")
    
    # Creating Gridlines for the Bottom Square
    while i < 9:
        linesH.append(i)
        lineInc = 294 + (i * 25)
        linesH[i] = field.create_rectangle(10, lineInc, 260, lineInc + 1, fill="grey", outline = "grey")
        i = i + 1
    i = 0
    while i < 9:
        linesV.append(i)
        lineInc = 34 + (i * 25)
        linesV[i] = field.create_rectangle(lineInc, 270, lineInc + 1, 520, fill="grey", outline = "grey")
        i = i + 1
    i = 0
    linesH = []
    linesV = []
    # Creating Gridlines for the Top Square
    while i < 9:
        linesH.append(i)
        lineInc = 34 + (i * 25)
        linesH[i] = field.create_rectangle(10, lineInc, 260, lineInc + 1, fill="grey", outline = "grey")
        i = i + 1
    i = 0
    while i < 9:
        linesV.append(i)
        lineInc = 34 + (i * 25)
        linesV[i] = field.create_rectangle(lineInc, 10, lineInc + 1, 260, fill="grey", outline = "grey")
        i = i + 1
    i = 0

    instruct = StringVar()
    inst = Text(main, relief= RAISED, height = 3, width = 37, padx = 3)
    inst.insert(INSERT, "Place your Ships! \nUse the arrow keys \nto move the ship and '/' to rotate!")
    inst.config(state = DISABLED)

    

                

main = Tk()
main.title("Battleship!")
startButton = Button(main, bg = "grey", text = "START", command = start)
title = Text(main, width = 10, height = 1, relief = RAISED)
title.insert(INSERT, "BATTLESHIP")
title.config(state= DISABLED)

title.pack()
startButton.pack()
main.mainloop()
