# Task 1
# A simple function.
# Create a simple function called favorite_movie, which takes a string containing the name of your favorite movie.
# The function should then print “My favorite movie is named {name}”.

def favorite_movie(name):
    print("My favorite movie is named " + name)
favorite_movie("Shakal")

# Task 2
# Creating a dictionary.
# Create a function called make_country, which takes in a country’s name and capital as parameters.
# Then create a dictionary from those two, with ‘name’ as a key and ‘capital’ as a parameter.
# Make the function print out the values of the dictionary to make sure that it works as intended.

def make_country(country_name, capital):
    return dict([(country_name, capital)])
#    return dict(country_name=capital)

print(make_country("Ukraine", "Kyiv"))

# option2
def make_country2(**kwargs):
    return (kwargs)
print(make_country2(Ukraine = "Kyiv", Poland="Warsaw", Germany="Berlin", Netherland="Amsterdam"))

# Task 3
# A simple calculator.
# Create a function called make_operation, which takes in a simple arithmetic operator as a first parameter
# (to keep things simple let it only be ‘+’, ‘-’ or ‘*’) and an arbitrary number of arguments (only numbers) as the second parameter.
# Then return the sum or product of all the numbers in the arbitrary parameter. For example:
# the call make_operation(‘+’, 7, 7, 2) should return 16
# the call make_operation(‘-’, 5, 5, -10, -20) should return 30
# the call make_operation(‘*’, 7, 6) should return 42

import numpy
def make_operation(oper, *args):
    # if oper == '*':   Just leave it here for the history. My attempts to understand how to work with result =0 in case of *
    #     result = 1
    # else:
    #     result = 0
    result = args[0]
    for i in range(1, len(args)):
 #       print(result)
        if oper == '+':
            result += args[i]
        elif oper == '-':
            result -= args[i]
        else:
            result *= args[i]
#            result = numpy.prod(args) # I know it's kinda of cheating but its an easy way to avoid an issue with result = 0 in multiplication
    return print(result)

make_operation('-', 5, 5, -10, -20)
make_operation('+', 7, 7, 2)
make_operation('*', 7, 6)


# Additional TASKS
# Write a function that takes on an input random ints (between 1 and 10) and returns the longest consecutive run
# and the length of that run of elements of the list.
# Ex. 	def task1(1,2,3,4,4,4,4,4,4,5,6,7,4,2,2,5) -> 6, 4
# 	def task1(1) -> 1, 1
# 	def task1() -> 0, None
# Then create another function which takes on input result of function from the previous step and prints
# Informative message about the longest consecutive run, something like - “Longest run is 6 of integers - 4”

def check_cons(*args):
    count = 0
    m_length = 0
    m_run = 0
    for i in range(1, len(args)):
        if args[i] == args[i-1]:
            count += 1
        else:
            count = 1
        if m_length < count:
            m_length = count
            m_run = args[i]
    return m_length, m_run

def check_cons2(func):
    m_length, m_run = func
    print (m_length, m_run, "\n""Longest run is " + str(m_length) + " of integers - " + str(m_run))
check_cons2(check_cons(1,2,3,4,9,8,6,7,7,7,7,7,7,7,7,7,1,2,3,2,2,2,2,2,2,5))

