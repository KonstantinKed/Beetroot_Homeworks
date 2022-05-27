# Task 1
# Make a program that has some sentence (a string) on input and returns a dict containing all unique words as keys and the number of occurrences as values.

text = input("Enter your text: ").strip().split()

our_dic ={}
for i in text:
    rep = 1
    if text.count(i) > 1:
        rep += 1
    our_dic.update({i: rep})
print(our_dic)

# Task 2
# Create a function which takes as input two dicts with structure mentioned above, then computes and returns the total price of stock.

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}

prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

def total_calc(a, b):
    total_dic = {}
    total = 1
    for i, j in a.items():
        for k, p in b.items():
            if i == k:
                total = j * p
            total_dic.update({i: total})
    return total_dic
print(total_calc(stock, prices))


# Task 3
# List comprehension exercise
# Use a list comprehension to make a list containing tuples (i, j) where `i` goes from 1 to 10 and `j` is corresponding to `i` squared.


buba =  [(i, i*i) for i in range (1,11)]
print(buba)