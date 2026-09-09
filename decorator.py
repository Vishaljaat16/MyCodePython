# 
#* #* Decorators in Python 
#^ Without arguments decorator 
# def my_decorator(func):
#     def wrapper(*args):
#         print("Before Decorator")
#         func()
#         print("After Decorator")
#     return wrapper 

# @my_decorator
# def greet():
#     print("Hello greeting from BridgeFix")

# greet()

#^ with arguments decorator  
# def my_decorator(func):
#     def wrapper(*args, **kwargs):
#         print("Before Decorator")
#         result = func(*args, **kwargs)
#         print("After Decorator")
#         return result 
#     return wrapper 

# @my_decorator
# def add(a,b):
#     return a+b 

# print(add(10,10))

# def my_muliplication_decorator(func):
#     def wrapper(*args):
#         print("Before Decorator")
#         result = args[0]*args[1]
#         print("After Decorator")
#         return result 
#     return wrapper 

# @my_muliplication_decorator
# def add(a,b):
#     return a+b 

# print(add(10,10))


#* function as a FIRST-CLASS objects 

# def greet(n): 
#     return f"Hello, {n}" 

# say_hi = greet 
# print(say_hi("Vishal"))

# def apply(f,v):
#     return f(v)
# res = apply(say_hi, "Vishal")
# print(res)

# def make_mult(f):
#     def mult(x):
#         return x*f 
#     return mult 

# dbl = make_mult(2)
# print(dbl(5))


#* ==== Method decorator ==== 

# def method_decorator(func):
#     def wrapper(self, *args, **kwargs):
#         print("Before method excution")
#         result = func(self, *args, **kwargs)
#         print("After method execution")
#         return result 
#     return wrapper 

# class Person:
#     @method_decorator
#     def say_hello(self):
#         print("Helloo") 

# p = Person() 
# p.say_hello()

#* ==== CLASS Decorator ==== 

# def fun(cls):
#     cls.class_name = cls.__name__ 
#     return cls 

# @fun 
# class Person:
#     pass 

# print(Person.class_name)

# class Circle:
#     def __init__(self, radius):
#         self._radius = radius

#     @property
#     def radius(self):
#         return self._radius

#     @radius.setter
#     def radius(self, value):
#         if value >= 0:
#             self._radius = value
#         else:
#             raise ValueError("Radius cannot be negative")

#     @property
#     def area(self):
#         return 3.14159 * (self._radius ** 2)

# c = Circle(5)
# print(c.radius) 
# print(c.area)    
# c.radius = 10
# print(c.area)


#* Chaining decorators

# def decor1(func):
#     def inner():
#         x = func()
#         return x*x 
#     return inner 

# def decor(func):
#     def inner():
#         x = func()
#         return 2*x 
#     return inner 

# @decor1 
# @decor 
# def num():
#     return 10

# @decor 
# @decor1 
# def num2():
#     return 10

# print(num())
# print(num2())


#* closers in python

# def outer_function(x):
#     def inner_function(y):
#         return x+y 
#     return inner_function

# closer = outer_function(10)

# print(closer(11))

#* Write a Python program to create a decorator that logs the arguments and return value of a function.

# def my_decorator(func):
#     def wrapper(*args, **kwargs):
#         print(f"calling {func.__name__} with args: {args}, kwargs: {kwargs}")
#         result = func(*args, **kwargs)
#         print(f'{func.__name__} returned: {result}')
#         return result 
#     return wrapper

# @my_decorator
# def multiply_numbers(x,y):
#     return x*y 

# result = multiply_numbers(19,10)
# print(result)

#*  Write a Python program to create a decorator function to measure the execution time of a function.

# import time 
# def decorator(func):
#     def counter(*args, **kwargs):
#         print("Starting time .......")
#         start = time.time()
#         result = func()
#         end = time.time()
#         print("End time .......")
#         return end-start 
#     return counter 

# @decorator
# def my():
#     t = 1 
#     for i in range(10000):
#         t *= i 
#     return t

# print(my())

#* Write a Python program to create a decorator to convert the return value of a function to a specified data type. 

# def decorator(func):
#     def inner(*args, **kwargs):
#         result = func(*args, **kwargs)
#         return str(result)
#     return inner 

# @decorator
# def my(n):
#     return n 

# n = int(input("Enter: "))
# print(type(my(n)))