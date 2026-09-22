from abc import * 

# class Test(ABC):
    
#     @abstractmethod
#     def m1(self):
#         pass
    
#     def m2(self):
#         print("I am M2 Method")

# t = Test()
# t.m2()
# Test.m2('hello')

# class Test:

#     @abstractmethod
#     def m1(self):
#         print("hello")

# t = Test()
# t.m1()

# class Test(ABC):

#     @abstractmethod
#     def m1(self):
#         print("hello")

# class A(Test):
#     pass

# a = A()
# a.m1()


#* ==========================================================   

# class Vehicle(ABC):

#     @abstractmethod
#     def noofwwheels(self):
#         pass 

# class Bus(Vehicle):
#     def noofwwheels(self):
#         return 6 

# class Auto(Vehicle):
#     def noofwwheels(self):
#         return 3

# b = Bus()
# print(b.noofwwheels())

# a = Auto()
# print(a.noofwwheels())


#* ==============================================================
#& ------------------ INTERFACE ------------------   

# class DBinterface(ABC):
#     @abstractmethod
#     def connect(self):
#         pass 

#     @abstractmethod
#     def disconnect(self):
#         pass

# class Oracle(DBinterface):
#     def connect(self):
#         print("Connecting to Oracle Database")
    
#     def disconnect(self):
#         print("Disconnecting to Oracle Database")


# class Sybase(DBinterface):
#     def connect(self):
#         print("Connecting sybase")
    
#     def disconnect(self):
#         print("Disconnecting Sybase") 

# dbname = input("Enter Database Name: ")
# classname = globals()[dbname]
# print(globals())
# x = classname()
# x.connect()
# x.disconnect()  


# class Printer(ABC):
#     @abstractmethod
#     def printit(self, text):
#         pass 
    
#     @abstractmethod
#     def disconnect(self):
#         pass

# class EPSON(Printer):
#     def printit(self, text):
#         print("Printing from EPSON Printer............")
#         print(text) 
    
#     def disconnect(self):
#         print('Printing completed on EPSON Printer .......')
    
# class HP(Printer):
#     def printit(self, text):
#         print("Printing from HP Printer.........")
#         print(text)
    
#     def disconnect(self):
#         print("Printing from HP is COmpleted ------")

# with open('oops/config.txt', 'r') as f:
#     pname = f.readline()

# classname = globals()[pname]
# x = classname() 
# x.printit("This data has to print")
# x.disconnect


