import os
import time

def homepage():
    clear()
    print("-----------------------")
    print("|      Game Menu      |")
    print("-----------------------")
    print("-----------------------")
    print("|   [1] Snake         |")
    print("|   [2] 4 in a Row    |")
    print("|   [3] Suduko        |")
    print("-----------------------")
    print("-----------------------")
    print("|    [4] Main Menu    |")
    print("-----------------------")
    
    while 1:

        ch = input("Enter your choice: ")
        if ch == '1':
          clear()
          from snake_menu import snake_main
          snake_main()
        elif ch == '2':
            clear()
            import four_row
            four_row   
        elif ch == '3':
            clear()
            from suduko import thisgame
            thisgame()
        elif ch == '4':
            clear()
            import authentication
            authentication
        else:
            print("Wrong Choice!")
            time.sleep(3)
            clear()
            
            return homepage()

def clear():
        os.system('clear')

    

homepage()