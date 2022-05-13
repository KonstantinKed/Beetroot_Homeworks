# Task 1
# String manipulation
# Write a Python program to get a string made of the first 2 and the last 2 chars from a given string.
# If the string length is less than 2, return instead of the empty string.

line = str(input("PLease enter your phrase: "))
if len(line) >= 2:
    print(line[0:2] + line[-2:])
else:
    print("")

# Task 2
# The valid phone number program.
# Make a program that checks if a string is in the right format for a phone number.
# The program should check that the string contains only numerical characters and is only 10 characters long.
# Print a suitable message depending on the outcome of the string evaluation.

phone_numb = (input("Please enter ten digits of your phone number: "))

if len(phone_numb) > 10 and phone_numb.isdigit():
    print("Numer has NOT been added. You enter more than 10 digits")
elif len(phone_numb) < 10 and phone_numb.isdigit():
    print("Numer has NOT been added. You missed to enter some digits")
elif len(phone_numb) == 10 and not phone_numb.isdigit():
    print("Numer has NOT been added. Please enter ONLY digits")
else:
    print("Your phone number has been added successfully")

# Task 3
# The name check.
# Write a program that has a variable with your name stored (in lowercase) and then asks for your name as input.
# The program should check if your input is equal to the stored name even if the given name has another case, e.g.,
# if your input is “Anton” and the stored name is “anton”, it should return True.

real_name = "konstantin"
enter_name = str(input("Please enter your name for checking: "))
check_name = enter_name.lower()
print (check_name == real_name)

# Additional tasks
# Check if the number is a simple number:
threshold = int(input("Enter the max threshold of checking: "))
for a in range (1, threshold):
    i = 2
    if a == 1:
        print(f"{a} is NOT a start-simple number")
    else:
        while i < a:
          if a % i == 0:
            print (f"{a} is NOT a simple number")
            break
          else:
            i += 1
        else:
            print(f"{a} is a simple number")

# Write a Python program to check whether a letter is a vowel or consonant.

word = str(input("Enter the word to check: "))
vowel_dict = ['e','y','u','i','o','a']
i = 0
y = 0
vowel_count = 0
consonant_count = 0
if word.strip().isalpha():
    while i < len(word):
        if word[i] in vowel_dict:
            vowel_count +=1
        else:
            consonant_count +=1
        i +=1
    print(f"In your word {vowel_count} vowels letters and {consonant_count} consonant letters")
else:
    print("Please DO NOT enter digits, spaces or symbols")

# Write a Python program that prints all the numbers from 0 to 6 except 3 and 6. Note : Use 'continue' statement.
our_threshold = 8
i = 0
print (i, end=' ')
while i < our_threshold:
    if i % 3 == 0 or i % 6 == 0:
        i += 1
        continue
    print(i, end=' ')
    i += 1

# Write a python program to find the sum of all even numbers from 0 to 10
our_threshold = 10
i = 0
sum = 0
while i <= our_threshold:
    if i % 2 == 0:
        sum += i
    i += 1
print("Total of even numbers from 0 to 10 is:", sum)

# Finding the average of 5 numbers using while loop
list_of_digits = [0, 5, 6, 4, 5]
i = 0
sum = 0
while i < len(list_of_digits):
    sum += list_of_digits[i]
    i += 1
print('Average of 5 digits in the list is:', sum/i)

# Finding the factorial of number (with while loop)
number = int(input("Enter number to calculate factorial: "))
i = 1
fac = 1
if number == 0:
    print(f'{number}! = {fac}')
else:
    while i <= number:
        fac *= i
        i += 1
    print(f'{number}! = {fac}')

# Write a python program to print the square of all numbers from 10 to 20
i = 10
while i <= 20:
    print(f'{i}*{i} =', i**2)
    i += 1
