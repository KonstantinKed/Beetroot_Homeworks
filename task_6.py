# Task 1
# The greatest number
# Write a Python program to get the largest number from a list of random numbers with the length of 10
# Constraints: use only while loop and random module to generate numbers

import random
i = 0
our_list_1 = []
while i < 10:
    n = random.randint(0, 100)
    our_list_1.append(n)
    i += 1
print (our_list_1, "\n", max(our_list_1))

# to practice with random SAMPLE

newlist = random.sample(range(1,100), 10)
print (newlist, "\n", max(newlist))

# Task 2
# Exclusive common numbers.
# Generate 2 lists with the length of 10 with random integers from 1 to 10,
# and make a third list containing the common integers between the 2 initial lists without any duplicates.
# Constraints: use only while loop and random module to generate numbers

import random
i = 0
our_list_2 = []  # our_list_1 comes from the previous task!
while i < 10:
    n = random.randint(0, 100)
    our_list_2.append(n)
    i += 1
b = 0
while b < len(our_list_2)-1:
    if our_list_2[b] not in our_list_1:
        our_list_1.append(our_list_2[b])
    b += 1

print (our_list_1, our_list_2)

# Task 3
# Extracting numbers.
# Make a list that contains all integers from 1 to 100, then find all integers from the list that are divisible by 7
# but not a multiple of 5, and store them in a separate list. Finally, print the list.
# Constraint: use only while loop for iteration.

i = 0
y = 0
list_hundred = []
list_final = []
while i <= 100:
    list_hundred.append(i)
    i += 1
while y < len(list_hundred)-1:
    if list_hundred[y] % 7 == 0 and list_hundred[y] % 5 != 0:
        list_final.append(list_hundred[y])
    y += 1
print(list_final)