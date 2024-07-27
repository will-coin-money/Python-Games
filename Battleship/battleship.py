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
        # Placing Battleship
        elif i == 3:
            ships[i] = field.create_rectangle(11, 271, 33, 368, fill="grey")
            field.update()
            shipsLoc.append([[1, 1],[1, 2],[1, 3],[1, 4]])
            while enter == False:
                if keyboard.is_pressed("up") and shipsLoc[i][0][1] != 1 and keyDown == False:
                    keyDown = True
                    field.move(ships[i], 0, -25)
                    shipsLoc[i][0][1] = shipsLoc[i][0][1] - 1
                    shipsLoc[i][1][1] = shipsLoc[i][1][1] - 1
                    shipsLoc[i][2][1] = shipsLoc[i][2][1] - 1
                    shipsLoc[i][3][1] = shipsLoc[i][3][1] - 1
                    print(shipsLoc[i], touching)
                    field.update()
                elif keyboard.is_pressed("right") and((shipsLoc[i][3][0] != 10 and rotate == True) or (shipsLoc[i][0][0] != 10 and rotate == False)) and keyDown == False:
                    keyDown = True
                    field.move(ships[i], 25, 0)
                    shipsLoc[i][0][0] = shipsLoc[i][0][0] + 1
                    shipsLoc[i][1][0] = shipsLoc[i][1][0] + 1
                    shipsLoc[i][2][0] = shipsLoc[i][2][0] + 1
                    shipsLoc[i][3][0] = shipsLoc[i][3][0] + 1
                    print(shipsLoc[i], touching)
                    field.update()
                elif keyboard.is_pressed("down") and ((shipsLoc[i][3][1] != 10 and rotate == False) or (shipsLoc[i][0][1] != 10 and rotate == True)) and keyDown == False:
                    keyDown = True
                    field.move(ships[i], 0, 25)
                    shipsLoc[i][0][1] = shipsLoc[i][0][1] + 1
                    shipsLoc[i][1][1] = shipsLoc[i][1][1] + 1
                    shipsLoc[i][2][1] = shipsLoc[i][2][1] + 1
                    shipsLoc[i][3][1] = shipsLoc[i][3][1] + 1
                    print(shipsLoc[i], touching)
                    field.update()
                elif keyboard.is_pressed("left") and shipsLoc[i][0][0] != 1 and keyDown == False:
                    keyDown = True
                    field.move(ships[i], -25, 0)
                    shipsLoc[i][0][0] = shipsLoc[i][0][0] - 1
                    shipsLoc[i][1][0] = shipsLoc[i][1][0] - 1
                    shipsLoc[i][2][0] = shipsLoc[i][2][0] - 1
                    shipsLoc[i][3][0] = shipsLoc[i][3][0] - 1
                    print(shipsLoc[i], touching)
                    field.update()
                elif keyboard.is_pressed("/") and keyDown == False:
                    keyDown = True
                    if rotate == False and (shipsLoc[i][0][0] != 8 and shipsLoc[i][0][0] != 9 and shipsLoc[i][0][0] != 10):
                        field.coords(ships[i], field.coords(ships[i])[0], field.coords(ships[i])[1], field.coords(ships[i])[0] + 97, field.coords(ships[i])[1] + 22)
                        rotate = True
                        shipsLoc[i][1][0] = shipsLoc[i][0][0] + 1
                        shipsLoc[i][1][1] = shipsLoc[i][0][1]
                        shipsLoc[i][2][0] = shipsLoc[i][0][0] + 2
                        shipsLoc[i][2][1] = shipsLoc[i][0][1]
                        shipsLoc[i][3][0] = shipsLoc[i][0][0] + 3
                        shipsLoc[i][3][1] = shipsLoc[i][0][1]
                        field.update()
                    elif rotate == True and (shipsLoc[i][0][1] != 8 and shipsLoc[i][0][1] != 9 and shipsLoc[i][0][1] != 10):
                        field.coords(ships[i], field.coords(ships[i])[0], field.coords(ships[i])[1], field.coords(ships[i])[0] + 22, field.coords(ships[i])[1] + 97)
                        rotate = False
                        shipsLoc[i][1][0] = shipsLoc[i][0][0]
                        shipsLoc[i][1][1] = shipsLoc[i][0][1] + 1
                        shipsLoc[i][2][0] = shipsLoc[i][0][0]
                        shipsLoc[i][2][1] = shipsLoc[i][0][1] + 2
                        shipsLoc[i][3][0] = shipsLoc[i][0][0]
                        shipsLoc[i][3][1] = shipsLoc[i][0][1] + 3
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
                        elif shipsLoc[i][3] == shipsLoc[e][f]:
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
        # Placing Aircraft Carrier
        elif i == 4:
            ships[i] = field.create_rectangle(11, 271, 33, 393, fill="grey")
            field.update()
            shipsLoc.append([[1, 1],[1, 2],[1, 3],[1, 4],[1, 5]])
            while enter == False:
                if keyboard.is_pressed("up") and shipsLoc[i][0][1] != 1 and keyDown == False:
                    keyDown = True
                    field.move(ships[i], 0, -25)
                    shipsLoc[i][0][1] = shipsLoc[i][0][1] - 1
                    shipsLoc[i][1][1] = shipsLoc[i][1][1] - 1
                    shipsLoc[i][2][1] = shipsLoc[i][2][1] - 1
                    shipsLoc[i][3][1] = shipsLoc[i][3][1] - 1
                    shipsLoc[i][4][1] = shipsLoc[i][4][1] - 1
                    print(shipsLoc[i], touching)
                    field.update()
                elif keyboard.is_pressed("right") and((shipsLoc[i][4][0] != 10 and rotate == True) or (shipsLoc[i][0][0] != 10 and rotate == False)) and keyDown == False:
                    keyDown = True
                    field.move(ships[i], 25, 0)
                    shipsLoc[i][0][0] = shipsLoc[i][0][0] + 1
                    shipsLoc[i][1][0] = shipsLoc[i][1][0] + 1
                    shipsLoc[i][2][0] = shipsLoc[i][2][0] + 1
                    shipsLoc[i][3][0] = shipsLoc[i][3][0] + 1
                    shipsLoc[i][4][0] = shipsLoc[i][4][0] + 1
                    print(shipsLoc[i], touching)
                    field.update()
                elif keyboard.is_pressed("down") and ((shipsLoc[i][4][1] != 10 and rotate == False) or (shipsLoc[i][0][1] != 10 and rotate == True)) and keyDown == False:
                    keyDown = True
                    field.move(ships[i], 0, 25)
                    shipsLoc[i][0][1] = shipsLoc[i][0][1] + 1
                    shipsLoc[i][1][1] = shipsLoc[i][1][1] + 1
                    shipsLoc[i][2][1] = shipsLoc[i][2][1] + 1
                    shipsLoc[i][3][1] = shipsLoc[i][3][1] + 1
                    shipsLoc[i][4][1] = shipsLoc[i][4][1] + 1
                    print(shipsLoc[i], touching)
                    field.update()
                elif keyboard.is_pressed("left") and shipsLoc[i][0][0] != 1 and keyDown == False:
                    keyDown = True
                    field.move(ships[i], -25, 0)
                    shipsLoc[i][0][0] = shipsLoc[i][0][0] - 1
                    shipsLoc[i][1][0] = shipsLoc[i][1][0] - 1
                    shipsLoc[i][2][0] = shipsLoc[i][2][0] - 1
                    shipsLoc[i][3][0] = shipsLoc[i][3][0] - 1
                    shipsLoc[i][4][0] = shipsLoc[i][4][0] - 1
                    print(shipsLoc[i], touching)
                    field.update()
                elif keyboard.is_pressed("/") and keyDown == False:
                    keyDown = True
                    if rotate == False and (shipsLoc[i][0][0] != 7 and shipsLoc[i][0][0] != 8 and shipsLoc[i][0][0] != 9 and shipsLoc[i][0][0] != 10):
                        field.coords(ships[i], field.coords(ships[i])[0], field.coords(ships[i])[1], field.coords(ships[i])[0] + 122, field.coords(ships[i])[1] + 22)
                        rotate = True
                        shipsLoc[i][1][0] = shipsLoc[i][0][0] + 1
                        shipsLoc[i][1][1] = shipsLoc[i][0][1]
                        shipsLoc[i][2][0] = shipsLoc[i][0][0] + 2
                        shipsLoc[i][2][1] = shipsLoc[i][0][1]
                        shipsLoc[i][3][0] = shipsLoc[i][0][0] + 3
                        shipsLoc[i][3][1] = shipsLoc[i][0][1]
                        shipsLoc[i][4][0] = shipsLoc[i][0][0] + 4
                        shipsLoc[i][4][1] = shipsLoc[i][0][1]
                        field.update()
                    elif rotate == True and (shipsLoc[i][0][1] != 7 and shipsLoc[i][0][1] != 8 and shipsLoc[i][0][1] != 9 and shipsLoc[i][0][1] != 10):
                        field.coords(ships[i], field.coords(ships[i])[0], field.coords(ships[i])[1], field.coords(ships[i])[0] + 22, field.coords(ships[i])[1] + 122)
                        rotate = False
                        shipsLoc[i][1][0] = shipsLoc[i][0][0]
                        shipsLoc[i][1][1] = shipsLoc[i][0][1] + 1
                        shipsLoc[i][2][0] = shipsLoc[i][0][0]
                        shipsLoc[i][2][1] = shipsLoc[i][0][1] + 2
                        shipsLoc[i][3][0] = shipsLoc[i][0][0]
                        shipsLoc[i][3][1] = shipsLoc[i][0][1] + 3
                        shipsLoc[i][4][0] = shipsLoc[i][0][0]
                        shipsLoc[i][4][1] = shipsLoc[i][0][1] + 4
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
                        elif shipsLoc[i][3] == shipsLoc[e][f]:
                            falCheck = falCheck - 1
                            touching = True
                        elif shipsLoc[i][4] == shipsLoc[e][f]:
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
        rotate = False
        enter = False     
        i = i + 1
        time.sleep(.1)
    i = 0
    rotate = False
    # Placing AI Ships
    while i < 5:
        touching = True
        # Placing Patrol Boart
        if i == 0:
            if random.randint(1,2) == 1:
                rotate = False
                enemyX = random.randint(1,9)
                enemyY = random.randint(1,10)
            else: 
                rotate = True
                enemyX = random.randint(1,10)
                enemyY = random.randint(1,9)
            if rotate == False:
                enemyLoc.append([[enemyX, enemyY], [enemyX + 1, enemyY]])
            elif rotate == True:
                enemyLoc.append([[enemyX, enemyY], [enemyX, enemyY + 1]])
        # Placing Submarine and Destroyer
        elif i == 1 or i == 2:
            while touching == True:
                touching = False
                if random.randint(1,2) == 1:
                    rotate = False
                    enemyX = random.randint(1,8)
                    enemyY = random.randint(1,10)
                else: 
                    rotate = True
                    enemyX = random.randint(1,10)
                    enemyY = random.randint(1,8)
                if rotate == False:
                    enemyLoc.append([[enemyX, enemyY], [enemyX + 1, enemyY], [enemyX + 2, enemyY]])
                elif rotate == True:
                    enemyLoc.append([[enemyX, enemyY], [enemyX, enemyY + 1], [enemyX, enemyY + 2]])
                # Checks Per Ship
                while e < len(enemyLoc) - 1:
                    # Checks Per Block                  
                    while f < len(enemyLoc[e]):                   
                        if enemyLoc[i][0] == enemyLoc[e][f]:
                            touching = True
                        elif enemyLoc[i][1] == enemyLoc[e][f]:
                            touching = True
                        elif enemyLoc[i][2] == enemyLoc[e][f]:
                            touching = True
                        f = f + 1
                    f = 0
                    e = e + 1
                f = 0
                e = 0
                if touching == True:
                    enemyLoc.pop(i)
        # Placing Battleship
        elif i == 3:
            while touching == True:
                touching = False
                if random.randint(1,2) == 1:
                    rotate = False
                    enemyX = random.randint(1,7)
                    enemyY = random.randint(1,10)
                else: 
                    rotate = True
                    enemyX = random.randint(1,10)
                    enemyY = random.randint(1,7)
                if rotate == False:
                    enemyLoc.append([[enemyX, enemyY], [enemyX + 1, enemyY], [enemyX + 2, enemyY], [enemyX + 3, enemyY]])
                elif rotate == True:
                    enemyLoc.append([[enemyX, enemyY], [enemyX, enemyY + 1], [enemyX, enemyY + 2], [enemyX, enemyY + 3]])
                # Checks Per Ship
                while e < len(enemyLoc) - 1:
                    # Checks Per Block                  
                    while f < len(enemyLoc[e]):                   
                        if enemyLoc[i][0] == enemyLoc[e][f]:
                            touching = True
                        elif enemyLoc[i][1] == enemyLoc[e][f]:
                            touching = True
                        elif enemyLoc[i][2] == enemyLoc[e][f]:
                            touching = True
                        elif enemyLoc[i][3] == enemyLoc[e][f]:
                            touching = True
                        f = f + 1
                    f = 0
                    e = e + 1
                f = 0
                e = 0
                if touching == True:
                    enemyLoc.pop(i)
        # Placing Aircraft Carrier
        elif i == 4:
            while touching == True:
                touching = False
                if random.randint(1,2) == 1:
                    rotate = False
                    enemyX = random.randint(1,6)
                    enemyY = random.randint(1,10)
                else: 
                    rotate = True
                    enemyX = random.randint(1,10)
                    enemyY = random.randint(1,6)
                if rotate == False:
                    enemyLoc.append([[enemyX, enemyY], [enemyX + 1, enemyY], [enemyX + 2, enemyY], [enemyX + 3, enemyY], [enemyX + 4, enemyY]])
                elif rotate == True:
                    enemyLoc.append([[enemyX, enemyY], [enemyX, enemyY + 1], [enemyX, enemyY + 2], [enemyX, enemyY + 3], [enemyX, enemyY + 4]])
                # Checks Per Ship
                while e < len(enemyLoc) - 1:
                    # Checks Per Block                  
                    while f < len(enemyLoc[e]):                   
                        if enemyLoc[i][0] == enemyLoc[e][f]:
                            touching = True
                        elif enemyLoc[i][1] == enemyLoc[e][f]:
                            touching = True
                        elif enemyLoc[i][2] == enemyLoc[e][f]:
                            touching = True
                        elif enemyLoc[i][3] == enemyLoc[e][f]:
                            touching = True
                        elif enemyLoc[i][4] == enemyLoc[e][f]:
                            touching = True
                        f = f + 1
                    f = 0
                    e = e + 1
                f = 0
                e = 0
                if touching == True:
                    enemyLoc.pop(i)
        print(enemyLoc)
        rotate = False
        i = i + 1
    inst.config(state= NORMAL)
    inst.delete(1.0,3.37)
    inst.config(height = 7)
    inst.insert(INSERT, "Your turn! \nYour ships:     Enemy Ships: \n■ ■             ■ ■\n■ ■ ■           ■ ■ ■\n■ ■ ■           ■ ■ ■\n■ ■ ■ ■         ■ ■ ■ ■\n■ ■ ■ ■ ■       ■ ■ ■ ■ ■")
    # Patrol Boat Health
    inst.tag_add("Pat1", "3.0", "3.1")
    inst.tag_config("Pat1", foreground = "lightgreen")
    inst.tag_add("Pat2", "3.2", "3.3")
    inst.tag_config("Pat2", foreground = "lightgreen")
    # Enemy Patrol Boat Health
    inst.tag_add("EPat1", "3.16", "3.17")
    inst.tag_config("EPat1", foreground = "lightgreen")
    inst.tag_add("EPat2", "3.18", "3.19")
    inst.tag_config("EPat2", foreground = "lightgreen")
    # Submarine Health
    inst.tag_add("Sub1", "4.0", "4.1")
    inst.tag_config("Sub1", foreground = "lightgreen")
    inst.tag_add("Sub2", "4.2", "4.3")
    inst.tag_config("Sub2", foreground = "lightgreen")
    inst.tag_add("Sub3", "4.4", "4.5")
    inst.tag_config("Sub3", foreground = "lightgreen")
    # Enemy Submarine Health
    inst.tag_add("ESub1", "4.16", "4.17")
    inst.tag_config("ESub1", foreground = "lightgreen")
    inst.tag_add("ESub2", "4.18", "4.19")
    inst.tag_config("ESub2", foreground = "lightgreen")
    inst.tag_add("ESub3", "4.20", "4.21")
    inst.tag_config("ESub3", foreground = "lightgreen")
    # Destroyer Health
    inst.tag_add("Des1", "5.0", "5.1")
    inst.tag_config("Des1", foreground = "lightgreen")
    inst.tag_add("Des2", "5.2", "5.3")
    inst.tag_config("Des2", foreground = "lightgreen")
    inst.tag_add("Des3", "5.4", "5.5")
    inst.tag_config("Des3", foreground = "lightgreen")
    # Enemy Destroyer Health
    inst.tag_add("EDes1", "5.16", "5.17")
    inst.tag_config("EDes1", foreground = "lightgreen")
    inst.tag_add("EDes2", "5.18", "5.19")
    inst.tag_config("EDes2", foreground = "lightgreen")
    inst.tag_add("EDes3", "5.20", "5.21")
    inst.tag_config("EDes3", foreground = "lightgreen")
    # Battleshop Health
    inst.tag_add("Bat1", "6.0", "6.1")
    inst.tag_config("Bat1", foreground = "lightgreen")
    inst.tag_add("Bat2", "6.2", "6.3")
    inst.tag_config("Bat2", foreground = "lightgreen")
    inst.tag_add("Bat3", "6.4", "6.5")
    inst.tag_config("Bat3", foreground = "lightgreen")
    inst.tag_add("Bat4", "6.6", "6.7")
    inst.tag_config("Bat4", foreground = "lightgreen")
    # Enemy Battleship Health
    inst.tag_add("EBat1", "6.16", "6.17")
    inst.tag_config("EBat1", foreground = "lightgreen")
    inst.tag_add("EBat2", "6.18", "6.19")
    inst.tag_config("EBat2", foreground = "lightgreen")
    inst.tag_add("EBat3", "6.20", "6.21")
    inst.tag_config("EBat3", foreground = "lightgreen")
    inst.tag_add("EBat4", "6.22", "6.23")
    inst.tag_config("EBat4", foreground = "lightgreen")
    # Aircraft Carrier Health
    inst.tag_add("Air1", "7.0", "7.1")
    inst.tag_config("Air1", foreground = "lightgreen")
    inst.tag_add("Air2", "7.2", "7.3")
    inst.tag_config("Air2", foreground = "lightgreen")
    inst.tag_add("Air3", "7.4", "7.5")
    inst.tag_config("Air3", foreground = "lightgreen")
    inst.tag_add("Air4", "7.6", "7.7")
    inst.tag_config("Air4", foreground = "lightgreen")
    inst.tag_add("Air5", "7.8", "7.9")
    inst.tag_config("Air5", foreground = "lightgreen")
    # Enemy Aircraft Carrier Health
    inst.tag_add("EAir1", "7.16", "7.17")
    inst.tag_config("EAir1", foreground = "lightgreen")
    inst.tag_add("EAir2", "7.18", "7.19")
    inst.tag_config("EAir2", foreground = "lightgreen")
    inst.tag_add("EAir3", "7.20", "7.21")
    inst.tag_config("EAir3", foreground = "lightgreen")
    inst.tag_add("EAir4", "7.22", "7.23")
    inst.tag_config("EAir4", foreground = "lightgreen")
    inst.tag_add("EAir5", "7.24", "7.25")
    inst.tag_config("EAir5", foreground = "lightgreen")
    inst.update()
    inst.config(state= DISABLED)

    reticle = field.create_image(22, 22, image = reticleImage)
    field.pack()
    field.update()

    aim = [1, 1]
    i = 0
    touching = False
    turn = True
    enter = False
    rotate = False
    down = False

    time.sleep(.5)

    # The Actual Game
    while loose == False:
        # Your Turn
        if turn == True:
            while enter == False:
                field.lift(reticle)
                touching = False
                blink = blink + 1
                if blink == 400000:
                    field.itemconfig(reticle, image = blank)
                    field.update()
                elif blink == 600000:
                    field.itemconfig(reticle, image = reticleImage)
                    field.update()
                    blink = 0
                if keyboard.is_pressed("up") and keyDown == False and aim[1] != 1:
                    keyDown = True
                    aim[1] = aim[1] - 1
                    field.move(reticle, 0, -25)
                    print(aim)
                    field.update()
                elif keyboard.is_pressed("right") and keyDown == False and aim[0] != 10:
                    keyDown = True
                    aim[0] = aim[0] + 1
                    field.move(reticle, 25, 0)
                    print(aim)
                    field.update()
                elif keyboard.is_pressed("down") and keyDown == False and aim[1] != 10:
                    keyDown = True
                    aim[1] = aim[1] + 1
                    field.move(reticle, 0, 25)
                    print(aim)
                    field.update()
                elif keyboard.is_pressed("left") and keyDown == False and aim[0] != 1:
                    keyDown = True
                    aim[0] = aim[0] - 1
                    field.move(reticle, -25, 0)
                    print(aim)
                    field.update()
                if keyboard.is_pressed("up") == False and keyboard.is_pressed("right") == False and keyboard.is_pressed("down") == False and keyboard.is_pressed("left") == False and keyboard.is_pressed('enter') == False:
                    keyDown = False
                if keyboard.is_pressed("enter") and keyDown == False:
                    hit = False
                    keyDown = True
                    while i < len(mem):
                        if aim == mem[i]:
                            print(mem)
                            touching = True
                            break
                        i = i + 1
                    if touching == False:
                        enter = True
                        turn = False
                        mem.append(aim)
                        # Checks Per Ship
                        while e < 5 and stop != True:
                        # Checks Per Block                  
                            while f < len(enemyLoc[e]) and stop != True:                   
                                if aim == enemyLoc[e][f]:
                                    hit = True
                                    ehealth[e] = ehealth[e] - 1
                                    field.create_rectangle(field.coords(reticle)[0] - 11, field.coords(reticle)[1] - 11, field.coords(reticle)[0] + 11, field.coords(reticle)[1] + 11, fill = "red", outline = "red")
                                    if e == 0 and ehealth[e] == 1:
                                        inst.tag_config("EPat2", foreground = "red")
                                        stop = True
                                    elif e == 0 and ehealth[e] == 0:
                                        inst.tag_config("EPat1", foreground = "red")
                                        stop = True
                                    elif e == 1 and ehealth[e] == 2:
                                        inst.tag_config("ESub3", foreground = "red")
                                        stop = True
                                    elif e == 1 and ehealth[e] == 1:
                                        inst.tag_config("ESub2", foreground = "red")
                                        stop = True
                                    elif e == 1 and ehealth[e] == 0:
                                        inst.tag_config("ESub1", foreground = "red")
                                        stop = True
                                    elif e == 2 and ehealth[e] == 2:
                                        inst.tag_config("EDes3", foreground = "red")
                                        stop = True
                                    elif e == 2 and ehealth[e] == 1:
                                        inst.tag_config("EDes2", foreground = "red")
                                        stop = True
                                    elif e == 2 and ehealth[e] == 0:
                                        inst.tag_config("EDes1", foreground = "red")
                                        stop = True
                                    elif e == 3 and ehealth[e] == 3:
                                        inst.tag_config("EBat4", foreground = "red")
                                        stop = True
                                    elif e == 3 and ehealth[e] == 2:
                                        inst.tag_config("EBat3", foreground = "red")
                                        stop = True
                                    elif e == 3 and ehealth[e] == 1:
                                        inst.tag_config("EBat2", foreground = "red")
                                        stop = True
                                    elif e == 3 and ehealth[e] == 0:
                                        inst.tag_config("EBat1", foreground = "red")
                                        stop = True
                                    elif e == 4 and ehealth[e] == 4:
                                        inst.tag_config("EAir5", foreground = "red")
                                        stop = True
                                    elif e == 4 and ehealth[e] == 3:
                                        inst.tag_config("EAir4", foreground = "red")
                                        stop = True
                                    elif e == 4 and ehealth[e] == 2:
                                        inst.tag_config("EAir3", foreground = "red")
                                        stop = True
                                    elif e == 4 and ehealth[e] == 1:
                                        inst.tag_config("EAir2", foreground = "red")
                                        stop = True
                                    elif e == 4 and ehealth[e] == 0:
                                        inst.tag_config("EAir1", foreground = "red")
                                        stop = True
                                f = f + 1
                            f = 0
                            e = e + 1
                            if hit == False:
                                field.create_rectangle(field.coords(reticle)[0] - 11, field.coords(reticle)[1] - 11, field.coords(reticle)[0] + 11, field.coords(reticle)[1] + 11, fill = "white", outline = "black")
                        f = 0
                        e = 0
                        stop = False
        # Enemy's Turn
        elif turn == False:
            turn = True
            # Picks Random Target
            if len(Emem) == 0 or ehit == 0:
                aim = [random.randint(1, 10), random.randint(1,10)]
                if len(Emem) != 0:
                    i = 0
                    while i < len(Emem):
                        while aim == Emem[i]:
                            aim = [random.randint(1, 10), random.randint(1,10)]
                            i = -1
                        i = i + 1
            if ehit >= 2 and down == False and rotate == False and Emem[len(Emem) - 1][1] - 1 == 0:
                down = True
            elif ehit >= 2 and down == True and rotate == True and Emem[len(Emem) - 1][0] + 1 == 11:
                down = True
            if ehit == 1:
                if miss == True:
                    g = g + 1
                if g > len(possSpot) - 1:
                    g = 0
                aim = possSpot[g]
                if possSpot[g][0] == 0 or possSpot[g][0] == 11 or possSpot[g][1] == 0 or possSpot[g][1] == 11:
                    g = g + 1
                    aim = possSpot[g]
            elif ehit == 2 and hitnum == 2:
                if Emem[len(Emem) - 1][0] == Emem[len(Emem) - (g + 2)][0]:
                    rotate = False
                elif Emem[len(Emem) - 1][1] == Emem[len(Emem) - (g + 2)][1]:
                    rotate = True
                if Emem[len(Emem)- (g + 2)][0] < Emem[len(Emem) - 1][0] or  Emem[len(Emem)- (g + 2)][1] < Emem[len(Emem) - 1][1] or miss == True or Emem[len(Emem)-1][0] == 1 or Emem[len(Emem)-1][1] == 1:
                    down = True
                if down == False and rotate == False and Emem[len(Emem) - 1][1] - 1 == 0:
                    down = True
                elif down == False and rotate == True and Emem[len(Emem) - 1][0] + 1 == 11:
                    down = True
                if miss == True or (down == False and rotate == False and Emem[len(Emem) - 1][1] - 1 == 0) or (down == True and rotate == True and Emem[len(Emem) - 1][0] + 1 == 11):
                    if rotate == False and down == True:
                        aim = [Emem[mem1][0], Emem[mem1][1] - 1]
                        down = False
                    elif rotate == True and down == True:
                        aim = [Emem[mem1][0] - 1, Emem[mem1][1]]
                        down = False
                    elif rotate == False and down == False:
                        aim = [Emem[mem1][0], Emem[mem1][1] + 1]
                        down = True
                    elif rotate == True and down == False:
                        aim = [Emem[mem1][0] + 1, Emem[mem1][1]]
                        down = True
                elif miss == False:
                    if rotate == False and down == False:
                       aim = [Emem[len(Emem) - 1][0], Emem[len(Emem) - 1][1] - 1]
                    elif rotate == True and down == False:
                        aim = [Emem[len(Emem) - 1][0] - 1, Emem[len(Emem) - 1][1]]
                    elif rotate == False and down == True:
                        aim = [Emem[len(Emem) - 1][0], Emem[len(Emem) - 1][1] + 1]
                    elif rotate == True and down == True:
                        aim = [Emem[len(Emem) - 1][0] + 1, Emem[len(Emem) - 1][1]]


                

main = Tk()
main.title("Battleship!")
startButton = Button(main, bg = "grey", text = "START", command = start)
title = Text(main, width = 10, height = 1, relief = RAISED)
title.insert(INSERT, "BATTLESHIP")
title.config(state= DISABLED)

title.pack()
startButton.pack()
main.mainloop()
