import time
import os

def clear():
    os.system('clear||cls')

def suduko_main():
    clear()
    print("------------------------------")
    print('------------------------------')
    print('|          Suduko            |')
    print("------------------------------")
    print('|     [1] Play               |')
    print('|     [2] Highest Score      |')
    print('|     [3] Game Menu          |')
    print('------------------------------')
    print('------------------------------')
    
    suduko_input = input('Enter: ')

    while True:
        if suduko_input == '1':
            import suduko
            suduko
        if suduko_input == '2':
            print('Highest score')
        if suduko_input == '3':
            from game_menu import homepage
            homepage()
            
        else:
            
            print('Input not valid !!!')
            print('...')
            time.sleep(2)

            return suduko_main

suduko_main()
