import tkinter as tk
from enum import Enum
from time import sleep

class game_GUI(tk.Canvas):

    score_font = ("Comic Sans MS", 40, "bold")
    box_coords = []
    class colour_list_enum(Enum):
        grey = "#6B6C6E"
        game_bg = "#BBADA0"
        disabled_tile = "#CDC1B4"
        tile_2 = "#EEE4DA"
        tile_4 = "#EEE1C9"
        tile_8 = "#F3B27A"
        tile_16 = "#F4965C"
        tile_32 = "#F4759"
        tile_64 = "#F16032"
        tile_128 = "#EDB141"
        tile_256 = "#EEC967"
        tile_512 = "#DBBA24"
        tile_1024 = "#E8BD36"
        tile_2048 = "#E8BF0A"

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
        

        self.draw_grid()

    def draw_grid(self):
        """This is a function that will draw the base grid of the game, this grid will not change.
        """        
        self.create_rectangle((94, 94, 510, 510), disabledfill = self.colour_list_enum.game_bg.value, state = "disabled", width  = 2)
        count = 0
        for coord in self.box_coords:
            self.create_rectangle(coord, disabledfill = self.colour_list_enum.disabled_tile.value, width = 2, state = "disabled", tags = ("rec" + str(count)))
            count += 1
            #self.create_text(250, 150, fill = self.colour_list_enum.grey.value, font = self.score_font, text = 2, tags = "text")

    
    def insert_box(self, values):
        """This is a function that will insert a box with a particular text and colour depending on the text

        Args:
            values ([type]): [description]
        """
        pass
    

root = tk.Tk()
root.title("2048 game")
root.resizable(False, False)

board = game_GUI()
board.pack() #this puts the canvas into the window

root.mainloop()
