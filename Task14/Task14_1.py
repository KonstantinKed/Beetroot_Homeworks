# Task 1
# Write a decorator that prints a function with arguments passed to it.
# NOTE! It should print the function, not the result of its execution!
#
def logger(func):
    def wrap(*args, **kwargs):
        print(func.__name__, "called with", args)
    return wrap


@logger
def add(a, b):
    return a + b

add(4, 5)

@logger
def square_all(*args):
    return [arg ** 2 for arg in args]

square_all(1,2,3,4,5)