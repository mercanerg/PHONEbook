import time
import os
import sys

phone_dict = {0: {'name': 'Martin DAAN', 'phone': '6874057600'},
              1: {'name': 'Roger NOAH', 'phone': '5780465576'},
              2: {'name': 'Gerard MILAN', 'phone': '5673889347'},
              3: {'name': 'Rutter MEES', 'phone': '7350984476'},
              4: {'name': 'Marieke LEUK', 'phone': '3940235060'}
              }

# At the begining menu function
def menu():
        os.system('cls')
        state = True
    # list of menu selections
        sel_list = ['1', '2', '3', '4', '5',None]
        print()
        print(60 * '*')
        print('%40s'  % 'RCN Soft  February 2022')
        print( '%48s'  %  'Developed by Mehmet Ercan EREGLIOGLU')
        print(60 * '*')
        print(10 * '- ' + '  Main Menu  ' + 10 * ' -' )
        print("  1 - New contact")
        print("  2 - Edit name or phone")
        print("  3 - Delete contact")
        print("  4 - List contacts")
        print("  5 - Exit")
        print()
        while state:
            sel_chr =input("  choose an options as - 1, 2, 3, 4, 5 -  ==>  ")
    # check input if it is valid in sel_list
            if sel_chr in sel_list:
                state = False
                return sel_chr
            else:
                print('Invalid character try again')

# convert name format to "Title Title CAPITAL"  as "Maria Lara GODGEEFT"
def nameformat(nam):
    naam = ''
    name_list = nam.split()
    length_name = len(name_list)
    for i in range(length_name):
        if i == length_name-1:
            naam += name_list[i].upper()
        else:
            naam += name_list[i].title() + ' '

    return naam

def namecontrol():
    control = True
        # split name by word to check if it is valid
    while control:
        name = input("  Enter name ==> ")
        name = nameformat(name)
        list_name = name.split()
        length = len(list_name)

        control = False
        for k in list_name:
            if not k.isalpha():
                control = True
        if control:
           print('  Invalid name try again')

    return name

def phonecontrol():
    state = False
    while not state:
        phone = input("  Enter the phone number ==> ")
        length = len(phone)
        # check phone number if it numeric and the length to length
        if phone.isnumeric() and length == 10:
            state = True
        else:
            print('Invalid phone number try again')
            state = False
    return phone
# append and edit contact
def updatebook(idno):
    name = namecontrol()
    phone = phonecontrol()
    # append the new data to phone_dict if the name and the phone number is valid
    # and then return to main menu
    phone_dict.update({idno:{'name':name, 'phone':phone}})
    listbook()

def search():
    print(' 1 - search by name')
    print(' 2 - search by phone number')
    choose = None
    state = True
    while state:
          choose = input('choose your option to search record - 1 or 2 - ')
# check input if it is valid in sel_list
          if choose in ['1', '2']:
              state = False
          else:
              print('Invalid character try again')
    if choose == '1':
        idnumber= searchbyname()
    elif choose == '2':
        idnumber = searchbyphone()
    return idnumber

def searchbyphone():
    state = False
    counter = 0
    length = 0
    #loop until valid name is typed by user
    # the name must be only numbers in 10 digits
    while not state:
        searchphone = input('enter phone number to edit (10 digits) ==> ')
        length = len(searchphone)
        # check the value entered by the user is a 10-digit numeric value
        if length == 10 and searchphone.isnumeric():
            state = True
        else:
            print('invalid phone number try again')
            state = False
    state = False
    #if the value entered by user is valid, search the value in dictionary
    while not state:
        phone = phone_dict[counter]['phone']
        if searchphone == phone:
            name = phone_dict[counter]['name']
            print(f"ID No  : {counter}    name : {name}   phone :  {phone}")
            state = True
            return counter
        if counter == len(phone):
                input('could not find the number you search in the PHONEbook - to continue press ENTER')
                return None
        counter += 1

def deletebook(id_no):
      del phone_dict[id_no]
      for i in range(id_no, len(phone_dict)):
          phone_dict[i] = phone_dict.pop(i + 1)

def searchbyname():
    #assign the string which namecontrol() returns to the variable of searchname
    searchname = namecontrol()
    state = False
    counter = 0
    while not state:

        if counter == len(phone_dict):
            input("could not find the name you search in the PHONEbook - to continue press ENTER")
            return None
        else:
        # assign the value of "name" from phone_dict (dictionary)
            name = phone_dict[counter]['name']
        # If the name in the dictionary is the same as the name sought
            if searchname == name:
                phone = phone_dict[counter]['phone']
                print(f"ID No  : {counter}    name : {name}   phone :  {phone}")
                state = True
                return counter
        counter += 1

def menuexec():
# get sel_ch returned value from menu() function
# run functions by choosing one of options
    sel_ch = menu()
    if sel_ch == '1':
        os.system('cls')
        print()
        print(10 * '* ' + '  New Records  ' + 10 * ' *')
        idno = len(phone_dict)
        updatebook(idno)
        os.system('cls')
        listbook()
    elif sel_ch == '2':
        idno = search()
        if idno != None:
            updatebook(idno)
        os.system('cls')
        listbook()
    elif sel_ch == '3':
        idno = search()
        os.system('cls')
        if idno != None:
            deletebook(idno)
        os.system('cls')
        listbook()
    elif sel_ch == '4':
        os.system('cls')
        listbook()
    elif sel_ch == '5':
        print('Exit')
        exit()
# list the all records the phone book on the screen
def listbook():
    print()
    print()
# title of list
    print("%10s" % "NAME" + "%38s" % "PHONE")
    print(20 * "-" + 15 * ' ' + 20 * "-")
    counter = 0

# get data from phone_dict and print screen
    for k in range(len(phone_dict)):
        name = phone_dict[k]['name']
        phone = phone_dict[k]['phone']
        print(f"{k} - {name:22}\t\t{phone}\t\t")
        counter += 1

# delay screen to see in each 20 records
        if counter == 20:
            input("Press ENTER to continue")
            counter = 0

# delay screen to see end of the list.
    input("Press ENTER to continue")
# return to main menu
    os.system('cls')
    menuexec()
def introduce(text):
     os.system('cls')
     for c in text:
         sys.stdout.write(c)
         sys.stdout.flush()
         time.sleep(0.1)

     os.system('COLOR 09')
     print("\033[1m" + " ")

text = ' \n PHONEbook - - - RCN Soft - - - Mehmet Ercan EREGLIOGLU - - - February 2022 - - - Netherland '
introduce(text)
menuexec() # run menuexec() function



