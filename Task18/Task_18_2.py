# Implement 2 classes, the first one is the Boss and the second one is the Worker.
#
# Worker has a property 'boss', and its value must be an instance of Boss.
#
# You can reassign this value, but you should check whether the new value is Boss.
# Each Boss has a list of his own workers. You should implement a method that allows you
# to add workers to a Boss. You're not allowed to add instances of Boss class to workers
# list directly via access to attribute, use getters and setters instead!

import random

class Boss:

    def __init__(self, id_: int, name: str, company: str):
        self.id = id_
        self.name = name
        self.company = company
        self.workers = []

    def add_workers(self, worker):
        self.workers.append(worker)

    def remove_workers(self, worker):
        self.workers.remove(worker)

    def __repr__(self):
        wrk_list = ''
        for wrk in self.workers:
            wrk_list += f'{wrk.name}(id: {wrk.id}), '
        return (f'Boss id: {self.id}, Name: {self.name} has following workers: '+str(wrk_list))

class Worker:

    def __init__(self, id_: int, name: str, company: str, boss: Boss):
        self.id = id_
        self.name = name
        self.company = company
        self.__boss = boss

    @property
    def boss(self):
        return self.__boss

    @boss.setter
    def boss(self,value):
        if isinstance(value, Boss):
            self.__boss = value


b1 = Boss(random.randint(1, 100), "Guido", "Promo")
b2 = Boss(random.randint(1, 100), "Robert", "S1")
b3 = Boss(random.randint(1, 100), "Jonny", "P3")

w1 = Worker(random.randint(1, 100), "Paul", b1.company, b1)
w2 = Worker(random.randint(1, 100), "Carl", b2.company, b2)
w3 = Worker(random.randint(1, 100), "Craig", b1.company, b1)
w4 = Worker(random.randint(1, 100), "Mike", b2.company, b2)
w5 = Worker(random.randint(1, 100), "Tony", b1.company, b1)
w6 = Worker(random.randint(1, 100), "Liza", b3.company, b3)
w7 = Worker(random.randint(1, 100), "Elli", b3.company, b3)
w8 = Worker(random.randint(1, 100), "Katty", b3.company, b3)

b1.add_workers(w1)
b2.add_workers(w2)
b1.add_workers(w3)
b2.add_workers(w4)
b1.add_workers(w5)
b3.add_workers(w6)
b3.add_workers(w7)
b3.add_workers(w8)
print('--------LIST OF WORKERS PER BOSS--------')
print(b1)
print(b2)
print(b3)
print('----------WORKER CHANGES BOSS----------')
print(w1.boss.name,f'- current boss of {w1.name}')
w1.boss = b3
# QUESTION--> HOW CAN WE ADJUST THE LIST ONCE WE DECIDE LOCALLY CHANGE THE BOOS OF THE WORKER.
print(w1.boss.name,f'- new boss of {w1.name}')
print('----UPDATED LIST OF WORKERS PER BOSS-----')
b1.remove_workers(w1) # METHOD TO REMOVE WORKER FROM BOSS
b3.add_workers(w1)
print(b1)
print(b2)
print(b3)