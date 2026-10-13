# n = int(input("Enter number :"))

#^ --- Square stars pattern ---- 
# for i in range(n):
#     print("* " * n)

# for i in range(1,n+1):
#     print(f"{i} "* n)

# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(i, end=" ")
#     print()

# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(j, end=" ")
#     print()

# for i in range(1, n+1):
#     print(f"{chr(64+i)} "*n)

# for i in range(1, n+1):
#     for j in range(1, n+1):
#         print(chr(64+i), end=" ")
#     print()

# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(chr(64+j), end=" ")
#     print()

# for i in range(1,n+1):
#     print(f"{(n+1)-i} "*n)

# for i in range(1, n+1):
#     for j in range(1,n+1):
#         print(f"{(n+1)-j} ", end=" ")
#     print()


# s = {1,2,3}
# a = {1,2,3,4,5,6,}
# print(s<=a)
# print(s<a)
# print(s>=a)
# print(s>a)


# import sys

# a = 10
# b = 10 ** 100
# c = 10 ** 1000
# d = 10 ** 10000

# print(sys.getsizeof(a))
# print(sys.getsizeof(b))
# print(sys.getsizeof(c))
# print(sys.getsizeof(d))

l = [1,2,3]
l.insert(20, 20)
print(l)
print(l[3])