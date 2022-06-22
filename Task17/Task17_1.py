class Animal:
    pass

    def talk(self, pat):
        if pat == 'Dog':
            print ("woof woof")
        if pat == 'Cat':
            print('meow')

class Dog(Animal):

    def talk(self):
        print("woof woof")

class Cat(Animal):

    def talk(self):
        print('meow')

def pat_talk(pat):
    pat.talk()


a = Animal() # Implementation through main class
b = Animal()
a.talk('Dog')
b.talk("Cat") # ___________
c = Dog()   # Implementation through derived class
d = Cat()
c.talk()
d.talk()  # _______________

pat_talk(c) # simple function generating call of appropriate class
pat_talk(d) # _____________

