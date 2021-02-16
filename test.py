from tkinter import *
from time import sleep
window = Tk() #starts a window
window.title("2048 Game") #Gives the window a name
window.configure(background = "#000000") #Black background for the window
window.geometry("600x600")
window.resizable(False, False) # prevent window resizing in the x and y axis
c = ["red", "blue", "yellow", "pink"]
x0 = window.winfo_screenwidth()/2
y0 = window.winfo_screenheight()/2


canv = Canvas(window, width = 600, height = 600, bg = "black")
canv.create_rectangle((94, 94, 510, 510), disabledfill ="#bbada0", state = "disabled", width  = 2) 
for y in range(4):
    for x in range(4):
        coords = (x*100+104, y*100+104, x*100+200, y*100+200, )
        canv.create_rectangle(coords, disabledfill = c[x], width = 2, state = "disabled", fill = c[x])
        canv.create_text(250,150,fill="white",font="Times 30 bold",
                        text="2")
canv.pack()
coords = (404, 404, 500, 500)
canv.create_rectangle(coords, disabledfill = "black", width = 2, state = "disabled", fill = "black")

window.mainloop() #Keeps the window running
