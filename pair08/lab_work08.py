#1
# a = input("A: ")
# b = input("B: ")
# op = input("Операція: ")
# numbers = ("1234567890")

# if a in numbers and b in numbers:
#     a = int(a)
#     b = int(b)
#     if op == "+":
#         print(a + b)
#     elif op == "-":
#         print(a - b)
#     elif op == "*":
#         print(a * b)
#     elif op == "/":
#         if b != 0:
#             print(a / b)
#         else:
#             raise ZeroDivisionError("Ділення на нуль")
#     else:
#         raise ValueError ("Невідома операція")
# else: 
#     raise ValueError("Введено не число")
#2
# def input_grade():
#     while True:
#         try:
#             grade = int(input("Оцінка: "))
#             if grade < 1 or grade > 12:
#                 raise ValueError("Помилка: оцінка повинна бути від 1 до 12")
#             else:
#                 print(f"Прийнято: {grade}")
#         except ValueError:
#             print("Помилка: потрібно ввести ціле число")
# input_grade()
#3
# students = ["Ivan", "Artem", "Platon", "Brazhnik", "Danylo"]
# grades = {
#     "Математика": 5,
#     "Фізика": 4,
#     "Пайтон": 7,
#     "Англійський": 3
# }
# while True:
#     choice = input("1 - учень, 2 - предмет: ")
#     if choice == "1":
#         index = int(input("Індекс: "))
#         if 0 <= index < len(students):
#             print(f"Учень: {students[index]}")
#         else:
#             raise IndexError("Помилка: учня з таким індексом немає")
#     elif choice == "2":
#         index = int(input("Індекс: "))
#         if 0 <= index < len(grades):
#             subject_name = list(grades.keys())[index]
#             print(f"Оцінка з предмета {subject_name}: {grades[subject_name]}")
#         else:
#             raise KeyError("Помилка: предмета з таким індексом немає")
#     else:
#         raise ValueError("Помилка: невірний вибір")
#4
incorrect = 0
try:
    with open("students.txt", "r", encoding="utf-8") as file:
        students = file.readlines()
    correct = []
    for i in enumerate(students, start=1):
        line = i[1].strip()
        if ";" not in line:
            print(f"Помилка: рядок {i[0]} не містить роздільника ';'")
            incorrect += 1
            continue
        parts = line.split(";")
        if len(parts) != 2:
            print(f"Помилка: рядок {i[0]} в неправильному форматі")
            incorrect += 1
            continue
        student, grade = parts[0].strip(), parts[1].strip()
        if not student:
            print(f"Помилка: рядок {i[0]} не містить імені учня")
            incorrect += 1
            continue
        try:
            value = int(grade)
        except ValueError:
            try: 
                value = float(grade)
            except ValueError:
                print(f"Помилка: рядок {i[0]} містить нечислову оцінку")
                incorrect += 1
                continue
            print(f"Помилка: рядок {i[0]} містить не цілу оцінку")
            incorrect += 1
            continue
        if not 0 <= value <= 100:
            print(f"Помилка: рядок {i[0]} містить оцінку поза діапазоном 0-100")
            incorrect += 1
            continue
        else:
            correct.append(line)
    with open("report.txt", "w", encoding="utf-8") as file:
        for line in correct:
            file.write(line + "\n")
    print("Правильних записів:", len(correct))
    print("Неправильних записів:", incorrect)
    print("Створено report.txt")

except FileNotFoundError:
    print("Помилка: файл students.txt не існує")