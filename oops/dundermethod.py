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