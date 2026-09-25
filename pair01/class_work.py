# a = 12
# b = 12.4
# c = 'hello'
# d = True

# print(a+b)

# a = input("Введи перше число: ")
# b = input("Введи друге число: ")

# print(int(a) + int(b)) #конкатенація
# print(a + b)

# int()
# float()
# str()
# bool()

# + -
# *    /    %    //
# **

# a=int(input("#1 "))
# b=int(input("#2 "))
# c=int(input("#3 "))

a, b, c = map(int, input("Введіть три числа через пробіл: ").split())

if a > b:
    if a > c:
        print(a)
    else:
        print(c)
elif b > a:
    if b > c:
        print(b)
    else:
        print(c)
elif c > a: 
    if c > b:
        print(c)
    else:
        print(b)
else:
    print("a == b == c")