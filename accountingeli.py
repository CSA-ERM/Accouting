import math
import time
def menu(): #for all selections
    print("""Choose below:""") #options
    c=input("""

    1. Login
    2. Administration
    3. Quit
    : """)
    if c=='1': #if the input is = 1, go to the function
        login_function()
    elif c=='2': #if the input is = 2, go to the function
        adminpass()
    elif c=="3": #if the input is = 3, go to the function
        time.sleep(4)
        quit()
    else:
        print("""
Invalid Entry""")
        menu()

def login_function():
    count=0
    while True:
        break_var = False
        values_list = []

        username = input("Username: ")
        password= input("Password: ")
        outfile = open("logins2.txt", "r")
        log = open("log2.txt","a")
        infile2 = open("logins2.txt", "a")

        read_file = outfile.read()
        values = read_file.split('\n\n')
        for x in values:
            values_new = x.split('\n')
            values_list.append(values_new)
        if count != 3:
            pass
        for x in values_list:
            if username.lower() == x[0].lower() and password.lower() == x[1].lower():
                print ("Congrats "+str(username)+ " you have logged in!")
                break_var = True
                quit()
        if break_var != True:
            count+=1
            print ("Incorrect login, try again!\n")
        if break_var == True:
            time.sleep(4)
        if count == 3:
            print ("YOU HAVE BEEN LOCKED OUT!")
            time.sleep(4)
            quit()
        outfile.close()
        infile2.close()
def adminpass():
    adminpassword="1111"
    adminpass=input("Input the admin password: ")
    if adminpass==(adminpassword):
        print("Valid Entry")
        newmenu()
    else:
        print("Incorrect password or username")
        menu()
def newmenu():
    print("""Choose below:""") #options
    c=input("""

    1. Create User
    2. Delete User
    3. Main Menu
    : """)
    if c=='1': #if the input is = 1, go to the function
        create_user()
    if c=='2': #if the input is = 2, go to the function
        delete_user()
    if c=="3": #if the input is = 3, go to the function
        time.sleep(4)
        menu()
    else:
        print("""
Invalid Entry""")
        newmenu()
def create_user():
    outfile = open("logins2.txt", "r")
    infile2 = open("logins2.txt", "a")
    newuser=(str(input("Input a new username: ")))
    newpassword=(str(input("Input a new password: ")))
    infile2.write('' +((str(newuser).lower())+ '\n' +(str(newpassword)))+ '\n')
    infile2.close()
    outfile.close()
def delete_user():
    global value_str
    while True:
        outfile = open("logins2.txt", "r")
        break_var = False  
        values_list = []
        read_file = outfile.read()
        values = read_file.split('\n\n')
        for x in values:
            x_split2 = x.split('\n')
            values_list.append(x_split2[0])
        for x in values_list:
            if x != '':
                print ("User: " +str(x)+ "")
        delete = input("Which user would you like to delete? [b to go back]")

        if delete.lower() == 'b' or delete.lower == 'back':
            outfile.close()
            break

        for x in values_list:
            if delete.lower() == x.lower():
                break_var = True
            values_list.remove(x)
            
        if break_var != True:
            print ("\nUSER ['" +str(delete)+ "'] DOES NOT EXIST!\n")
            time.sleep(1)
        if break_var == True:
            infile = open("logins2.txt","w")
            value_str = ''
            for x in values_list:
                value_str = ''.join(x)
                print (value_str)
                infile.write(str(value_str)+ '\n')
            infile.close()
            outfile.close()
            break
        
menu()
