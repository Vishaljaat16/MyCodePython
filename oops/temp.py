# import classes 

# print(classes.l.name)
# print(classes.Label._Label__name11)
# print(classes.l._Lable__font)
# print(classes.l._Label__name11)
# from classes import Circle 

# c = Circle(10)
# print(c.radius)
# c.radius = 111
# print(c.radius)

#*===============================================
#^ ----- isinstance() and issubclass() -----

# class Animal:
#     pass 

# class Dog(Animal):
#     pass

# dog = Dog()

# print(isinstance(dog, Dog))
# print(isinstance(dog, Animal))
# print(issubclass(Dog, Animal))


# import dundermethod 

# print(__name__)

# l = [0,0,0,0,0,0,1,0,]
# print(any(l))
# print(all(l))


# from encapsulation import Student

# s = Student("Vishal",111, 99, 22000)
# s.display()
# print()
# s._marks = 77
# s._Student__amount = 33000
# s.display()


# def my():
#     try:
#         return "HELLO"
#     finally:
#         print("HII")

# print(my())









#*===================================================
# 
# from math import pi

# class Shape:
#     def __init__(self, shape_type, **kwargs):
#         self.shape_type = shape_type
#         if self.shape_type == "rectangle":
#             self.width = kwargs["width"]
#             self.height = kwargs["height"]
#         elif self.shape_type == "circle":
#             self.radius = kwargs['radius']
#         else:
#             raise TypeError("Unsupported shape type")

#     def calculate_area(self):
#         if self.shape_type == "rectangle":
#             return self.width * self.height
#         elif self.shape_type == "circle":
#             return pi * self.radius**2
#         else:
#             raise TypeError("Unsupported shape type")

# s = Shape("rectangle", height=10, width = 20)
# print(s.calculate_area())


#* ======================================================

from collections import defaultdict

# letter_counts = defaultdict(int)

# text = "apple"

# for letter in text:
#     letter_counts[letter] += 1

# print(letter_counts)

# grouped_words = defaultdict(list)

# words = ['apple','banana','apricot','blueberry']

# for word in words:
#     first_letter = word[0]
#     grouped_words[first_letter].append(word)

# print(grouped_words)

a = 1
b = 1
# print(((a and b) or (a==b==None)))
if (a and b) or (a==b==None):
    print("True")
else:
    print("False")