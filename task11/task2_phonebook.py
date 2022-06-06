# PHONEBOOK

import json
from print_phonebook import show_phonebook as pr_pb
from print_phonebook import save_phonebook as save_pb
from print_phonebook import save_phonebook as print_record

# TEST FIRST NOTE IN THE PHONEBOOK
b = {}
b['first_name'] = ""
b['last_name'] = ""
b['phone_number'] = ""
b['city'] = ""

while True:
    try:
        action = int(input('----------MENU----------\n 1 - Add new person info\n 2 - Update person info\n 3 - Search\n 4 - Delete a record\n 5 - Show phonebook records\n 6 - EXIT\nMake a choice:').strip())
        with open('phonebook.json') as f:
            ph_bk = json.load(f)
    except ValueError:
        print("Please enter digits from 1---6!!!")

    if action == 1:
        print("Add a new record")
        info = input('Please enter First name, Last name, phone number and city:\n').strip().split(' ')
        try:
            b['first_name'] = info[0]
            b['last_name'] = info[1]
            b['phone_number'] = info[2]
            b['city'] = info[3]
            for dics in ph_bk.values():
                dics.append(b)
            with open('phonebook.json', 'w') as f:
                json.dump(ph_bk, f)  # save_pb - function to save changes in phonebook doesn't work ???
  #     pr_pb()    # function to print current phonebook
        except:
            print("Record is NOT saved! Please enter ONLY First name, Last name, phone number and city")
    elif action == 2:
        print('Update person info.\n Please select person\'s phone number from the phonebook:')
        pr_pb()  # print a Phonebook to select number
        try:
            info = input('COPY/Enter person\'s phone number from the list above and update First name, Last name and city:').strip().split(' ')
            for lists in ph_bk.values():
                for dics in lists:
                      if dics['phone_number'] == info[0]:
#                lists = [dics.update({'first_name': info[1], 'last_name': info[2], 'city': info[3]} for dics in lists if dics['phone_number'] == info[0])]
                        dics.update({'first_name': info[1], 'last_name': info[2], 'phone_number': info[0], 'city': info[3]})
            print("\n Your updates has been saved successfully")  # UPDATES CAN BE SEEN ONLY AFTER PROGRAM RESTARTED
#2            save_pb()   # doesn't work
            with open('phonebook.json', 'w') as f:
                json.dump(ph_bk, f)
        except IndexError:
            print('You missed to enter phone number or update info')
            continue # doesn't want to bring action to line 34!!!


    elif action == 3:
        print("Search by first, last or full name, by phone_number or by city")  # There was a task to do 4 separate search. But I improved it to one search
        info = input('Enter the first name, last name, phone_number or city to search details: \n').strip().split(' ')
        for lists in ph_bk.values():
            check = 0
            for dics in lists:
                if dics['first_name'] == info[0] or dics['last_name'] == info[0] or dics['phone_number'] == info[0] or dics['city'] == info[0]:
                    check += 1
                    print('----->', check, end='')
                    for k, v in dics.items():
                        print(":", k, ":", v, '|', end = '')
                    print('\n', '-' * 90)
            if check == 0:
                print("We couldn't find a record to given request data. Check info and try again")
#           print(next(item for item in lists if item['first_name'] == info or item['last_name'] == info or item['phone_number'] == info))   # comprehension method  How to enter all data with the same value?


    elif action == 4:
        print("Delete a record")
        info = input('Enter telephone number to delete appropriate record:').strip()
        for lists in ph_bk.values():
                try:
                    del_var = next(dics for dics in lists if dics['phone_number'] == info)
                    print('The following record:',del_var,'will be deleted.')
                    del_action = input('Press (Y)es/(N)o:').strip().upper()
                    if del_action == 'Y':
                        lists[:] = [dics for dics in lists if dics.get('phone_number') != info]  # deleting action---
                        print('The record was deleted successfully')
                    else:
                        print('U skip deleting')
                    break
                except:
                    exc_answ = input('The record with provided phone number was not found in the phonebook. Press 1 - to try again, or any other button to go to MENU')
                    if exc_answ == '1':
                        continue
                    else:
                        break

        with open('phonebook.json', 'w') as f:
            json.dump(ph_bk, f)

    elif action == 5:
        pr_pb()
    elif action == 6:
        with open('phonebook.json', 'w') as f:
            json.dump(ph_bk, f)
        print('You successfully exit the phonebook. All data has been saved!')
        break


# while True:
#     try:
#         exit_ph_bk = input('Press any button to access MENU or E for EXIT C/E?\n').strip().upper()
#     except TypeError:
#         print("Please any button to access MENU or E for EXIT!!!")
#     if exit_ph_bk == 'E':
#         with open('phonebook.json', 'r+') as f:
#             json.dump(ph_bk, f)
#         print('You successfully exit the phonebook. All data has been saved!')
#         break
#     else:
#         pass
