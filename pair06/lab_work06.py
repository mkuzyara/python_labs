import math
import random
import statistics
import datetime
#1
# r = int(input("Радіус: "))
# katet = input("Катети через кому: ")
# katets = katet.split(',')
# n = int(input("Предметів: "))
# k = int(input("В упаковці: "))
# print("Площа круга: ", round((math.pi*r**2), 2))
# print("Гіпотенуза: ", math.sqrt(int(katets[0])**2+int(katets[1])**2))
# print("Кількість упаковок: ", math.ceil(n/k))
#2
# n = int(input("N = "))
# if n <= 0:
#     print("N має бути більше 0")
#     exit()
# grades = []
# for i in range(n):
#     grades.append(random.randint(1, 12))
# print("Оцінки: ", grades)
# print("Min: ", min(grades))
# print("Max: ", max(grades))
# print("Середнє: ", round(statistics.mean(grades), 1))
# print("Медіана: ", statistics.median(grades))
# print("Оцінок 10-12: ", grades.count(10) + grades.count(11) + grades.count(12))
#3
# date = input("Дата події: ")
# year, month, day = date.split("-")
# event_date = datetime.date(int(year), int(month), int(day))
# today = datetime.date.today()
# difference = event_date - today
# if difference.days > 0:
#     print(f"До події залишилось {difference.days} днів")
# elif difference.days < 0:
#     print(f"Подія відбулась {-difference.days} днів тому")
# elif difference.days == 0:
#     print("Подія відбудеться сьогодні")