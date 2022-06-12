# Task 1

# A Person class
# Make a class called Person. Make the __init__() method take firstname, lastname, and age as
# parameters and add them as attributes. Make another method called talk() which makes prints a greeting
# from the person containing, for example like this: “Hello, my name is Carl Johnson and I’m 26 years old”.

class Person:

    def __init__(self, firstname, lastname, age):
        self.age = age
        self.lastname = lastname
        self.firstname = firstname

    def talk(self):
        print(f"Hello, my name is {self.firstname} {self.lastname}, and I'm {self.age} years old")


p1 = Person("Rob", "Robson", 25)
p2 = Person("Steve", "Cooker", 30)
p3 = Person("Martin", "Bulk", 50)

p1.talk()
p2.talk()
p3.talk()