
#global variables
size = 4
inp = ""

#Functions
import random

def startGame():
    index = 0
    grid = []
    for _ in range(size**2):
        if (index < (size**2)-1):
            grid.append(0)
        else:
            grid.append(2)
        index = index+1
    return grid

def printGrid(grid):
    index = 0
    for _ in range(size):
        for _ in range(size):
            print(grid[index], end="         ")
            index = index + 1
        print("")
        print("")

#returns a particular column as a list
def getCol(grid, colNum):
    column = []
    index = colNum - 1
    for _ in range(size):
        column.append(grid[index])
        index = index + size
    return column

def rotateAntiClock(grid):
    grid2 = []
    colNum = size
    for _ in range(size):
        col = getCol(grid, colNum)
        for num in col:
            grid2.append(num)
        colNum = colNum-1
    grid[:] = grid2

#returns the number of empty spaces in a given list with a between a starting and ending index inclusive
def empty(row, low_limit, high_limit, index):
    count = 0
    for i in range(low_limit, high_limit):
        if row[i] == 0:
            index.append(i)
            count = count+1
    return count

#gets all the indices in the grid with no values and randomly selects a value between 2 and 4 and adds it to that position in the grid
def addVal(grid):
    rand = random.choice([2, 4])
    index = []
    empty(grid, 0, size**2, index)
    rand2 = random.choice(index)
    grid[rand2] = rand

#arranges all the empty spaces on the right side and all the numbers on the left
def arrange(grid, low_limit, high_limit):
    index = []#will not use this for the arrange function but this is required to call the empty function
    numZero = empty(grid, low_limit, high_limit-1, index)
    count1 = 0
    while count1 <= numZero:
        for i in range(low_limit,high_limit-1):
            if grid[i] == 0:
                grid[i] = grid[i+1]
                grid[i+1] = 0
        count1 = count1+1

def move_row_left(grid, low_limit, high_limit):
    grid_copy = grid[:]
    arrange(grid, low_limit, high_limit)

    for i in range(low_limit, high_limit-1):
        if (grid[i] == grid[i+1]) and (grid[i] != 0):
            grid[i] = 2*grid[i]
            grid[i+1] = 0
    
    arrange(grid, low_limit, high_limit)
    if(grid_copy == grid):
        return False
    return True

#moves the whole grid left
def moveLeft(grid):
    c = False
    changed = False
    #I use "changed" to determine if the grid changed after a move to the left or if the move did not do anything
    for i in range(size):
        low_limit = i*size
        high_limit = low_limit + size
        c = move_row_left(grid, low_limit, high_limit)
        if(c):
            changed = True
    return changed

def moveRight(grid):
    rotateAntiClock(grid)
    rotateAntiClock(grid)
    u = moveLeft(grid)
    rotateAntiClock(grid)
    rotateAntiClock(grid)
    return u

def moveUp(grid):
    rotateAntiClock(grid)
    u = moveLeft(grid)
    rotateAntiClock(grid)
    rotateAntiClock(grid)
    rotateAntiClock(grid)
    return u

def moveDown(grid):
    rotateAntiClock(grid)
    rotateAntiClock(grid)
    rotateAntiClock(grid)
    u = moveLeft(grid)
    rotateAntiClock(grid)
    return u

def endGame(grid):
    grid2 = grid[:]
    if 2048 in grid2:
        return True
    if moveLeft(grid2) == False and moveDown(grid2) == False and moveRight(grid2) == False and moveUp(grid2) == False:
        return True
    elif(inp == "quit"):
        return True
    return False

def makeMove(grid):
    addVal(grid)
    #printGrid(grid)
def instructions():
    print("")
    print("x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x")
    print("")
    print("")
    print("Type 'w', 'a', 's', 'd' and click enter.")
    print("")
    print("To quit the game, type 'quit' and press enter.")
    print("")
    print("To see this message again later in the game, type 'help' and click enter.")
    print("")
    print("")
    print("x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x")
    print("")

#Main code to run the game below

# grid = startGame()
# print("This is the start of the game")
# print("")
# instructions()


# printGrid(grid)
# count = 0
# while(endGame(grid) == False):
#     inp = input("What is your move?")
#     print("")
#     if inp == "a":
#         if(moveLeft(grid)):
#             makeMove(grid)
#         else:
#             print("Make a valid move!!")
#             print("")
    
#     elif inp == "d":
#         if(moveRight(grid)):
#             makeMove(grid)
#         else:
#             print("Make a valid move!!")
#             print("")

#     elif inp == "w":
#         if(moveUp(grid)):
#             makeMove(grid)
#         else:
#             print("Make a valid move!!")
#             print("")

#     elif inp == "s":
#         if(moveDown(grid)):
#             makeMove(grid)
#         else:
#             print("Make a valid move!!")
#             print("")
#     elif inp == "quit":
#         pass
#     elif inp == "helo":
#         instructions()
#     count = count+1
#     highest = max(grid)

# print("Your game has ended!")
# print("")
# print("Your score is: " + str(count) + " moves and the highest number you got is: " + str(highest))