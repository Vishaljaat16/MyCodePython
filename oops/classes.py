# class Dog:

#     tricks = []

#     def __init__(self, name):
#         self.name = name 

#     def add_trick(self, trick):
#         self.tricks.append(trick)

# d = Dog("Pullover")
# d = Dog("Jonny")
# d.add_trick("Pitbull")
# d.add_trick("jarman") 
# print(d.tricks)


# class Dog:

#     def __init__(self, name):
#         self.name = name
#         self.tricks = []
    
#     def add_tricks(self, trick):
#         self.tricks.append(trick) 
    
# d = Dog("Jarman")
# d.add_tricks('Long Jumps')

# print(d.tricks)

# print(globals())

# class Mapping:
#     def __init__(self, iterable):
#         self.items_list = []
#         self.__update(iterable)

#     def update(self, iterable):
#         for item in iterable:
#             self.items_list.append(item)

#     __update = update   # private copy of original update() method

# class MappingSubclass(Mapping):

#     def update(self, keys, values):
#         # provides new signature for update()
#         # but does not break __init__()
#         for item in zip(keys, values):
#             self.items_list.append(item)

# i = [1,2,3,4,5,6]
# m = MappingSubclass(i)
# print(m.items_list) 


# from dataclasses import dataclass 

# @dataclass
# class data:

#     name: str 
#     dept: str 
#     salary: int 

# d = data('Vishal', 'Python Developer', 10000)

# print(d.name)
# print(d.dept)
# print(d.salary)


#** ===== Classes By Durga Sir ============  

# class Student:
#     """ This is Student class with required data""" 

# print(Student.__doc__) 

# class Student:

#     def __init__(self, x, y, z):
#         self.name = x
#         self.rollno = y
#         self.marks = z

#     def display(self):
#         print("Student Name: {}\nStudent Rollno: {}\nStudent marks: {}".format(self.name, self.rollno, self.marks))

# s1 = Student("vishal", 101, 89)
# s2 = Student("Rahul", 102, 90)
# s1.display()
# print()
# s2.display()

#* ===================================================================== 
# class Student:

#     a = 10

#     def __init__(self):
#         Student.b = 11 
    
#     def m1(self):
#         Student.c = 12 

#     @classmethod
#     def clsm2(cls):
#         cls.d = 13 
#         Student.e = 14

#     @staticmethod
#     def m4():
#         Student.f = 15 
    
#     def display(self):
#         print(f"variable a = {Student.a}")
#         print(f"variable b = {Student.b}")
#         print(f"variable c = {Student.c}")
#         print(f"variable d = {Student.d}")
#         print(f"variable e = {Student.e}")
#         print(f"variable f = {Student.f}")

# s = Student()
# s.m1()
# s.clsm2()
# s.m4()
# s.display()


#* ===============================================================
# ====== Getter and Setter method =====

# class Label:
#     __name11 = "Rupesh"
#     def __init__(self, text, font):
#         self.name = "Vishal"
#         self._text = text 
#         self._font = font 

#     def get_text(self):
#         return self._text 
    
#     def set_text(self, value):
#         self._text = value 
    
#     def get_font(self):
#         return self._font 
    
#     def set_font(self, value):
#         self._font = value 
    
# l = Label("Hello", "Cursue") 

# print(l.get_text())
# print(l.get_font())

# print(l._text)


# from datetime import date

# class Employee:
#     def __init__(self, name, birth_date):
#         self.name = name 
#         self.birth_date = birth_date 

#     @property
#     def name(self):
#         return self.__name 
    
#     @name.setter
#     def name(self, value):
#         self.__name = value.upper()

#     @property
#     def birth_date(self):
#         return self.__birth_date 
    
#     @birth_date.setter 
#     def birth_date(self, value):
#         self.__birth_date = date.fromisoformat(value)


# e = Employee("Ravi", "2003-09-16")
# e.name = "Vishal"
# print(e.name)
# print(e.birth_date) 

#* ================================================================= 
#& ----------- property()  method ---------------------------------

# class Circle:
#     def __init__(self, radius):
#         self._radius = radius 
    
#     def _get_radius(self):
#         print("Get radius")
#         return self._radius 
    
#     def _set_radius(self, value):
#         print("Set radius")
#         self._radius = value 

#     def _del_radius(self):
#         print("Delete radius")
#         del self._radius 
    
#     radius = property(
#         fget=_get_radius,
#         fset=_set_radius,
#         fdel=_del_radius,
#         doc="The radius property"
#     )


#* =======================================================

# class Student:
#     pass 

# s = Student()
# s.name = "Vishal" 
# s.age = 23 
# print(f"Name {s.name}\nAge {s.age}")

#* ======================================================

# class BankAccount:
    
#     def __init__(self, balance):
#         self.__balance = balance 
    
#     def deposit(self, amount):
#         self.__balance += amount 
    
#     def get_balance(self):
#         return self.__balance 


# account = BankAccount(1000)
# account.deposit(500)
# print(account.get_balance())

#*==========================================================


# class Student:
    
#     def __init__(self):
#         self.name = "Vishal"
#         self._marks = 88
#         self.__grade = "A"

# s = Student()
# print(s.name)
# print(s._marks)
# print(s.__grade)
# print(s._Student__grade) #* this is a name mangling in python 

#* ========================================================

# class Student:

#     def __init__(self, marks):
#         self.__marks = marks 
    
#     def get_marks(self):
#         return self.__marks 
    
#     def set_marks(self, value):
#         if value >= 0:
#             self.__marks = value 
#         else:
#             print("Marks cannot be negative")


# s = Student(88)
# print(s.get_marks())
# s.set_marks(-100)
# print(s.get_marks())

#* ============================================================= 
#& --------------- @property ----------------- 

class Student:

    def __init__(self, marks):
        self._marks = marks 

    @property
    def marks(self):
        return self._marks 
    
    @marks.setter
    def marks(self, value):
        if value >= 0:
            self._marks = value 
        else:
            print("Marks cann't be negative") 

s = Student(88)
print(s.marks)
s.marks = 100 
print(s.marks)