from tkinter import *

root = Tk()
root.title("2048 game")
root.geometry("600x600")
root.resizable(False, False)


count = 0

def something():
    global count
    my_label.config(text = str(count))
    count+=1

my_label = Label(root, text = "terg", )
my_label.pack()

while(True):
    inp = input("WHat?")
    if(inp == "y"):
        something()


root.mainloop()