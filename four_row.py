

import os
import time

gw = False

def cls():
    os.system('clear||cls')
#Check vertical 4 in a row.
def check_ver():
    for row in range(6):
        xCounter = 0
        for col in range(5):
            if (grid[col][row] == "X"):
                xCounter += 1
        if xCounter == 4:
            xw()
    for row in range(6):
        oCounter = 0
        for col in range(5):
            if (grid[col][row] == "O"):
                oCounter += 1
        if oCounter == 4:
            ow()
#Check horizontal 4 in a row.
def check_hor():
    for col in range(5):
        xCounter = 0
        for row in range(6):
            if (grid[col][row] == "X"):
                xCounter += 1
            if xCounter == 4:
                xw()
    for col in range(5):
        oCounter = 0
        for row in range(6):
            if (grid[col][row] == "O"):
                oCounter += 1
            if oCounter == 4:
                xw()
#Checks all
def check_all():
    check_ver()
    check_hor()
#Checks for win, prints the game
def p():
    cls()
    check_all()
    for x in range(5):
        print(*grid[x], sep=" | ")
    for x in range(2):
        print(*info[x], sep=" | ")
#Empty prints for victory message
def em():
    for x in range(3):
        print("")
#Victory message and stuff for O
def ow():
    
    em()
    print("O, Wins!".center(16))
    em()
    print('Back to Home')
    from four_row_menu import four_row_main
    four_row_main()
    cls()
    gw = True

#Victory message and stuff for X
def xw():
    
    em()
    print("X, Wins!".center(16))
    em()
    print('Back to Home')
    
    time.sleep(3)
    from four_row_menu import four_row_main
    four_row_main()
    cls()
    gw = True
#Grid system
grid = [['.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]
info = [['==+===+===+===+===+=='],
        ['1', '2', '3', '4', '5', '6']]
#Game
while True:
    if gw == True:
        break
    else:
        p()
        try:
            row = int(input("X, column: "))
            row -= 1
        except ValueError:
            em()
            print('Wrong Input!! Enter number 1 to 6 only')
            time.sleep(3)
            continue
        
        if 0 > row or row > 6:
            continue
        else:
            for x in range(4, -1, -1):
                if grid[x][row] == '.':
                    grid[x][row] = 'X'
                    break
        p()
        try:
            row = int(input("O, column: "))
            row -= 1
        except ValueError:
            em()
            print('Wrong Input!! Enter number 1 to 6 only')
            time.sleep(3)
            continue
        if 0 > row or row > 6:
            continue
        else:
            for x in range(4, -1, -1):
                if grid[x][row] == '.':
                    grid[x][row] = 'O'
                    break