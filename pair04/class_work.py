# #list - список
# grades = [8, 9, 10]

# #tuple - кортежі
# point = (10, -12)

# #set - множини
# subjects = {"Python", "HTML", "CSS", "JavaScript"}

# #dict - словники
# student = {
#     "name": "Brazhnik",
#     "grade": 11
# }

# numbers = []

# numbers.append(10)
# numbers.append(4)
# numbers.insert(1, [5, 6])
# numbers.extend([7, 8, 9, 7, 8, 5, 8])
# numbers.remove(7)
# numbers.pop(1)
# print(numbers.count(8))
# print(numbers.index(8))

# print(8 in numbers)

# print(numbers)


numbers = [1, 4, 6, 8, 3]
numbers.sort(reverse=True)
print(numbers)

new_numbers = sorted(numbers)
print(new_numbers)