import os

def clear():
    os.system('clear||cls')

class Board:
    """Setting board game and board game solution for Soduku"""
    def __init__(self):
        self.board = [["*", "*", "*", "1", "*", "8", "*" ,"*", "*"],
         ["2", "8", "*", "3", "*", "5", "*", "*", "*"],
        ["5", "*", "*", "*", "2", "4", "6", "3", "8"],
        ["*", "7", "*", "8", "*", "*", "5", "*", "*"],
        ["4", "*", "*", "9", "1", "6", "*", "*", "3"],
        ["*", "*", "1", "*", "*", "7", "*", "8", "*"],
        ["6", "3", "7", "2", "5", "*", "*", "*", "1"],
        ["*", "*", "*", "6", "*", "3", "*", "7", "9"],
        ["*",  "*", "*", "4", "*", "1", "*", "*", "*"]]

        self.board_solution = [["7", "6", "3", "1", "9", "8", "4" ,"5", "2"],
        ["2", "8", "4", "3", "6", "5", "1", "9", "7"],
        ["5", "1", "9", "7", "2", "4", "6", "3", "8"],
        ["9", "7", "6", "8", "3", "2", "5", "1", "4"],
        ["4", "5", "8", "9", "1", "6", "7", "2", "3"],
        ["4", "2", "1", "5", "4", "7", "9", "8", "6"],
        ["6", "3", "7", "2", "5", "9", "8", "4", "1"],
        ["1", "4", "5", "6", "8", "3", "2", "7", "9"],
        ["8",  "9", "2", "4", "7", "1", "3", "6", "5"]]

    """Setting the user's input of their guesses into the correct row and column"""
    def SetBoard(self, row, item, guess):
        """setting the guess into the row and item"""
        if self.board[row][item] == "*":
            self.board[row][item] = str(guess) 
        else: 
           print("Incorrect placement or not a proper number! Try again! Remember to count from 0?!")  
        
    """"Print out the board in a more visually appealing representation"""           
    def DisplayBoard(self):
        """print the values in the rows"""
        row_string = ''
        for row in self.board:
            for element in row:
                row_string = row_string + ' ' + element
            row_string += '\n'
        print(row_string)

    def Board_not_Full(self):
        """Check if board is full"""
        for row in self.board:
            for item in row:
                if "*" == item:
                    return True
        return False  

class Board_Med(Board):
    """Creating the first subclass of board for a different level of the board game"""
    def __init__(self):
        self.board = [["*", "2", "*", "*", "*", "*", "*", "*", "3"],
        ["3", "6", "*", "*", "7", "1", "4", "5", "*"],
        ["1", "*", "*", "*", "*", "*", "2", "*", "*"],
        ["*", "1", "4", "5", "*", "*", "*", "8", "*"],
        ["*", "*", "3", "*", "6", "*", "5", "*", "*"],
        ["*", "5", "*", "*", "*", "9", "7", "1", "*"],
        ["*", "*", "6", "*", "*", "*", "*", "*", "1"],
        ["*", "4", "1", "6", "3", "*", "*", "7", "5"],
        ["8", "*", "*", "*", "*", "*", "*", "3", "*"]]

        self.board_solution = [["4", "2", "7", "8", "5", "6", "1", "9", "3"],
        ["3", "6", "9", "2", "7", "1", "4", "5", "8"],
        ["1", "8", "5", "4", "9", "3", "2", "6", "7"],
        ["6", "1", "4", "5", "2", "7", "3", "8", "9"],
        ["7", "9", "3", "1", "6", "8", "5", "4", "2"],
        ["2", "5", "8", "3", "4", "9", "7", "1", "6"],
        ["5", "3", "6", "7", "8", "4", "9", "2", "1"],
        ["9", "4", "1", "6", "3", "2", "8", "7", "5"],
        ["8", "7", "2", "9", "1", "5", "6", "3", "4"]]    

class Board_Hard(Board):
    """Creating a second subclass of board for a different level of the board game"""
    def __init__(self):
        self.board = [["6", "*", "9", "3", "7", "5", "*", "*", "*"],
        ["*", "*", "*", "1", "*", "*", "*", "*", "*"],
        ["1", "*", "*", "*", "*", "9", "*", "5", "*"],
        ["*", "9", "*", "*", "*", "*", "2", "*", "1"],
        ["*", "*", "8", "*", "*", "*", "6", "*", "*"],
        ["2", "*", "7", "*", "*", "*", "*", "9", "*"],
        ["*", "4", "*", "9", "*", "*", "*", "*", "7"],
        ["*", "*", "*", "*", "*", "4", "*", "*", "*"],
        ["*", "*", "*", "5", "1", "7", "3", "*", "6"]]

        self.board_solution = [["6", "2", "9", "3", "7", "5", "4", "1", "8"],
        ["8", "7", "5", "1", "4", "2", "9", "6", "3"],
        ["1", "3", "4", "6", "8", "9", "7", "5", "2"],
        ["4", "9", "6", "7", "5", "8", "2", "3", "1"],
        ["3", "5", "8", "2", "9", "1", "6", "7", "4"],
        ["2", "1", "7", "4", "6", "3", "8", "9", "5"],
        ["5", "4", "3", "9", "2", "6", "1", "8", "7"],
        ["7", "6", "1", "8", "3", "4", "5", "2", "9"],
        ["9", "8", "2", "5", "1", "7", "3", "4", "6"]]

class Board_Diabolical(Board):
    """Creating a third subclass of board for a different level of the board game"""
    def __init__(self):
        self.board = [["*", "*", "7", "*", "*", "*", "6", "*", "*"],
        ["3", "6", "*", "*", "2", "7", "*", "*", "*"],
        ["*", "*", "2", "4", "*", "*", "*", "1", "*"],
        ["*", "*", "*", "*", "7", "*", "1", "*", "*"],
        ["*", "9", "*", "5", "*", "3", "*", "6", "*"],
        ["*", "*", "3", "*", "9", "*", "*", "*", "*"],
        ["*", "3", "*", "*", "*", "4", "2", "*", "*"],
        ["*", "*", "*", "6", "1", "*", "*", "3", "8"],
        ["*", "*", "9", "*", "*", "*", "4", "*", "*"]]

        self.board_solution = [["1", "5", "7", "3", "8", "9", "6", "2", "4"],
        ["3", "6", "4", "1", "2", "7", "5", "8", "9"],
        ["9", "8", "2", "4", "6", "5", "3", "1", "7"],
        ["5", "4", "8", "2", "7", "6", "1", "8", "3"],
        ["7", "9", "1", "5", "4", "3", "8", "6", "2"],
        ["6", "2", "3", "8", "9", "1", "7", "4", "5"],
        ["8", "3", "6", "9", "5", "4", "2", "7", "1"],
        ["4", "7", "5", "6", "1", "2", "9", "3", "8"],
        ["2", "1", "9", "7", "3", "8", "4", "5", "6"]]

class Check:
    """This is a class that checks the user's filled out board to the board solution"""
    def BoardsAreEqual(self, board, board_solution):
        """Returns true if board and board_solution are identical false otherwise"""
        for row_i in range(0, 9):
            for col_i in range(0, 9):
                if board[row_i][col_i] != board_solution[row_i][col_i]:
                    return False
        return True

#start of input

print('                                     ')
print('========Welcome to Sodoku!==========================')
print('There are 4 rules to this game: ')
print('1. This is a 9x9 grid box. Valid numbers are 1 to 9')
print('2. Each row has all numbers from 1 to 9')
print('3. Each column has all numbers from 1 to 9')
print('4. Each 3x3 grid box has all numbers from 1 to 9')
print("====================================================")
print('                                     ')
level = int(input('Choose level:        1. easy     2.medium        3.hard      4.extreme: '))
print('                                     ')
clear()

#call Board here, print board according to the user's level input
#create instances of the various boards to display the appropriate board. The method DisplayBoard is inherited from Board class to other Board level classes, such as hard, medium, and diabolical

print_board_easy = Board()
print_board_med = Board_Med()
print_board_hard = Board_Hard()
print_board_diabolical = Board_Diabolical()

if level == 1:
    print_board_easy.DisplayBoard()
elif level == 2:
    print_board_med.DisplayBoard()
elif level == 3:
    print_board_hard.DisplayBoard()
elif level == 4:
    print_board_diabolical.DisplayBoard()

#create instances of the various boards to check to use the method attributes of class Board
check_board = Board()
check_board_med = Board_Med()
check_board_hard = Board_Hard()
check_board_diabolical = Board_Diabolical()

#Reiterate the questions till the board is filled. This is a giant if else statement that takes in the user's input for the level they desire to play in.

if level == 1:
    while check_board.Board_not_Full() == True:
        try:
            row = int(input("Enter a row:"))
        except ValueError:
            print("Row must be a number from 0 to 8, starting from the top.")

        try:
            item = int(input("Enter a column:"))
        except ValueError:
            print("Column must be a number from 0 to 8, starting from the left.")
        try:
            guess = int(input("Enter a guess:"))
            if guess in range(1,10):
                try: 
                    check_board.SetBoard(row, item, guess)
                except IndexError as other:
                    print("Row, column and guess must be a number from 0 to 8, starting from the top.", other)
                check_board.DisplayBoard()
            else:
                print("Guess is your answer. It must be a number from 1 to 9. Please correct.")
        except:
            print("Guess is your answer. It must be a number also but from 1 to 9")
    
        try:
            give_up = input("Enter q to give up :) It's OK! Unless you want keep playing, enter any key!")
            if give_up == 'q':
                from suduko_menu import suduko_main
                suduko_main()
            else:
                continue
        except:
            print('Must enter a character to continue.')
            if give_up == 'q':
                break
            clear()
elif level == 2:
    while check_board_med.Board_not_Full() == True:
        try:
            row = int(input("Enter a row:"))
        except ValueError:
            print("Row must be a number from 0 to 8, starting from the top.")

        try:
            item = int(input("Enter a column:"))
        except ValueError:
            print("Column must be a number from 0 to 8, starting from the left.")
        try:
            guess = int(input("Enter a guess:"))
            if guess in range(1,10):
                try: 
                    check_board_med.SetBoard(row, item, guess)
                except IndexError as other:
                    print("Row, column and guess must be a number from 0 to 8, starting from the top.", other)
                check_board_med.DisplayBoard()
            else:
                print("Guess is your answer. It must be a number from 1 to 9. Please correct.")
        except:
            print("Guess is your answer. It must be a number also but from 1 to 9")

        try:
            give_up = input("Enter q to give up :) It's OK! Unless you want keep playing, enter anything else!")
            if give_up == 'q':
                suduko_main()
            else:
                continue
        except:
            print('Must enter a character to continue.')
            if give_up == 'q':
                break
elif level == 3:
    while check_board_hard.Board_not_Full() == True:
        try:
            row = int(input("Enter a row:"))
        except ValueError:
            print("Row must be a number from 0 to 8, starting from the top.")

        try:
            item = int(input("Enter a column:"))
        except ValueError:
            print("Column must be a number from 0 to 8, starting from the left.")
        try:
            guess = int(input("Enter a guess:"))
            if guess in range(1,10):
                try: 
                    check_board_hard.SetBoard(row, item, guess)
                except IndexError as other:
                    print("Row, column and guess must be a number from 0 to 8, starting from the top.", other)
                check_board_hard.DisplayBoard()
            else:
                print("Guess is your answer. It must be a number from 1 to 9. Please correct.")
        except:
            print("Guess is your answer. It must be a number also but from 1 to 9")

        try:
            give_up = input("Enter q to give up :) It's OK! Unless you want keep playing, enter anything else!")
            if give_up == 'q':
                suduko_main()
            else:
                continue
        except:
            print('Must enter a character to continue.')
            if give_up == 'q':
                break
elif level == 4:
    while check_board_diabolical.Board_not_Full() == True:
        try:
            row = int(input("Enter a row:"))
        except ValueError:
            print("Row must be a number from 0 to 8, starting from the top.")

        try:
            item = int(input("Enter a column:"))
        except ValueError:
            print("Column must be a number from 0 to 8, starting from the left.")
        try:
            guess = int(input("Enter a guess:"))
            if guess in range(1,10):
                try: 
                    check_board_diabolical.SetBoard(row, item, guess)
                except IndexError as other:
                    print("Row, column and guess must be a number from 0 to 8, starting from the top.", other)
                check_board_diabolical.DisplayBoard()
            else:
                print("Guess is your answer. It must be a number from 1 to 9. Please correct.")
        except:
            print("Guess is your answer. It must be a number also but from 1 to 9")

        try:
            give_up = input("Enter q to give up :) It's OK! Unless you want keep playing, enter anything else!")
            if give_up == 'q':
                suduko_main
            else:
                continue
        except:
            print('Must enter a character to continue.')
            if give_up == 'q':
                break
#Now if the board is filled out, we have to check it against the solution and give back our response: 

Final_board = Check()
while check_board.Board_not_Full() == False:
    if Final_board.BoardsAreEqual(check_board.board, check_board.board_solution) == True:
        print('Beautiful! You are a master at easy Sodoku! You can try a harder Sodoku now!')
    else: 
        print('So sad! Your board is not correct. Could you have violated any rules of the game? Thank you for playing. Feel free to try again!')
    break
while check_board_med.Board_not_Full() == False:
    if Final_board.BoardsAreEqual(check_board_med.board, check_board_med.board_solution) == True:
        print('Beautiful! You are a master at medium Sodoku! You can try a harder Sodoku now!')
    else: 
        print('So sad! Your board is not correct. Could you have violated any rules of the game? Thank you for playing. Feel free to try again!')
    break
while check_board_hard.Board_not_Full() == False: 
    if Final_board.BoardsAreEqual(check_board_hard.board, check_board_hard.board_solution) == True:
        print('Beautiful! You are a master at hard Sodoku! You can try a even harder Sodoku now!')
    else: 
        print('So sad! Your board is not correct. Could you have violated any rules of the game? Thank you for playing. Feel free to try again!')
    break
while check_board_diabolical.Board_not_Full() == False:
    if Final_board.BoardsAreEqual(check_board_diabolical.board, check_board_diabolical.board_solution) == True:
        print('Beautiful! You are a master at the hardest level of Sodoku! You are a God!')
    else:
        print('So sad! Your board is not correct. Could you have violated any rules of the game? Thank you for playing. Feel free to try again!')
    break
