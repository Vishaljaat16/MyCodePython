#
#* ===========================================================
#& ------------- __str__() method ----------------- 

# class Student:
#     def __init__(self, name, rollno):
#         self.name = name 
#         self.rollno = rollno 
    
# s1 = Student('Durga', 101)
# s2 = Student('Ravi', 102)

# print(s1) 
# print(s2)

# class Student:
#     def __init__(self, name, rollno):
#         self.name = name 
#         self.rollno = rollno 
    
#     def __str__(self):
#         return f"This is the Students Datawith Name - {self.name} and rollno - {self.rollno}"
    
# s1 = Student('Durga', 101)
# s2 = Student('Ravi', 102)

# print(s1) 
# print(s2) 


#* ======================================================== 
#&----------------- __new()__ method ----------------- 

# class A:
#     def __init__(self):
#         print("Initializing instance")

#     def __new__(cls):
#         print("Creating Instance")
#         return super().__new__(cls)
    
# A()
# print(A())

# class A:
#     def __new__(cls):
#         print("Creating instance")
#         return "Hello, World!"

# print(A())

# class Animal:
#     def __str__(self):
#         return "Animal Object"
    
# class Person:
#     def __new__(cls):
#         return Animal()
    
#     def __init__(self):
#         print("Inside __init__")

# print(Person())

#^ ---------- Where we use __new__() -------------
# Todo:   When to use __new__
#& ---  __new__ is rarely overridden, but it is useful in specific scenarios, such as:

#& -- Implementing Singleton Pattern:-- Ensures only one instance of a class exists.

#& -- Returning Cached Objects:-- Helps in memory optimization by reusing existing objects instead of creating new ones.

#& -- Immutable Object Creation:-- Used in classes like str and tuple since they are immutable.

#& -- Subclassing Immutable Types:-- When extending built-in immutable types like int, float or str. 


#^  -------------- __repr()__ method ----------------- 

# class GFG:
#     def __init__(self, f_name, m_name, l_name):
#         self.f_name = f_name
#         self.m_name = m_name
#         self.l_name = l_name

#     def __repr__(self):
#         return f"GFG('{self.f_name}','{self.m_name}', '{self.l_name}')" 

# g = GFG("geeks", "for", "geeks")
# print(g)
 
#^ ------------- __repr__() vs __str__() --------------

# class Vishal:
#     def __init__(self, name):
#         self.name = name 
    
#     def __str__(self):
#         return f'Name is {self.name}'
    
#     def __repr__(self):
#         return f'GFG(name={self.name})'

# obj = Vishal("vishal")
# print(obj.__str__())  #? IT has high priority during runtime execution
# print(obj.__repr__())




#^ -------------- __hash__() ----------------- 

# print(hash(1)) 
# print(hash("Python")) 

#^ -------------- __getitem__() --------------
# class Team:
#     def __init__(self, members):
#         self.members = members 

#     def __getitem__(self, index):
#         return self.members[index]

# team = Team(['Vishal','Saurav','Rupesh','Guru'])
# print(team[0])

# print(__name__)


#^ -------------- __getattribute__() ---------------

# class Student:

#     def __init__(self):
#         self.name = "Vishal"
#         self.age = 20 
    
#     def __getattribute__(self, name):
#         print(f"Someone is accessing: {name} ")
#         return object.__getattribute__(self, name)

# s = Student()
# s.name = "Vishal"
# s.age = 23

# print(s.name)
# print(s.age)

# class Student:
#     def __getattribute__(self, name):
#         print("Some Accessing the Name attribute")
#         # return self.name 
#         return object.__getattribute__(self,name)

# s = Student()
# s.name = "Vishal"
# print(s.name)

#* ==================================================================================
#^ ----------------------- __getattr__() -------------------------------- 

# class Student:
#     def __getattr__(self, name):
#         return f"{name} attribute doesn't exist in the object"
        
# s = Student()
# print(s.name)
# s.name = "Vishal"
# print(s.name)

# class Student:
    
#     name = "Vishal"

#     def __getattribute__(self, name):
#         print(f"GATEATTRIBUTE -> {name}")
#         return object.__getattribute__(self, name)

#     def __getattr__(self, name):
#         print(f"GETATTR -> {name}")
#         return "Default Value"

# s = Student()
# print(s.name)
# print(s.age)


#* ===================================================================================
#^ ---------------------- __setattr__() -------------------------- 

# class Student:
#     def __setattr__(self, name, value):
#         print(f"setting {name} = {value}")
#         object.__setattr__(self, name, value) 

# s = Student()
# s.name = "vishal"
# s.age = 23

# class Student:
#     def __setattr__(self, name, value):
#         if name == "age" and value <= 0:
#             raise ValueError("Age cannot be negative")
#         object.__setattr__(self, name, value) 

# s = Student()
# s.name = "Vishal"
# print(s.name)
# s.age = 111
# print(s.age)



#* ===================================================================================
#^ ------------------------ __slots__() ---------------------  

# class Employee:

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age 

# e = Employee("vishal", 22)
# e.dept = 'AI'
# print(e.name)
# print(e.age)
# print(e.dept)
# print()

# class Employee2:

#     __slots__ = ('name','age',)

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# e2 = Employee2('Rahul', 32)
# print(e2.name)
# print(e2.age)
# e2.dept = "Mechanical"
# e2.name = "Ravi"
# print(e2.name)
# print(e2.dept)

#* =====================================================================================
#^ -------------------------- Context Manager ------------------------------------

# class Demo:
#     def __enter__(self):
#         print("=============================")
#         print("Entering to the file")
    
#     def __exit__(self, exc_type, exc_value, traceback):
#         print("Leaving the file")
#         print("===============================")

# with Demo():
#     print()
#     print("Inside the context")
#     print()

# class Demo:
#     def __enter__(self):
#         print("Enter")

#     def __exit__(self, exc_type, exc_value, traceback):
#         print("Exit")
#         print("Exception Type : ", exc_type)
#         print("Exception value : ", exc_value)

# with Demo():
#     print("Before Error")
#     x = 10/0
#     print("After Error")

print(any([]))
print(all([]))