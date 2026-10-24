class Person:
    def __init__(self, name):
        self.name = name
    def info(self):
        return self.name
class Student(Person):
    def __init__(self, name, group):
        super().__init__(name)
        self.group = group
    def info(self):
        return f"{self.name}, {self.group}"
class Teacher(Person):
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject
    def info(self):
        return f"{self.name}, {self.subject}"
class Course:
    def __init__(self, name, teacher):
        self.name = name
        self.teacher = teacher
        self.students = []
# student = Student("Brazhnik", "10B")
# person = Person("Lyvova")
# print(student.name)
# print(student.group)
# print(person.info())
# print(student.info())

people = [Person("Brazhnik"), Student("Zozulya", "10B"), Teacher("Pan Pavlo", "Math"), Student("Pikulytskyi", "10B")]
for person in people:
    print(person.info())