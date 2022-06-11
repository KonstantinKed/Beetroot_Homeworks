# Task 1
# Write a Python program to detect the number of local variables declared in a function.

def count_param(*args, ** kwargs):
    print(len(args), len(kwargs))

count_param(1, 2, 3, "amore", a = 3, b = 4, length = [1,2,3,4,5], keyword='strange')

# USING .co_nlocals
def count_par():
    a = 1
    b = 'text'
    c = {'name': 'Kostya', 'age': '12' }
count_par()
print(count_par.__code__.co_nlocals)

# Task 2
# Write a Python program to access a function inside a function (Tips: use function, which returns another function)

def inner(a, b):
    return a + b

def outer(func):
    print('Concatination of "a" and "d" is: ')
    print(func(4, 5))

outer(inner)

# Task 3
# Write a function called `choose_func` which takes a list of nums and 2 callback functions.
# If all nums inside the list are positive, execute the first function on that list and return the result of it.
# Otherwise, return the result of the second one

nums1 = [1, 2, 3, 4, 5]

nums2 = [1, -2, 3, -4, 5]

def square_nums(nums):
    return [num ** 2 for num in nums]


def remove_negatives(nums):
    return [num for num in nums if num > 0]


def choose_func(nums: list, func1, func2):
    lists = [i for i in nums if i > 0]
    if len(lists) == len(nums):
        print(square_nums(lists))
    else:
        print(remove_negatives(nums))

choose_func(nums1, square_nums, remove_negatives)
choose_func(nums2, square_nums, remove_negatives)



