class Student:

    def __init__(self, name, age, course, marks):
        self.name = name 
        self.age = age 
        self.course = course 
        self.marks = marks 

    def display_details(self):
        print(f"My name is {self.name}")
        print(f"and i am {self.age} old")
        print(f"I am doing {self.course}")
        print(f"And I am geeting {self.marks} marks")

    def calculate_percentage(self):
        return (self.marks/100)*100

    def is_passed(self):
        if self.marks >= 35:
            return "Passed"
        else:
            return "Failed"

# s = Student("Vishal",26,'MCA',88)
# s.display_details()
# print(s.calculate_percentage())
# print(s.is_passed()) 


class Bank:

    def __init__(self, account_holder, account_number, balance=0):
        self.account_holder = account_holder
        self.account_number = account_number 
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount 
    
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount 
        else:
            print("Insufficient Balance")

    
    def check_balance(self):
        print(f"Your current account balance is : {self.balance}")

# b = Bank('Vishal',12345678, 1000)
# b.deposit(111)
# b.withdraw(1)
# b.check_balance()


#^ Only try code block using @property 
# class Bank:

#     def __init__(self, name, account, balance=0):
#         self.name = name
#         self.account = account
#         self._balance = balance 
    
#     @property
#     def deposit(self):
#         print(self._balance)

#     @deposit.setter
#     def deposit(self, amount):
#         self._balance += amount 

# b = Bank("Vishal",123456, 1000)
# b.deposit
# b.deposit = 111
# b.deposit

#* ============================================================
class BankAccount:

    def __init__(self, name, account, balance=0):
        self.name = name
        self.account = account
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount 
    
    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
        else:
            print("Insufficient Account Balance!!")
    
    def get_balance(self):
        print(self.__balance)

# ba = BankAccount('Vishal', 11221, 111111)
# ba.get_balance()
# ba.withdraw(111)
# print()
# ba.get_balance()
# print(ba._BankAccount__balance) #* Name Mangling 


#* ======================================================
#^ ---------- @property decorator ---------------- 

# class Employee:

#     def __init__(self, ename, eid, salary):
#         self.ename = ename
#         self.eid = eid
#         self.__salary = salary

#     @property
#     def salary(self):
#         print(self.__salary)
    
#     @salary.setter
#     def salary(self, amount):
#         self.__salary += amount 

# e = Employee

#* ===========================================================
