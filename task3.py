# TASK 1. Make a program that has your name and the current day of the week stored
# as separate variables and then prints a message like this:
# “Good day <name>! <day> is a perfect day to learn some python.”
name = "Konstantin"
day = "10'th of May"
print(f'Good day {name}! {day} is a perfect day to learn some python.')
print('Good day {}! {} is a perfect day to learn some python.'.format(name, day))

# TASK 2. Save your first and last name as separate variables, then use string
# concatenation to add them together with a white space in between and print a greeting.
first_name = "Konstantin"
last_name = "Kozynskyi"
print(first_name + " " + last_name)

# TASK 3. Using python as a calculator.
# Make a program with 2 numbers saved in separate variables a and b, then print the result for each of the following:

a = 3
b = 14.8
print(b - a)
print(b + a)
print(b / a)
print(b * a)
print(b ** a)
print(b // a)
print('%.2f' % (b % a))


#EXERCISES FROM THE CLASSROOM:
# Define the variables below. Print the types of each variable. What is the sum of your variables?
# (Hint: use a type conversion function.) What datatype is the sum?
a = 4
b = 4.8
c = "4.2"
d = 1 +2j
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(a + float(b))
print(type(a + float(b)))


# Exercise: Find the last position of a given substring
# Write a program to find the last position of a substring "Emma" in a given string.
a = 'Emma is my daughter. Emma likes bananas'
print(a.rfind('Emma'))

# Exercise: Return the count of a given substring from a string
a = 'Emma is my daughter. Emma likes bananas'
result = a.count('Emma')
print(f'Emma counts {result} times')

# Exercise: Insert the correct syntax to add a placeholder for the age parameter
age = 36
print(f'I am a {age} years old')

# Exercise: Return the string without any whitespace at the beginning or the end
string = " some string as an example   "
print(string.strip())

# Write a Python program to convert temperatures to and from celsius, Fahrenheit. Formula : c/5 = f-32/9
# [ where c = temperature in celsius and f = temperature in Fahrenheit.
#     Expected Output (pay attention to output, students have to practice
#     in string formating for constructing result message): 60°C is 140 in Fahrenheit 45°F is 7 in Celsius

temp_far = float(input('Please input the temperature in Fahrenheit'))
c = round((temp_far-32)/9*5)
print (f'{temp_far} in Fahrenheit equals {c} Celcium')
temp_celc = float(input('Please input the temperature in Celcius'))
f = round((temp_celc*9/5)+32)
print(f'{temp_celc} in Celcius equals {f} in Fahrenheit')
# 2. Write a Python program to create a string that is made of an input string’s second and last characters.

text = input("please enter your phrase :")
print(text[1] + text[-1])
print(text[1:])
# 3. Create a string s1, calculate the sum and average of the digits that appear in this string,
# ignoring all other characters.

s1 = input("please enter the phrase:")
number_digits = 0
count_digits = 0
for i in s1:
   if i.isdigit():
       number_digits+=int(i)
       count_digits +=1
print("Total sum is : ",number_digits, "Avarage is: ",number_digits/count_digits)

# 4. Create a string. Replace special symbols in your string with #. Example: input = “&^hwjys*%#” output = “##hwjys###”

line = "&^hwjys*%/#"
for symb in line:
    if not symb.isalnum():
        line = line.replace(symb, "#")
print(line)

# 5. Create a program that displays your name and complete mailing address
# formatted in the manner that you would usually see it on the outside of an envelope

first_name = "Konstantin"
last_name = "Kozynskyi"
email = "knkostya@gmail.com"
print("\t\t\t\t\t\t\t\t\tName:\t{}\t{}\n\t\t\t\t\t\t\t\t\tEmail:\t{}".format(first_name, last_name, email))

# 6. Create two strings and check if all the characters in the string1 are present in string2 and print the result (True or False)
str1 = "a nanab"
str2 = "textisve rybigfindbananainme"
i = -1
while i < len(str1):
    if str1[i] in str2:
        i += 1
    else:
        a = False
        break
else:
    a = True
print(a)
# 7. Create a program that reads the length and width of a farmer’s field from the user in feet.
# Display the area of the field in acres. Hint: The area is 43,5 square km. Use different string formating!
sqr_feet_per_km = 43.5
length = float(input("Enter the lenght of the plot in feet: "))
width = float(input("Enter the width of the plot in feet: "))

area = length * width / sqr_feet_per_km
print ("The area of the farmer field is %.2f in km" % area)