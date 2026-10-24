#1
# class Person:
#     def __init__(self, name):
#         self.name = name
#     def info(self):
#         return self.name
# class Student(Person):
#     def __init__(self, name, group):
#         super().__init__(name)
#         self.group = group
#     def info(self):
#         return f"Учень: {self.name}, Група: {self.group}"
# student = Student("Anna Ivanenko", "10IT")
# print(student.info())
#2
# class Person:
#     def __init__(self, name):
#         self.name = name
#     def info(self):
#         return f"Ім'я: {self.name}"
# class Student(Person):
#     def __init__(self, name, group):
#         super().__init__(name)
#         self.group = group
#     def info(self):
#         return f"Учень: {self.name}, Група: {self.group}"
# class Teacher(Person):
#     def __init__(self, name, subject):
#         super().__init__(name)
#         self.subject = subject
#     def info(self):
#         return f"Викладач: {self.name}, Предмет: {self.subject}"
# people = [Person("Ivan Komarov"), Student("Anna Ivanenko", "10IT"), Student("Platon Brazhnik", "10B"), Teacher("Olena Kovalenko", "Python")]
# for person in people:
#     print(person.info())
#3
# class Person:
#     def __init__(self, name):
#         self.name = name
#     def info(self):
#         return f"Ім'я: {self.name}"
# class Student(Person):
#     def __init__(self, name, group):
#         super().__init__(name)
#         self.group = group
#     def info(self):
#         return f"Учень: {self.name}, Група: {self.group}"
# class Teacher(Person):
#     def __init__(self, name, subject):
#         super().__init__(name)
#         self.subject = subject
#     def info(self):
#         return f"Викладач: {self.name}, Предмет: {self.subject}"
# class Course:
#     def __init__(self, title, teacher, students):
#         self.title = title
#         self.teacher = teacher
#         self.students = []
#     def add_student(self, student):
#         if student not in self.students:
#             self.students.append(student)
#             return True
#         return False
#     def remove_student(self, name):
#         for student in self.students:
#             if student.name.lower() == name.lower():
#                 self.students.remove(student)
#                 return True 
#         return False
#     def show_students(self):
#         print(f"Курс: {self.title}")
#         print(f"Викладач: {self.teacher}")
#         print("Студенти:")
#         for i, student in enumerate(self.students, start=1):
#             print(f"{i}. {student.info()}")
# course = Course("Python", "Ivan Komarov", [])
# course.add_student(Student("Anna Ivanenko", "10IT"))
# course.add_student(Student("Platon Brazhnik", "10B"))
# course.add_student(Student("Danylo Pikulytskyi", "10B"))
# course.add_student(Student("Artem Zozulya", "10B"))
# course.remove_student("Platon Brazhnik")
# course.show_students()
#4
import os

class Person:
    def __init__(self, name):
        self.name = name
    def info(self):
        return f"Ім'я: {self.name}"
class Student(Person):
    def __init__(self, name, group, grades):
        super().__init__(name)
        self.group = group
        self.grades =list(grades)
    def info(self):
        return f"Учень: {self.name}, Група: {self.group}"
    def add_grade(self, grade):
        if grade >= 1 and grade <= 12:
            self.grades.append(grade)
    def average(self):
        if len(self.grades) == 0:
            return 0
        return round(sum(self.grades) / len(self.grades), 2)
class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject
    def info(self):
        return f"Викладач: {self.name}, Предмет: {self.subject}"
class Course:
    def __init__(self, title, teacher, students):
        self.title = title
        self.teacher = teacher
        self.students = list(students)
    def add_student(self, student):
        if student not in self.students:
            self.students.append(student)
            return True
        return False
    def remove_student(self, name):
        for student in self.students:
            if student.name.lower() == name.lower():
                self.students.remove(student)
                return True 
        return False
    def show_students(self):
        print(f"Курс: {self.title}")
        print(f"Викладач: {self.teacher.info()}")
        print("Студенти:")
        for i, student in enumerate(self.students, start=1):
            print(f"{i}. {student.info()}, Оцінки: {student.grades}")
    def find_student(self, name):
        for student in self.students:
            if student.name.lower() == name.lower():
                return student
        return None
    def add_grade_to_student(self, name, grade):
        student = self.find_student(name)
        if student:
            student.add_grade(grade)
            return True
        return False
    def show_rating(self):
        print("Рейтинг:")
        student_sort = sorted(self.students, key=lambda s: s.average(), reverse=True)
        for i, student in enumerate(student_sort, start=1):
            print(f"{i}. {student.name}: {student.average()}")
    def save_to_file(self, filename):
        filename = "course_data.txt"
        with open(filename, "w", encoding="utf-8") as file:
            file.write(f"Курс: {self.title}\n")
            file.write(f"{self.teacher.info()}\n")
            file.write("\nУчні:\n")
            for i, student in enumerate(self.students, start=1):
                grades = ", ".join(str(g) for g in student.grades) or "немає оцінок"
                file.write(f"{i}. {student.name}, Група: {student.group}, "
                           f"Оцінки: {grades}, Середній бал: {student.average()}\n")
        return True
    def load_from_file(self, filename):
        if not os.path.exists(filename):
            return None
        with open(filename, "r", encoding="utf-8") as file:
            lines = file.readlines()
            self.title = lines[0].strip().split(": ")[1]
            teacher_info = lines[1].strip().split(", ")
            self.teacher = Teacher(teacher_info[0].split(": ")[1], teacher_info[1].split(": ")[1])
            self.students = []
            for line in lines[4:]:
                parts = line.strip().split(", ")
                name = parts[0].split(". ")[1]
                group = parts[1].split(": ")[1]
                grades_str = parts[2].split(": ")[1]
                grades = [int(g) for g in grades_str.split(", ") if g.isdigit()]
                student = Student(name, group, grades)
                self.students.append(student)
if os.path.exists("course_data.txt"):
    course = Course("", None, [])
    course.load_from_file("course_data.txt")
    print("Дані курсу завантажено")
else:
    teacher = Teacher("Ivan Komarov", "Python")
    course = Course("Python", teacher, [])
while True:
    choice = int(input("Дія(1 - показати курс, 2 - додати студента, 3 - видалити студента, 4 - знайти студента, 5 - виставити оцінку, 6 - показати рейтинг, 7 - зберегти дані, 0 - вихід): "))
    if choice == 0:
        break
    if choice == 1:
        course.show_students()
    elif choice == 2:
        name = input("Введіть ім'я студента: ")
        group = input("Введіть групу студента: ")
        student = Student(name, group, [])
        course.add_student(student)
    elif choice == 3:
        name = input("Введіть ім'я студента: ")
        course.remove_student(name)
    elif choice == 4:
        name = input("Введіть ім'я студента: ")
        student = course.find_student(name)
        if student:
            print(f"Студент: {student.info()}, оцінки: {student.grades}")
        else:
            print("Студент не знайдений")
    elif choice == 5:
        name = input("Введіть ім'я студента: ")
        grade = float(input("Введіть оцінку: "))
        course.add_grade_to_student(name, grade)
    elif choice == 6:
        course.show_rating()
    elif choice == 7:
        course.save_to_file("course_data.txt")
    else:
        print("Невідома дія")