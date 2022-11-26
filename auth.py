import os
import csv
import pwinput
import time

is_exit = False
main_menu_input = ''

def main():
    clear()
    print('[1] Register')
    print('[2] Login')
    print('[3] Logout')
    print('[4] Reset Password')
    global main_menu_input
    main_menu_input = input('Choice: ')
    is_exit = False

    while is_exit == False:
        if main_menu_input == '1':
            clear()
            register()
            main()
        if main_menu_input == '2':
            clear()
            login()
        if main_menu_input == '3':
            clear()
            logout()
            main()
        if main_menu_input == '4':
            clear()
            reset_password()
            main()
        
        return True

def register():
    print('Registration Form')
    username = input('Enter your username: ')
    password = pwinput.pwinput(prompt='Enter your password: ', mask='*')
    with open('database.csv', 'a') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow([username, password])
    return True

def login():
    print('Login Form')
    username = input('Username: ')
    password = pwinput.pwinput(prompt='Password: ', mask='*')
    with open('database.csv') as csv_file:
        reader = csv.reader(csv_file)
        is_success = False
        for row in reader:
            if len(row) > 1:
                if row[0] == username and row[1] == password:
                    is_success = True
        
        if is_success:
            print('Login Success')
        else:
            print('Login Failed')
        global is_exit
        global main_menu_input
        is_exit = True
        main_menu_input = ''
        # time.sleep(10)

def logout():
    return True

def reset_password():
    print('Reset Password Form')
    print('Login First')
    username = input('Username: ')
    password = pwinput.pwinput(prompt='Password: ', mask='*')
    with open('database.csv') as csv_file:
        reader = csv.reader(csv_file)
        is_success = False
        counter = 0
        index = None
        new_list = []
        for row in reader:
            new_list.append(row)
            if len(row) > 1:
                if row[0] == username and row[1] == password:
                    is_success = True
                    index = counter
            counter += 1
        
        if is_success:
            new_password = input('Input New Password: ')
            for i in range(len(new_list)):
                if i == index:
                    new_list[i][1] = new_password
            with open('database.csv', 'w+') as csv_file:
                writer = csv.writer(csv_file)
                for i in range(len(new_list)):
                    writer.writerow(new_list[i])
            time.sleep(20)
        else:
            print('Login Failed')
        global is_exit
        global main_menu_input
        is_exit = True
        main_menu_input = ''
        # time.sleep(10)

def clear():
    os.system('clear||cls')

main()

