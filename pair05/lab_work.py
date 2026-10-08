import math
#1
# def circle_s():
#     r = int(input("R= "))
#     pi = 3.14159
#     return pi * r ** 2
# def rectangle_s():
#     a = int(input("Ширина= "))
#     b = int(input("Висота= "))
#     return a * b
# def triangle_s():
#     a = int(input("1 сторона= "))
#     b = int(input("2 сторона= "))
#     c = int(input("3 сторона= "))
#     p = (a + b + c) / 2
#     return math.sqrt(p * (p - a) * (p - b) * (p - c))
# def main():
#     print("1) площа кола")
#     print("2) площа прямокутника")
#     print("3) площа трикутника")
#     choice = int(input("Виберіть фігуру (номер): "))
#     if choice == 1:
#         s = circle_s()
#         print("Площа кола: ", s)
#     elif choice == 2:
#         s = rectangle_s()
#         print("Площа прямокутника: ", s)
#     elif choice == 3:
#         s = triangle_s()
#         print("Площа трикутника: ", s)
#     else:
#         print("Невірний вибір")
# main()
#2
# def is_prime(n):
#     if n < 2:
#         return False
#     if n < 4:
#         return True
#     if n % 2 == 0:
#         return False
#     for i in range(3, int(math.sqrt(n)) + 1, 2):
#         if n % i == 0:
#             return False
#     return True
# def divisors(n):
#     small, large = [], []
#     for i in range(1, int(math.sqrt(n)) + 1):
#         if n % i == 0:
#             small.append(i)
#             if i != n // i:
#                 large.append(n // i)
#     return small + large
# def digit_sum(n):
#     n = abs(n)
#     total = 0
#     while n > 0:
#         total += n % 10
#         n //= 10
#     return total
# def main():
#     n = int(input("Введіть число: "))
#     if is_prime(n):
#         print(f"Просте число: так")
#     else:
#         print(f"Просте число: ні")
#     divisors(n)
#     print("Дільники: ", divisors(n))
#     digit_sum(n)
#     print("Сума цифр: ", digit_sum(n))
# main()
#3
# grades = [10, 8, 12, 9, 11]
# value = 9
# def average(grades):
#     return sum(grades) / len(grades)
# def minimum(grades):
#     return min(grades)
# def maximum(grades):
#     return max(grades)
# def count_above(grades, value):
#     count = 0
#     for i in range(len(grades)):
#         if grades[i] > value:
#             count += 1
#     return count
# def main():
#     print("Середній бал:", average(grades))
#     print("Мінімальна:", minimum(grades))
#     print("Максимальна:", maximum(grades))
#     print("Вище 9:", count_above(grades, value))
# main()
#4
def min_len(password):
    min_len = False
    if len(password) >= 8:
        min_len = True
    return min_len
def has_num(password):
    has_num = False
    numbers = ("0123456789")
    for i in range(len(password)):
        if password[i] in numbers:
            has_num = True
            break
    return has_num
def has_upper(password):
    has_upper = False
    pass_upper = password.upper()
    for i in range(len(password)):
        if password[i] == pass_upper[i]:
            has_upper = True
            break
    return has_upper
def has_lower(password):
    has_lower = False
    pass_lower = password.lower()
    for i in range(len(password)):
        if password[i] == pass_lower[i]:
            has_lower = True
            break
    return has_lower
def has_special(password):
    has_special = False
    special = ("!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~")
    for i in range(len(password)):
        if password[i] in special:
            has_special = True
            break
    return has_special
def check_password(password):
    password_safe = False
    if min_len(password) == True and has_num(password) == True and has_upper(password) == True and has_lower(password) == True and has_special(password) == True:
        password_safe = True
    else:
        print("Пароль не відповідає вимогам.")
        if min_len(password) == False:
            print("Не виконано: пароль менше 8 символів")
        if has_num(password) == False:
            print("Не виконано: пароль не містить цифр")
        if has_upper(password) == False:
            print("Не виконано: пароль не містить великих літер")
        if has_lower(password) == False:
            print("Не виконано: пароль не містить малих літер")
        if has_special(password) == False:
            print("Не виконано: немає спеціального символу")
password = input("Пароль =")
check_password(password)