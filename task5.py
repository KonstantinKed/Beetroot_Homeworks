# Task 1
# The Guessing Game.
# Write a program that generates a random number between 1 and 10 and lets the user guess what number was generated.
# The result should be sent back to the user via a print statement.

import random
i = 0
while i < 5:
    comp_choice = (random.randint(1,10))
    player_choice = int(input("Enter any number from 1 to 10: "))
    win_counter = 0
    if 0 < player_choice <= 10:
        i += 1
        if comp_choice ==player_choice:
            print(f"You are lucky dude, by typing {player_choice} you guessed the number!")
            win_counter +=1
        else:
            print(f"You selected {player_choice} and computer selected {comp_choice}. Give another try")
    else:
        print("You chose a wrong number. Please make a choice from 0 to 10!!!")
print(f"The Game is OVER. You win {win_counter} times!")

# Task 2
# The birthday greeting program.
# Write a program that takes your name as input, and then your age as input and greets you with the following:
# “Hello <name>, on your next birthday you’ll be <age+1> years”
name = str(input("Please enter your name: "))
age = int(input("PLease enter your full age: "))
print(f"Hello {name}, on your next birthday you'll be", age + 1, "years")

# Task 3
# Words combination
# Create a program that reads an input string and then creates and prints 5 random strings from characters of the input string.
# For example, the program obtained the word ‘hello’, so it should print 5 random strings(words) that
# combine characters ‘h’, ‘e’, ‘l’, ‘l’, ‘o’ -> ‘hlelo’, ‘olelh’, ‘loleh’ …
# Tips: Use random module to get random char from string)

import random

word = str(input("Enter the word: "))
a = 0
while a < 5:
    print(f'word{a + 1} = ', end='')
    new_word = ""
    while len(new_word) <= len(word)-1:
        new_letter = word[random.randint(0, len(word)-1)]
        if new_letter not in new_word:
            new_word += new_letter
        elif word.count(new_letter) > 1 and new_word.count(new_letter) < word.count(new_letter):
            new_word += new_letter
    print(new_word, end='\t')
    a += 1

# Task 4 QUIZZZZ
# The math quiz program
# Write a program that asks the answer for a mathematical expression, checks whether the user is right or wrong,
# and then responds with a message accordingly.

import random
i = 0 # counter of used question
correct = 0 # counter of right answers
wrong = 0 # counter of wrong answers
repeat = ""
while i < 5:
    a = random.randint(1, 5)
    if str(a) not in repeat:  # condition to avoid questions repeating
        i += 1
        if a == 1:   # First question
            answer_1 = int(input("Please count the following expression: 2+2/2*8: "))
            if answer_1 == 10:
                correct += 1
            else:
                wrong += 1
        elif a == 2:   # Second question
            answer_2 = int(input("If 1=3, 2=3, 3=5, 4=4, 5=4, then 6=?: "))
            if answer_2 == 3:
                correct += 1
            else:
                wrong += 1
        elif a == 3:   # Third question
            answer_3 = int(input("Which number is equivalent (3**4)/(3**2): "))
            if answer_3 == 9:
                correct += 1
            else:
                wrong += 1
        elif a == 4:   # Forth question
            answer_4 = int(input("I am an odd number. Take away one letter and I become EVEN. What number am I?: "))
            if answer_4 == 7:
                correct += 1
            else:
                wrong += 1
        else:          # Fifth question
            answer_5 = int(input("Look at this series: 22, 21, 23, 22, 24, 23, … What number should come next: "))
            if answer_5 == 25:
                correct += 1
            else:
                wrong += 1
    repeat += str(a)
print (f"You have {correct} correct answer(s) and {wrong} wrong answer(s)", end="\n\n")
print("Log of random output: ", repeat) # log of random module work