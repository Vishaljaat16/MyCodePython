# import __main__
name = "Pythonista"
# print(dir())

# print(__main__.__dict__)

#* Checking globals, locals and dir() -> returns scoped variable

# def func():
#     b = 10
#     print(locals())
#     print(globals())
#     print(dir())
#     print(name) 
# func()

# def square(base):
#     result = base ** 2
#     print(dir())
#     print(vars())
#     print(locals())
#     return result 
# print(square(10))
# print(square)   #* NameError: name "result" is not defined 

# print(square.__code__.co_argcount)
# print(square.__code__.co_varnames)

#* ======= ENCLOSING VARIABLES ========== 

# def outer_func():
#     variable = 100
#     def inner_func():
#         print(f"Printing variable in inner function {variable}")
#     inner_func()
#     print(f"Printing variable in outer function {variable}")

# outer_func()


# def outer_func():
#     variable = 100
#     def inner_func():
#         print(f"Printing variable in inner function {variable}")
#     # inner_func()
#     print(f"Printing variable in outer function {variable}")
#     return inner_func 

# v = outer_func()
# v()

# def outer_func():
#     variable = 100 

#     def inner_func():
#         print(f"Variable from inner function {variable}")
#         # print(f"another_var from inner function {another_var}") #* gives NameError 

#     inner_func()
#     another_var = 111 
#     print(f"variable from outer function {variable}")
#     print(f"another_var from outer function {another_var}")

# outer_func()

# print(__name__)


#* Global Scope variables 

# number = 42 
# def get_number():
#     return number 

# print(f"outerside = {number}")

# number = 42 

# def num():
#     number = 22
#     return number 
# print(number)
# print(num())

# import builtins 
# del abs
# print(dir(builtins))

# a = 10
# b = 11
# c = 22


#* ======== Global keywords in Python ================

# counter = 0 
# def update_counter():
#     global counter 
#     counter += 1

# print(counter) 
# update_counter()
# print(counter)
# update_counter()
# print(counter)
# update_counter()
# print(counter)


# def create_lazy_name():
#     global number
#     number = 100 
#     return number 

# create_lazy_name()

# print('number' in dir())


#* ========== nonLocal variables ======== 

# def function():
#     number = 42 
#     def inner_func():
        # nonlocal number #& For updating inside nested function 
#         number += 100
#         return number
#     inner_func()
#     print(inner_func())
#     print(number)
#     # return inner_func()

# function()

# def function():
#     number = 42 
#     def inner_func():
#         number = 100
#         return number
#     inner_func()
#     print(inner_func())
#     print(number)

# function()


# number = 42
# def function():
#     number = 42 
#     def inner_func():
#         nonlocal number 
#         number += 111
#         print(number)
#     inner_func()
#     print(number)

# function()

#& ---- nonlocal keyword only access variables inside the function but outside the current function means it only work in nested function ``` It can't deal with global variable ``` 

#* ===== Closer in function ===== 
# def power_factory(exponent):
#     def power(base):
#         return base ** exponent 
#     return power 

# square = power_factory(3)
# print(square(10))


# for items in range(5):
#     pass 

# print(items)


#* ======= variables in exception ========= 

# number = [1,2,3]
# exception = None 

# try:
#     number[4]
# except IndexError as error:
#     exception = error 
#     error 

# print(exception)

# class A:
#     attr = 100 
#     print(attr)
# print(A.__dict__.keys())
# print(A.attr)


#* ========== Namespace =========

class Mobile:
        fb = 'Yes'

        @classmethod
        def is_fb(cls):
                print("finger Print : ", cls.fb)

realme = Mobile()
oppo = Mobile()
redmi = Mobile()

print(f"Class fb: {Mobile.fb}")
print(f"realme fb: {realme.fb}")
print(f"oppo fb: {oppo.fb}")
print(f"redmi fb: {redmi.fb}")

print()
Mobile.fb = "No"
print(f"Class fb: {Mobile.fb}")
print(f"realme fb: {realme.fb}")
print(f"oppo fb: {oppo.fb}")
print(f"redmi fb: {redmi.fb}")

print()
realme.fb = "WoW"
print(f"Class fb: {Mobile.fb}")
print(f"realme fb: {realme.fb}")
print(f"oppo fb: {oppo.fb}")
print(f"redmi fb: {redmi.fb}")