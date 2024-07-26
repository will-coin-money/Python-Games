from tkinter import *
import keyboard
import random
import time

def play():
    score = 0
    n = 0
    tile = []
    tileNum = []
    loose = False
    

    while loose == False:
        config(tile[n], fill = "white")



main = Tk()
main.title("2048!")
startButton = Button(main, bg = "orange", text = "PLAY", command = play)
botButton = Button(main, bg = "lightgreen", text = "RUN BOT", command = bot)
title = Text(main, width = 10, height = 1, relief = RAISED)
title.insert(INSERT, "2048!")
title.config(state= DISABLED)

title.pack()
startButton.pack()
botButton.pack()
main.mainloop()
