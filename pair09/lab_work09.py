#1
# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#     def area(self):
#         return self.width * self.height
#     def perimeter(self):
#         return 2 * (self.width + self.height)
#     def info(self):
#         print(f"ширина: {self.width}")
#         print(f"висота: {self.height}")
#         print(f"площа: {self.area()}")
#         print(f"периметр: {self.perimeter()}")
# rectangle1 = Rectangle(5, 3)
# rectangle1.info()
# rectangle2 = Rectangle(10, 4)
# rectangle2.info()
#2
# class Student:
#     def __init__(self, name, grades):
#         self.name = name
#         self.grades = grades
#     def add_grade(self, grade):
#         if grade >= 1 and grade <= 12:
#             self.grades.append(grade)
#     def average(self):
#         if len(self.grades) == 0:
#             return 0
#         return round(sum(self.grades) / len(self.grades), 2)
#     def __str__(self):
#         print(f"{self.name}: {self.grades}, середній = {self.average()}")
# student = Student("Ivan Petrenko", [])
# student.add_grade(10)
# student.add_grade(12)
# student.add_grade(15)
# student.add_grade(9)
# student.__str__()
#3
# class Student:
#     def __init__(self, name, grades=None):
#         self.name = name
#         self.grades = list(grades) if grades else []
#     def add_grade(self, grade):
#         if grade >= 1 and grade <= 12:
#             self.grades.append(grade)
#     def average(self):
#         if len(self.grades) == 0:
#             return 0
#         return round(sum(self.grades) / len(self.grades), 2)
#     def __str__(self):
#         return f"{self.name} -- {self.average()}"

# class Grades:
#     def __init__(self):
#         self.students = {}

#     def add_student(self, name, grades=None):
#         self.students[name] = Student(name, grades)
#         return self.students[name]

#     def add_grade(self, name, grade):
#         self.students[name].add_grade(grade)

#     def show_all(self):
#         for student in self.students.values():
#             print(student)
#     def top(self):
#         best = None
#         for student in self.students.values():
#             if best is None or student.average() > best.average():
#                 best = student
#         return best
# book = Grades()
# book.add_student("Anna", [10, 11, 9])
# book.add_student("Ivan", [7, 8])
# book.add_student("Olha", [12, 12, 11])
# book.add_student("Brazhnik", [2, 3, 4])
# book.add_student("Misha", [9, 8, 10])
# book.show_all()
# print(f"Найкращий результат: {book.top()}")
#4
class Wallet:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
        else:
            print(f"Помилка: недостатньо коштів для -{amount}")
    def info(self):
        print(f"{self.owner}: баланс {self.balance}")
ivan = Wallet("Ivan", 1000)
ivan.deposit(500)
ivan.withdraw(300)
ivan.withdraw(2000)
ivan.info()
olha = Wallet("Olha", 700)
olha.withdraw(200)
olha.deposit(100)
olha.info()