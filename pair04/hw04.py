#1
# numbers = [12, 3, 4, 14, -12, 5, 10, 16, -4]
# pos = []
# neg = []
# par = []
# kratni = []

# for i in range(len(numbers)):
#     if numbers[i] > 0:
#         pos.append(numbers[i])
#     elif numbers[i] < 0:
#         neg.append(numbers[i])
#     if numbers[i] % 2 == 0:
#         par.append(numbers[i])
#     if numbers[i] % 3 == 0:
#         kratni.append(numbers[i])
# print("Додатні:", pos)
# print("Від'ємні:", neg)
# print("Парні:", par)
# print("Кратні 3:", kratni)
# print("Sum:", sum(numbers))
# print("Average:", round(sum(numbers) / len(numbers), 2))
# for i in range(len(numbers)):
#     if numbers[i] == max(numbers):
#         print("Max:", numbers[i])
#     if numbers[i] == min(numbers):
#         print("Min:", numbers[i])
#2
# group1 = {'Anna','Ivan','Olha'}
# group2 = {'Ivan','Maksym','Olha'}
# common = set()
# only_group1 = set()
# only_group2 = set()
# all = set()
# for i in group1:
#     if i in group2:
#         common.add(i)
#     else:
#         only_group1.add(i)
# for i in group2:
#     if i not in group1:
#         only_group2.add(i)
# for i in group1:
#     all.add(i)
# for i in group2:
#     all.add(i)
# print("Спільні:", common)
# print("Тільки в group1:", only_group1)
# print("Тільки в group2:", only_group2)
# print("Усі:", all)
#3
# catalog = {
#     "milk": 48,
#     "tea": 75,
# }
# while True:
#     choice = input("Що ви хочете зробити? (add/change/search/searchbyprice/exit): ")
#     if choice == "add":
#         name = input("Назва товару: ")
#         price = int(input("Ціна товару: "))
#         catalog[name] = price
#     if choice == "change":
#         name = input("Назва товару: ")
#         if name in catalog:
#             price = int(input("Нова ціна товару: "))
#             catalog[name] = price
#         else:
#             print("Товар не знайдено")
#     if choice == "search":
#         name = input("Назва товару: ")
#         if name in catalog:
#             print("Ціна товару:", catalog[name], "грн")
#         else:
#             print("Товар не знайдено")
#     if choice == "searchbyprice":
#         min_price = int(input("Мінімальна ціна: "))
#         max_price = int(input("Максимальна ціна: "))
#         found = False
#         for name in catalog:
#             if min_price <= catalog[name] <= max_price:
#                 print(name, "-", catalog[name], "грн")
#                 found = True
#         if not found:
#             print("Товарів у цьому діапазоні не знайдено")
#     if choice == "exit":
#         break
#     else:
#         print("Неправильна команда")
#5
group_info = ('10-IT', '2026/2027')
grades = {
    "Anna": [10, 11, 12, 9, 10],
    "Ivan": [8, 9, 10, 11, 9]
}
while True:
    choice = input("Що ви хочете зробити? (add/print/average/rating/highestavg/exit): ")
    if choice == "add":
        name = input("Ім'я учня: ")
        grades_input = input("Введіть 5 оцінок через пробіл: ")
        new_grades = []
        for i in grades_input.split():
            new_grades.append(int(i))
        if len(new_grades) == 5:
            grades[name] = new_grades
            print("Учня додано")
        else:
            print("Потрібно рівно 5 оцінок")
    elif choice == "print":
        print(group_info[0], "-", group_info[1])
        for name in grades:
            print(name, "-", grades[name])
    elif choice == "average":
        print(group_info[0], "-", group_info[1])
        for name in grades:
            avg = sum(grades[name]) / len(grades[name])
            print(name, "-", round(avg, 2))
    elif choice == "rating":
        averages = {}
        for name in grades:
            averages[name] = sum(grades[name]) / len(grades[name])
        sorted_names = sorted(averages, key=averages.get, reverse=True)
        place = 1
        for name in sorted_names:
            print(str(place) + ".", name, "-", round(averages[name], 2))
            place += 1
    elif choice == "highestavg":
        best_name = ""
        best_avg = -1
        for name in grades:
            avg = sum(grades[name]) / len(grades[name])
            if avg > best_avg:
                best_avg = avg
                best_name = name
        print("Найвищий середній бал:", best_name, "-", round(best_avg, 2))
    elif choice == "exit":
        break
    else:
        print("Неправильна команда")