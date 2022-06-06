# Task 2
# Write a function that takes in two numbers from the user via input(), call the numbers a and b, and then returns the value of squared a divided by b,
# construct a try-except block which raises an exception if the two values given by the input function were not numbers, and if value b was zero (cannot divide by zero).


var = input("Please enter two digits 'a' and 'b' with the space: ").strip().split(' ')

def sq_div(a,b):
    try:
      return (int(a)**2)/int(b)
    except ValueError:
        print("Enter digits  only, not text")
    except ZeroDivisionError:
        print('can not divide by zero!!!')
print(sq_div(var[0], var[1]))
