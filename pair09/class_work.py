# class Book:
#     def __init__(self, title, author, copies):
#         self.title = title
#         self.author = author
#         self.copies = copies
#     def available(self):
#         return self.copies > 0
# book1 = Book("Кобзар", "Тарас Шевченко", 15)
# print(book1.title, book1.author, book1.copies)
# print(book1.available())

# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#     def area(self):
#         return self.width * self.height
#     def perimeter(self):
#         return 2 * (self.width + self.height)
#     def info(self):
#         print(f"rectangle width: {self.width}")
#         print(f"rectangle height: {self.height}")
#         print(f"rectangle area: {self.area()}")
#         print(f"rectangle perimeter: {self.perimeter()}")
# rectangle = Rectangle(100, 200)
# rectangle.info()

# class Counter:
#     def __init__(self):
#         self.value = 0
#     def increment(self):
#         self.value += 1
# counter1 = Counter()
# counter2 = Counter()
# print(f"було: {counter1.value, counter2.value}")
# counter1.increment()
# counter2.increment()
# print(f"стало: {counter1.value, counter2.value}")

