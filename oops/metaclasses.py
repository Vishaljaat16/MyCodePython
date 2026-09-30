# def add(self):
#     return 10 + 29


# Test = type('Test', (), dict(x="Vishal", my_method=add))

# t = Test()
# print(type(t))

# print(t.my_method())

#* =================================================================================
#^ ------------------ Creating MetaClasses ---------------------------
 

# class Person:
#     def eat(self):
#         print("Eating YUM YUM..........")

# class CustomMeta(type):
#     def __new__(cls, name, bases, attrs):
#         print(f"Creating class : {name}")
#         print(cls)
#         print(name)
#         print(bases)
#         print(attrs)
#         print()
#         attrs['class'] = 'MCA'
#         bases = (Person,)
#         return super().__new__(cls, name, bases, attrs)

# class Student(metaclass=CustomMeta):
#     school = "Deathcode School"
#     pass

# class Graduate(Student):
#     pass

# # s = Student()
# # print(type(Student))
# # s.eat()

# Graduate().eat()

#
#& ====================================================
#^ ------- Singleton Meta class -------------------- 
# Todo:->  Creating for only one object for the perticular class

# class SingletonMeta(type):
#     _instances = {}
#     def __call__(cls, *args, **kwargs):
#         if cls not in cls._instances:
#             cls._instances[cls] = super().__call__(*args, **kwargs)
#         return cls._instances[cls]

# class Database(metaclass=SingletonMeta):
#     pass 

# d1 = Database()
# print(id(d1))
# d2 = Database()
# print(id(d2))


#* ==================================================================== 
# class Meta(type):

#     def __new__(cls, name, bases, attrs):
#         attrs['greet'] = lambda self: f"Hello from {name}"
#         return super().__new__(cls, name, bases, attrs)

# class Person(metaclass=Meta):
#     def __init__(self, name):
#         self.name = name 

# p = Person("Olivia")
# print(p.greet())


#* =====================================================================================================
#^ ----------------------------- Creating Subclasses ---------------------------- 

# def init(self, ftype):
#     self.ftype = ftype

# def getFtype(self):
#     return self.ftype


# FoodType = type('FoodType', (), {
#     "__init__":init,
#     "getFtype":getFtype
# })


# def vegFoods(self):
#     return {'spinach', 'Bitter Guard'}

# VegType = type('VegType', (FoodType,), {
#     "vegFoods":vegFoods,
# })

# v = VegType("Vegetarian")
# print(v.getFtype())
# print(v.vegFoods())


#* =================================================================== 
#^ ---------------- Metaclass Inheritance --------------------------- 

# class MetaCls(type):
#     pass

# A = MetaCls('A', (object,), {})

# class B(object):
#     pass 
# class C(A,B):
#     pass

# print(type(A))
# print(type(B))
# print(type(C))



#* ==================================================================
#^ ---------------------- MetaClass Conflicts -----------------------

# class MetaCls(type):
#     pass

# A = MetaCls('A', (object,), {})
# print("Type of A: ", type(A))

# class DiffMetaCls(type):
#     pass

# B = DiffMetaCls('B', (object,), {})
# print("Type of B: ", type(B))

# class C(A, B):
#     pass 

# print("Type of C: ", type(C))