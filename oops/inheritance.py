# class Animal:
#     def eat(self):
#         print("Eating")

# class Dog(Animal):
#     def bark(self):
#         print("the Dog is Barking ")

# d = Dog()
# d.eat()
# d.bark()

#* ============================================================
#^ ----------------- Multilevel Inheritance ------------------- 

# class A:

#     def m1(self):
#         print("I am class A")

# class B(A):

#     def m2(self):
#         print("I am class B")

# class C(B):

#     def m3(self):
#         print("I am class C")

# c = C()
# c.m1()
# c.m2()
# c.m3()


#* ======================================================== 
#^ ----------------- MRO ----------------------

# class A:
#     def show(self):
#         print("A") 

# class B(A):
#     def show(self):
#         print("B")

# class C(A):
#     def show(self):
#         print("C")

# class D(B,C):
#     pass 

# obj = D()
# obj.show()


#* =========== Composition (Has-A Relationship) ===============

#& DEMO PROGRAM 1 :--- 
# class Engine:
#     a = 10 

#     def __init__(self):
#         self.b = 20 

#     def m1(self):
#         print("Engine Specific Functionality")

# class Car:

#     def __init__(self):
#         self.engine = Engine()

#     def m2(self):
#         print("Car using Engine Class Functionality") 
#         print(self.engine.a)
#         print(self.engine.b)
#         self.engine.m1()

# c = Car() 
# c.m2()

#& DEMO PROGRAM 2 :--- 

# class Car:
#     def __init__(self, name, model, color):
#         self.name = name 
#         self.model = model 
#         self.color = color 
    
#     def getinfo(self):
#         print(f"Car Name:{self.name}, Model:{self.model} and Color:{self.color}")

# class Employee:
#     def __init__(self, ename, eno, car):
#         self.ename = ename 
#         self.eno = eno
#         self.car = car 
    
#     def empinfo(self):
#         print(f"Employee Name : {self.ename}")
#         print(f"Employee Number : {self.eno}")
#         print(f"Employee Car Info : ") 
#         self.car.getinfo()

    
# c = Car("Mustang", "1.5v", "Red") 
# e = Employee("Vishal", 302, c) 
# e.empinfo()


#* =========================================================
#& ------------------- Super() Method -------------------  
#^ DEMO PROGRAM 2 :--- 
 
# class Person:

#     def __init__(self, name, age):
#         self.name = name 
#         self.age = age 
    
#     def display(self):
#         print(f"Name {self.name}")
#         print(f"Age {self.age}")

# class Student(Person):
#     def __init__(self, name, age, rollno, marks):
#         super().__init__(name, age) 
#         self.rollno = rollno 
#         self.marks = marks

#     def display(self):
#         self.p = Person("Ravi", 28)
#         # super().display()
#         self.p.display()
#         print("Roll No", self.rollno)
#         print("Marks", self.marks) 


# s1 = Student("Vishal", 23, 77, 78)
# s1.display()

#^ DEMO PROGRAM 3 :- 
 
# class P:

#     a = 10 
#     def __init__(self):
#         self.b = 10 
    
#     def m1(self):
#         print("Parent instance method")
    
#     @classmethod
#     def m2(cls):
#         print("Parent class Method")
    
#     @staticmethod
#     def m3():
#         print("Parent static Method")


# class C(P):
#     a = 888 

#     def __init__(self):
#         self.b = 999 
#         super().__init__()
#         print(super().a)
#         super().m1()
#         super().m2()
#         super().m3()

# c = C()
# print(c.a)


#^ super() case - 3 

# class P:
#     def __init__(self):
#         print('Parent Constructor')
    
#     def m1(self):
#         print('Parent instance method')
    
#     @classmethod
#     def m2(cls):
#         print('Parent class method')
    
#     @staticmethod
#     def m3():
#         print('Parent static method') 

# p = P()
# p.m1()
# p.m2()
# p.m3()

# P.m1()   #* we can't call instance method using class name

# P.m2()
# P.m3()

# class C(P):
#     @classmethod
#     def m1(cls):
#         # super().__init__()
#         # super().m1()
#         super().m2()
#         super().m3()

# c = C()
# c.m1()

#^ another way to call constructor and instance method using super() in classmethod of child 
# 

# class A:
#     def __init__(self):
#         print('Parent construtor')
    
#     def m1(self):
#         print('Parent instance method') 

# class B(A):
#     @classmethod
#     def m2(cls):
#         super(B, cls).__init__(cls)
#         super(B, cls).m1(cls)

# B.m2() 
# b = B()
# print()
# b.m2()

