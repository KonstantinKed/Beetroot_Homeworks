# Task 1
# School
# Make a class structure in python representing people at school. Make a base class called Person, a class
# called Student, and another one called Teacher. Try to find as many methods and attributes as you can which
# belong to different classes, and keep in mind which are common and which are not. For example, the name should be
# a Person attribute, while salary should only be available to the teacher.

class Person:
    person_amount = 0

    def __init__(self, first_name, last_name, age, position):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.position = position
        Person.person_amount += 1

    def get_person_info(self):
        return "Name: " + self.first_name + ", Last name: " + ", age"

    def food_budget(self):
        sum_food_budget = Person.person_amount * 1000  # Assuming we need $1000 per year per 1 person food preparation
        return sum_food_budget

    # def total_budget(self):
    #     return sum (sum_food_budget+)

class Student(Person):
    score_rate = []
    total_score = {}

    def __init__(self, first_name, last_name, age, st_book, position="Student"):
        super().__init__(first_name, last_name, age, position)
        self.st_book = st_book

    def get_person_info(self):
        return "Name: " + self.first_name + ", Last name: " + self.last_name + ", age: " + str(
            self.age) + ", position: " + self.position + ", student book: " + str(self.st_book)

    def get_total_score(self):
        Student.total_score = {'last_name': self.last_name, 'total_score': sum(self.st_book.values())}
        Student.score_rate.append(Student.total_score)
        return Student.score_rate

    def rate_calc(self):
        return sorted(Student.score_rate, key=lambda item: item['total_score'], reverse=True)

class Teacher(Person):
    total_salary = {}
    annual_salary = []

    def __init__(self, first_name, last_name, age, salary, position="Teacher"):
        super().__init__(first_name, last_name, age, position)
        self.salary = salary
        pass

    def get_person_info(self):  # redefinition of the method
        return "Name: " + self.first_name + ", Last name: " + self.last_name + ", age: " + str(
            self.age) + ", position: " + self.position + ", salary: $" + str(self.salary)


    def get_annual_salary(self):
        Teacher.total_salary = {'last_name': self.last_name, 'annual_salary': self.salary*12}
        Teacher.annual_salary.append(Teacher.total_salary)
        return Teacher.annual_salary

    def annual_teacher_budget(self):
        return sum(i['annual_salary'] for i in Teacher.annual_salary)

# def total_budget(*args):  HOW to calculate results of methods from two different classes??????
#     return sum (args)
#
# total_budget(Person.food_budget(self), Teacher.annual_teacher_budget())

p1 = Student("Alex", "Parkinson", 21, {"Math": 80, "Physics": 89, "History": 70})
p2 = Student("John", "Deer", 20, {"Math": 70, "Physics": 59, "History": 99})
p3 = Student("Emma", "Bird", 19, {"Math": 97, "Physics": 98, "History": 71})
p4 = Student("James", "Watson", 22, {"Math": 84, "Physics": 83, "History": 75})
t1 = Teacher("Melinda", "Simons", 54, 4000)
t2 = Teacher("Maya", "Soe", 44, 3000)
t3 = Teacher("Emma", "Loe", 29, 2000)
t4 = Teacher("Carla", "Rudy", 54, 5000)
print(p1.get_person_info())

print(t1.get_person_info())
p1.get_total_score()
p2.get_total_score()
p3.get_total_score()
p4.get_total_score()
print("____________")
print("University rate of students: ",p1.rate_calc())
print("____________")
t1.get_annual_salary()
t2.get_annual_salary()
t3.get_annual_salary()
print("List of teacher's salary: ",t4.get_annual_salary())
print("____________")
print("Teacher's annual salary: ",p1.rate_calc())
print("Teacher's budget:",t1.annual_teacher_budget())
print("Total persons at the university:", Person.person_amount)
print("Total food budget:",p1.food_budget())
# print(total_budget())