

def homepage():
        
    print("********** Main Menu **********")
    print("1.Snake")
    print("2.queue")
    print("3.stacked")
    print("Exit")
    while 1:

        ch = int(input("Enter your choice: "))
        if ch == 1:
          import sample
          sample
        elif ch == 2:
            import stacked
            stacked
        elif ch == 3:
            import queue
            queue
        elif ch == 4:
            break
        else:
            print("Wrong Choice!")
            
            return homepage

print(homepage())