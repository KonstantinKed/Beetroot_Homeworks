import json

with open('phonebook.json') as f:
    ph_bk = json.load(f)

def show_phonebook():  # Print current phonebook
    for lists in ph_bk.values():
        print('-' * 40, 'PHONEBOOK', '-' * 40)
        for dic in lists:
            for k, v in dic.items():
                print (k, ":", v, '|', end=' ')
            print('\n','-' * 90)
               # when u type "return" it shows only 1 element

show_phonebook()


def save_phonebook():
    with open('phonebook.json', 'w') as f:
        json.dump(ph_bk, f)
save_phonebook()

# def print_record():  # Print even if not called ?
#     for lists in ph_bk.values():
#         for dics in lists:
#             for k, v in dics.items():
#                 print (k, ":", v, '|', end=' ')
#             print('\n','-' * 90)
#
# print_record()
