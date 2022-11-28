import os

def homepage():
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

        ch = int(input("Enter your choice: "))
        if ch == 1:
          cls()
          import queue
          queue
        elif ch == 2:
            cls()
            import stacked
            stacked
        elif ch == 3:
            cls()
            import queue
            queue
        elif ch == 4:
            cls()
            import authentication
            authentication
        else:
            print("Wrong Choice!")
            
            return homepage

def cls():
        os.system('clear')

    

homepage()