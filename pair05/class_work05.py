#функція без параметрів
# def say_hello():
#     print("Привіт, Python!")
#     say_hello()

#функція з параметром
# def greet(name):
#     print(f"Привіт, {name}!")
#     greet("Misha")

#функція з return
# def area_rectangle(a, b):
#     return a * b
# area = area_rectangle(7, 4)
# print("Площа:", area)

#print() i return 
# def square_print(x):
#     print(x * x)
# def square_return(x):
#     return x * x
# square_print(5)
# result = square_return(5)
# print("Результат можна використати:", result + 10)

#параметр за замовчуванням
# def greet(name, message="Привіт"):
#     print(f"{message}, {name}!")
# greet("Misha")
# greet("Brazhnik", "Добрий день")

#іменовані аргументи
# def student_info(name, group, grade):
#     print(f"{name}: група {group}, оцінка {grade}")
# student_info(grade=9, name="Misha", group="10-IT")

#повернення двох значень
# def min_max(numbers):
#     return min(numbers), max(numbers)
# minimum, maximum = min_max([7, 2, 15, 4, 9])
# print("Min:", minimum)
# print("Max:", maximum)

#функція перевірки значення
# def is_valid_grade(grade):
#     return 1 <= grade <= 12
# grade = int(input("Оцінка: "))
# if is_valid_grade(grade):
#     print("Коректна оцінка")
# else:
#     print("Помилка")

#кілька функція для аналізу списку
# def average(numbers):
#     return sum(numbers) / len(numbers)
# def count_positive(numbers):
#     count = 0
#     for number in numbers:
#         if number > 0:
#             count += 1
#     return count
# numbers = [4, -2, 8, 0, 5]
# print("Середнє:", average(numbers))
# print("Додатних:", count_positive(numbers))

#*args
# def total_sum(*numbers):
#     total = 0
#     for number in numbers:
#         total += number
#     return total
# print(total_sum(5, 10))
# print(total_sum(1, 2, 3, 4, 5))

#main() кординує програму
# def area_rectangle(a, b):
#     return a * b
# def main():
#     width = float(input("Ширина: "))
#     height = float(input("Висота: "))
#     result = area_rectangle(width, height)
# print("Площа:", result)
# main()

#декомпозиція програми
# def input_grades():
#     return [10, 8, 12, 9, 11]
# def average(grades):
#     return sum(grades) / len(grades)
# def best_grade(grades):
#     return max(grades)
# def print_report(grades):
#     print("Оцінки:", grades)
#     print("Середній бал:", round(average(grades), 2))
#     print("Найкраща оцінка:", best_grade(grades))
# def main():
#     grades = input_grades()
#     print_report(grades)
# main()