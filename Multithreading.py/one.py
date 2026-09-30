import threading

# print("Current Executing Thread:",threading.current_thread().getName())

# *=============================================================
# ^ -------- creating a thread without using any CLASS ---------

# def display():
#     for i in range(1,11):
#         print("Child Thread")

# t = threading.Thread(target=display)
# t.start()

# for i in range(1,11):
#     print("Main Thread")


# *=========================================================
# ^ ---- Creating a Thread by extending Thread Class ----

# class MyThread(threading.Thread):
#     def run(self):
#         for i in range(10):
#             print("Child Thread-1")

# t = MyThread()
# t.start()
# for i in range(10):
#     print("Main Thread-2")


# *===========================================================
# ^ --- Creating a Thread without extending Thread Class ----

# class Test:
#     def display(self):
#         for i in range(10):
#             print("Child Thread-2")

# obj = Test()
# t = threading.Thread(target=obj.display)
# t.start()

# for i in range(10):
#     print("Main Thread-2")

import time

# def doubles(numbers):
#     for n in numbers:
#         time.sleep(1)
#         print("Double:", 2*n)
# def squares(numbers):
#     for n in numbers:
#         time.sleep(1)
#         print("Square:",n*n)

# numbers = [1,2,3,4,5,6,7]

# begintime = time.time()
# doubles(numbers)
# squares(numbers)
# print("The Total time taken:", time.time()-begintime)

# ^ ---- with Thread

# def doubles(numbers):
#     for n in numbers:
#         time.sleep(1)
#         print("Double:", 2*n)
# def squares(numbers):
#     for n in numbers:
#         time.sleep(1)
#         print("Square:",n*n)

# numbers = [1,2,3,4,5,6,7]

# begintime = time.time()
# t1 = threading.Thread(target=doubles, args=(numbers,))
# t2 = threading.Thread(target=squares, args=(numbers,))

# print("The Total time taken:", time.time()-begintime)


# *=========================================================
# ^ ------- Setting and Getting Name of a Thread -----------

# print(threading.current_thread().getName())
# threading.current_thread().setName("Vishal Jaat")
# print(threading.current_thread().getName())
# print(threading.current_thread().name)


# *========================================================
# ^------- Thread Identification Number (ident) -------

# def test():
#     print("Child Thread")

# t = threading.Thread(target=test)
# t.start()
# print("Main Thread identification Number:", threading.current_thread().ident)
# print("Child Thread identification Number:",t.ident)

# *==========================================================
# ^ ------ active_count() ------

# import time
# def display():
#     print(threading.current_thread().getName(), "....Started")
#     time.sleep(3)
#     print(threading.current_thread().getName(), "....ended")
# print("The Number of active Threads:", threading.active_count())

# t1 = threading.Thread(target=display, name="ChildThread1")
# t2 = threading.Thread(target=display, name="ChildThread2")
# t3 = threading.Thread(target=display, name="ChildThread3")

# t1.start()
# t2.start()
# t3.start()

# print("Thre Number of active Threads: ", threading.active_count())
# time.sleep(5)
# print("Thre Number of active Threads: ", threading.active_count())


# *======================================================
# ^ ----- enumerate() -------

import time
def display():
    print(threading.current_thread().getName(),"...started")
    time.sleep(3)
    print(threading.current_thread().getName(),"...ended")

t1 = threading.Thread(target=display, name="ChildThread11")
t2 = threading.Thread(target=display, name="ChildThread22")
t3 = threading.Thread(target=display, name="ChildThread33")

t1.start()
t2.start()
t3.start()
l = threading.enumerate()
for t in l:
    print("Thread Name:",t.name)
time.sleep(5)
l = threading.enumerate()
for t in l:
    print("Thread Name:",t.name)


# *===========================================================
# ^ ----------   isAlive() ---------------

# from threading import *
# import time

# def display():
#     print(current_thread().getName(), "...started")
#     time.sleep(3)
#     print(current_thread().getName(), "...ended")
# t1 = Thread(target=display, name="ChildThread1")
# t2 = Thread(target=display, name="ChildThread2")
# t1.start()
# t2.start()

# print(t1.name, "is Alive :", t1.is_alive())
# print(t2.name, "is Alive :", t2.is_alive())
# time.sleep(5)
# print(t1.name, "is Alive :", t1.is_alive())
# print(t2.name, "is Alive :", t2.is_alive())


#todo:-> A or B "If A is truthy, give me A. Otherwise, give me B." 
#todo:-> A and B "If A is falsy, give me A. Otherwise, give me B."
#*======================================================
#^ -------- join() ------  

# import time
# def display():
#     for i in range(10):
#         print("Seetha Thread")
#         time.sleep(2)

# t = threading.Thread(target=display)
# t.start()
# t.join(2)
# t.join()
# for i in range(10):
#     print("Rama Thread")

#* ========================================================
#^ -------- 
