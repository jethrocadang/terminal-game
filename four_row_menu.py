
import time
import os

def clear():
    os.system('clear||cls')

def four_row_main():
    clear()
    print("------------------------------")
    print('------------------------------')
    print('|        4 in a Row          |')
    print("------------------------------")
    print('|     [1] Play               |')
    print('|     [2] Highest Score      |')
    print('|     [3] Game Menu          |')
    print('------------------------------')
    print('------------------------------')
    
    four_row_input = input('Enter: ')

    while True:
        if four_row_input == '1':
            import four_row
            four_row
        if four_row_input == '2':
            print('Highest score')
        if four_row_input == '3':
            from game_menu import homepage
            homepage()
        else:
            
            print('Input not valid !!!')
            print('...')
            time.sleep(2)

            return four_row_main

four_row_main()
    