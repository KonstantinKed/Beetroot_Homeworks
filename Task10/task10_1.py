# Task 1
# Write a function called oops that explicitly raises an IndexError exception when called. Then write another
# function that calls oops inside a try/except state­ment to catch the error. What happens if you change oops to
# raise KeyError instead of IndexError?

import json

with open('dict_name_age.json', 'r+') as f:
    a = json.load(f)

#The first function oops to call INDEX ERROR
# def oops():
#     print(a[4]['name'])
# oops()

# The second function to call and fix INDEX ERROR
def oops():
    try:
        print(a[2]['name', 'age'])  # if you a) change [2]-->[4] - Index Error will be catch by except and special text will be printed.
    except IndexError:              # If you add extra key ['age'] - Key Error will occur and will not be cought by exception
        print('OOPS. Use other index to search dictionary')

oops()



