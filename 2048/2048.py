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
    field = Canvas(main, width = 425, height = 425, bg = "lightgrey")
    scoreboard = Text(main, relief= RAISED, height = 1, width = 37, padx = 3)
    scoreboard.insert(INSERT, "Score: ")
    scoreboard.insert(INSERT, score)
    scoreboard.tag_add("yourScore", 1.8, 1.9)
    scoreboard.tag_config("yourScore", foreground= "green")
    scoreboard.config(state = DISABLED)

    h1 = field.create_rectangle(0, 2, 425, 7, fill="grey", outline="grey")
    h2 = field.create_rectangle(0, 105, 425, 110, fill="grey", outline="grey")
    h3 = field.create_rectangle(0, 210, 425, 215, fill="grey", outline="grey")
    h4 = field.create_rectangle(0, 315, 425, 320, fill="grey", outline="grey")
    h5 = field.create_rectangle(0, 420, 425, 425, fill="grey", outline="grey")
    v1 = field.create_rectangle(2, 0, 7, 425, fill="grey", outline="grey")
    v2 = field.create_rectangle(105, 0, 110, 425, fill="grey", outline="grey")
    v3 = field.create_rectangle(210, 0, 215, 425, fill="grey", outline="grey")
    v4 = field.create_rectangle(315, 0, 320, 425, fill="grey", outline="grey")
    v5 = field.create_rectangle(420, 0, 425, 425, fill="grey", outline="grey")

    title.pack_forget()
    startButton.pack_forget()
    botButton.pack_forget()
    scoreboard.pack()
    field.pack()

    while loose == False:
        tile.append(field.create_rectangle(7, 7, 105, 105))
        if random.randint(1, 4) == 4:
            tileNum.append(4)
            field.itemconfig(tile[n], fill = "orange")
        else: 
            tileNum.append(2)
            field.itemconfig(tile[n], fill = "white")
        field.update()
def bot():
    field = Canvas(main, width = 350, height = 350, bg = "orange")
    title.pack_forget()
    startButton.pack_forget()
    botButton.pack_forget()
    field.pack()

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
