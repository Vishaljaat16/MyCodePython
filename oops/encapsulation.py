class Student:

    def __init__(self, name, rollno, marks, amount):
        self.name = name
        self.rollno = rollno
        self._marks = marks
        self.__amount = amount 
    
    def display(self):
        print(f"Student name = {self.name}")
        print(f"Student Roll no = {self.rollno}")
        print(f"Student marks = {self._marks}")
        print(f"Student fees amount = {self.__amount}")

# class B(Student):
#     def __init__(self,):
#         super().__init__("Vishal", 111, 33, 22000)
    
#     def show(self):
#         print(self._marks)

# b = B()
# # b.display()
# b.show()


# s = Student("Vishal",102, 88, 11000)
# s.display()
# s._marks = 111
# print()
# s.display()
# print()
# s._Student__amount = 11111
# s.display()




