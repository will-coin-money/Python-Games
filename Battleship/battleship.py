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

    title.pack_forget()
    startButton.pack_forget()
    inst.pack()
    field.pack()
    field.update()
    # Placing Ships
    while i < 5:
        ships.append(i)
        # Placing Patrol Boat
        if i == 0:
            ships[i] = field.create_rectangle(11, 271, 33, 318, fill="grey")
            field.update()
            shipsLoc.append([[1, 1],[1, 2]])
            while keyboard.is_pressed("enter") != True:
                if keyboard.is_pressed("up") and shipsLoc[i][0][1] != 1 and keyDown == False:
                    keyDown = True
                    field.move(ships[i], 0, -25)
                    shipsLoc[i][0][1] = shipsLoc[i][0][1] - 1
                    shipsLoc[i][1][1] = shipsLoc[i][1][1] - 1
                    print(shipsLoc[i])
                    field.update()
                elif keyboard.is_pressed("right") and((shipsLoc[i][1][0] != 10 and rotate == True) or (shipsLoc[i][0][0] != 10 and rotate == False)) and keyDown == False:
                    keyDown = True
                    field.move(ships[i], 25, 0)
                    shipsLoc[i][0][0] = shipsLoc[i][0][0] + 1
                    shipsLoc[i][1][0] = shipsLoc[i][1][0] + 1
                    print(shipsLoc[i])
                    field.update()
                elif keyboard.is_pressed("down") and ((shipsLoc[i][1][1] != 10 and rotate == False) or (shipsLoc[i][0][1] != 10 and rotate == True)) and keyDown == False:
                    keyDown = True
                    field.move(ships[i], 0, 25)
                    shipsLoc[i][0][1] = shipsLoc[i][0][1] + 1
                    shipsLoc[i][1][1] = shipsLoc[i][1][1] + 1
                    print(shipsLoc[i])
                    field.update()
                elif keyboard.is_pressed("left") and shipsLoc[i][0][0] != 1 and keyDown == False:
                    keyDown = True
                    field.move(ships[i], -25, 0)
                    shipsLoc[i][0][0] = shipsLoc[i][0][0] - 1
                    shipsLoc[i][1][0] = shipsLoc[i][1][0] - 1
                    print(shipsLoc[i])
                    field.update()
                elif keyboard.is_pressed("/") and keyDown == False:
                    keyDown = True
                    if rotate == False and shipsLoc[i][0][0] != 10:
                        field.coords(ships[i], field.coords(ships[i])[0], field.coords(ships[i])[1], field.coords(ships[i])[0] + 47, field.coords(ships[i])[1] + 22)
                        rotate = True
                        shipsLoc[i][1][0] = shipsLoc[i][0][0] + 1
                        shipsLoc[i][1][1] = shipsLoc[i][0][1]
                        field.update()
                    elif rotate == True and shipsLoc[i][0][1] != 10:
                        field.coords(ships[i], field.coords(ships[i])[0], field.coords(ships[i])[1], field.coords(ships[i])[0] + 22, field.coords(ships[i])[1] + 47)
                        rotate = False
                        shipsLoc[i][1][0] = shipsLoc[i][0][0]
                        shipsLoc[i][1][1] = shipsLoc[i][0][1] + 1
                        field.update()
                if keyboard.is_pressed("up") == False and keyboard.is_pressed("right") == False and keyboard.is_pressed("down") == False and keyboard.is_pressed("left") == False and keyboard.is_pressed("/") == False:
                    keyDown = False
        # Placing Destroyer and Submarine
        elif i == 1 or i == 2:
            ships[i] = field.create_rectangle(11, 271, 33, 343, fill="grey")
            field.update()
            shipsLoc.append([[1, 1],[1, 2],[1, 3]])
            while enter == False:
                if keyboard.is_pressed("up") and shipsLoc[i][0][1] != 1 and keyDown == False:
                    keyDown = True
                    field.move(ships[i], 0, -25)
                    shipsLoc[i][0][1] = shipsLoc[i][0][1] - 1
                    shipsLoc[i][1][1] = shipsLoc[i][1][1] - 1
                    shipsLoc[i][2][1] = shipsLoc[i][2][1] - 1
                    print(shipsLoc[i], touching)
                    field.update()
                elif keyboard.is_pressed("right") and((shipsLoc[i][2][0] != 10 and rotate == True) or (shipsLoc[i][0][0] != 10 and rotate == False)) and keyDown == False:
                    keyDown = True
                    field.move(ships[i], 25, 0)
                    shipsLoc[i][0][0] = shipsLoc[i][0][0] + 1
                    shipsLoc[i][1][0] = shipsLoc[i][1][0] + 1
                    shipsLoc[i][2][0] = shipsLoc[i][2][0] + 1
                    print(shipsLoc[i], touching)
                    field.update()
                elif keyboard.is_pressed("down") and ((shipsLoc[i][2][1] != 10 and rotate == False) or (shipsLoc[i][0][1] != 10 and rotate == True)) and keyDown == False:
                    keyDown = True
                    field.move(ships[i], 0, 25)
                    shipsLoc[i][0][1] = shipsLoc[i][0][1] + 1
                    shipsLoc[i][1][1] = shipsLoc[i][1][1] + 1
                    shipsLoc[i][2][1] = shipsLoc[i][2][1] + 1
                    print(shipsLoc[i], touching)
                    field.update()
                elif keyboard.is_pressed("left") and shipsLoc[i][0][0] != 1 and keyDown == False:
                    keyDown = True
                    field.move(ships[i], -25, 0)
                    shipsLoc[i][0][0] = shipsLoc[i][0][0] - 1
                    shipsLoc[i][1][0] = shipsLoc[i][1][0] - 1
                    shipsLoc[i][2][0] = shipsLoc[i][2][0] - 1
                    print(shipsLoc[i], touching)
                    field.update()
                elif keyboard.is_pressed("/") and keyDown == False:
                    keyDown = True
                    if rotate == False and (shipsLoc[i][0][0] != 10 and shipsLoc[i][0][0] != 9):
                        field.coords(ships[i], field.coords(ships[i])[0], field.coords(ships[i])[1], field.coords(ships[i])[0] + 72, field.coords(ships[i])[1] + 22)
                        rotate = True
                        shipsLoc[i][1][0] = shipsLoc[i][0][0] + 1
                        shipsLoc[i][1][1] = shipsLoc[i][0][1]
                        shipsLoc[i][2][0] = shipsLoc[i][0][0] + 2
                        shipsLoc[i][2][1] = shipsLoc[i][0][1]
                        field.update()
                    elif rotate == True and (shipsLoc[i][0][1] != 9 and shipsLoc[i][0][1] != 10):
                        field.coords(ships[i], field.coords(ships[i])[0], field.coords(ships[i])[1], field.coords(ships[i])[0] + 22, field.coords(ships[i])[1] + 72)
                        rotate = False
                        shipsLoc[i][1][0] = shipsLoc[i][0][0]
                        shipsLoc[i][1][1] = shipsLoc[i][0][1] + 1
                        shipsLoc[i][2][0] = shipsLoc[i][0][0]
                        shipsLoc[i][2][1] = shipsLoc[i][0][1] + 2
                        field.update()
                elif keyboard.is_pressed("enter") and touching == False:
                    enter = True
                if keyboard.is_pressed("up") == False and keyboard.is_pressed("right") == False and keyboard.is_pressed("down") == False and keyboard.is_pressed("left") == False and keyboard.is_pressed("/") == False:
                    keyDown = False
                # Checks Per Ship
                while e < len(shipsLoc) - 1:
                    # Checks Per Block                  
                    while f < len(shipsLoc[e]):                   
                        if shipsLoc[i][0] == shipsLoc[e][f]:
                            falCheck = falCheck - 1
                            touching = True
                        elif shipsLoc[i][1] == shipsLoc[e][f]:
                            falCheck = falCheck - 1
                            touching = True
                        elif shipsLoc[i][2] == shipsLoc[e][f]:
                            falCheck = falCheck - 1
                            touching = True
                        f = f + 1
                    f = 0
                    e = e + 1
                if falCheck == 100:
                    touching = False
                falCheck = 100
                f = 0
                e = 0


                

main = Tk()
main.title("Battleship!")
startButton = Button(main, bg = "grey", text = "START", command = start)
title = Text(main, width = 10, height = 1, relief = RAISED)
title.insert(INSERT, "BATTLESHIP")
title.config(state= DISABLED)

title.pack()
startButton.pack()
main.mainloop()
