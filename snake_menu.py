import time
import os

def clear():
    os.system('clear||cls')

def snake_main():
    clear()
    print("------------------------------")
    print('------------------------------')
    print('|          Snake             |')
    print("------------------------------")
    print('|     [1] Play               |')
    print('|     [2] Highest Score      |')
    print('|     [3] Game Menu          |')
    print('------------------------------')
    print('------------------------------')
    
    snake_input = input('Enter: ')

    while True:
        if snake_input == '1':
            import snake
            snake
        if snake_input == '2':
            print('Highest score')
        if snake_input == '3':
            from game_menu import homepage
            homepage()
            
        else:
            
            print('Input not valid !!!')
            print('...')
            time.sleep(2)

            return snake_main

