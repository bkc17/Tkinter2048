import tkinter as tk
from enum import Enum
from time import sleep
import random
import game


class game_GUI(tk.Canvas):

    score_font = ("Comic Sans MS", 25, "bold")
    game_end_font = ("Comic Sans MS", 35, "bold")
    box_coords = []
    val_coords = []
    score = 0
    class game_colour_list_enum(Enum):
        grey = "#6B6C6E"
        game_bg = "#BBADA0"
        disabled_tile = "#CDC1B4"

    #below dictionary stores the tile colour and text colour for each number
    tile_colour = {
        0: ["#CDC1B4", "#CDC1B4"],
        2: ["#EEE4DA", "#776E65"],
        4: ["#EEE1C9", "#776E65"],
        8: ["#F3B27A", "white"],
        32: ["#EC775B","white"],
        16: ["#F4965C","white"],
        32: ["#EC775B","white"],
        64: ["#F16032","white"],
        128: ["#EDB141","white"],
        256: ["#EEC967","white"],
        512: ["#DBBA24","white"],
        1024: ["#E8BD36","white"],
        2048: ["#E8BF0A","white"],
    }

    def __init__(self):
        super().__init__(width = 600, height = 600, background = "black", highlightthickness = 0) 
        #we inherited the canvas class into our game gui class, so for init,... 
        #...super().__init__ just uses the init of the canvas class from tkinter

        #highlightthickeness is the thickness of the canvas which is by default 1...
        #...and it shows up as a white border so we set it to 0 because we don't want it.


        #below code stores the coordinates of each box in our grid
        for y in range(4):
            for x in range(4):
                self.box_coords.append([x*100+104, y*100+104, x*100+200, y*100+200])
                self.val_coords.append([x*100 +150, y*100 + 150])     
        
        self.draw_grid()

        

    def delete_box(self, tags):
        """This function deletes objects from the canvas

        Args:
            tags (list): Tags of objects to delete
        """
        for tag in tags:
            self.delete(tag)

    def draw_grid(self):
        """This is a function that will draw the base grid of the game, this grid will not change.
        """        
        self.create_rectangle((94, 94, 510, 510), disabledfill = self.game_colour_list_enum.game_bg.value, state = "disabled", width  = 2, tags = "baserec1")

        for coord in self.box_coords:
            self.create_rectangle(coord, disabledfill = self.game_colour_list_enum.disabled_tile.value, width = 2, state = "disabled", tags = ("baserec2"))


    def game_ended(self, highest_number):
        """Prints a screen after a game ends

        Args:
            highest_number ([int]): The highest number reached in the game 
        """
        self.delete_box(["baserec1", "baserec2", "rec", "val", "scoreText", "scoreVal"])
        self.config(background = "dark blue")
        self.create_text(300, 260, font = self.score_font, text = "Highest Number: ", fill = "white")
        self.create_text(300, 320, font = self.game_end_font, text = str(highest_number), fill = "red")

    def print_new_grid(self, values):
        """This is a function that will insert a box with a particular text and colour depending on the text

        Args:
            values (list): List of all tile values
        """
        self.delete_box(["val", "rec", "scoreVal"]) #deleting the old boxes and text

        score = sum(values)
        self.create_text(70, 50, fill = "white", font = ("Times New Roman", 15), text = "SCORE: ", tags = "scoreText")
        self.create_text(115, 50, fill = "yellow", font = ("Times New Roman", 15), text = str(score), tags = "scoreVal")
        
        for x in range(16):
            self.create_rectangle(self.box_coords[x],width = 2, state = "normal", tags = ("rec"), fill = self.tile_colour.get(values[x])[0])
            self.create_text(self.val_coords[x][0], self.val_coords[x][1], fill = self.tile_colour.get(values[x])[1], font = self.score_font, text = values[x], tags = ("val"))
            


        
    

root = tk.Tk()
root.title("2048 game")
root.resizable(False, False)
high_score = 0
board = game_GUI()
board.pack() #this puts the canvas into the window
# values = [0, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 0, 4, 2, 2]
# while(True):
#     inp = input("What? \n")
#     if (inp == "y"):
#         board.print_new_grid(values)
#     random.shuffle(values)

grid = game.startGame()
board.print_new_grid(grid)
try:
    while(game.endGame(grid) == False):
        high_score = max(grid)
        inp = input("Move? \n")
        if inp == "a":
            if(game.moveLeft(grid)):
                game.makeMove(grid)
            else:
                print("Make a valid move!!")
                print("")
        
        elif inp == "d":
            if(game.moveRight(grid)):
                game.makeMove(grid)
            else:
                print("Make a valid move!!")
                print("")

        elif inp == "w":
            if(game.moveUp(grid)):
                game.makeMove(grid)
            else:
                print("Make a valid move!!")
                print("")

        elif inp == "s":
            if(game.moveDown(grid)):
                game.makeMove(grid)
            else:
                print("Make a valid move!!")
                print("")
        elif inp == "quit":
            pass
        board.print_new_grid(grid)

    print("Your game has ended!")
except KeyboardInterrupt:
    board.game_ended(high_score)
board.game_ended(high_score)
root.mainloop()
