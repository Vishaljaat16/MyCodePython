# def make_alternate_pattern(given_str):

#     count_dot = given_str.count('.')
#     count_b = given_str.count('b')
#     result_needed = "Alternate Form Is Not Possible !!"

#     alternate_str = []
#     alternate_str1 = []
#     alternate_str2 = []
#     result_needed = ""
#     result_needed1 = ""
#     result_needed2 = ""

#     if count_b == 0 or count_dot == 0 or count_b > count_dot + 1:
#         return result_needed, -1
    
#     elif count_b == 1 and given_str[-1] != 'b' and given_str[-2] != 'b':
#         return ('.'*count_dot+'b'), 2
    
#     elif count_b == 1 and (given_str[-1] == 'b' or given_str[-2] == 'b'):
#         return given_str, 0
    
#     elif count_b == count_dot + 1:
#         for _ in range(count_b-1):
#             alternate_str.append('b.')
#         alternate_str.append('b')
#         result_needed1 += "".join(alternate_str)
#         result_needed2 += "".join(alternate_str)

#     elif count_b == count_dot:
#         for _ in range(count_b):
#             alternate_str1.append('b.')
#         result_needed1 += "".join(alternate_str1)

#         for _ in range(count_b):
#             alternate_str2.append('.b')
#         result_needed2 += "".join(alternate_str2)

#     elif count_b < count_dot:
#         front_dots1 = (['.'] * (count_dot-(count_b)))
#         for _ in range(count_b):
#             alternate_str1.append('b.')
#         front_dots1.extend(alternate_str1)
#         result_needed1 += "".join(front_dots1)

#         front_dots2 = (['.'] * (count_dot - count_b))
#         for _ in range(count_b):
#             alternate_str2.append('.b')
#         front_dots2.extend(alternate_str2)
#         result_needed2 += "".join(front_dots2)

#     def count_difference(given_str, result_needed1, result_needed2):
#         shift_count1 = sum(1 for a, b in zip(given_str, result_needed1) if a != b)
#         shift_count2 = sum(1 for c, d in zip(given_str, result_needed2) if c != d)
#         if shift_count1 <= shift_count2:
#             result_needed = result_needed1
#             counts = shift_count1
#         else:
#             result_needed = result_needed2
#             counts = shift_count2
#         return result_needed, counts
#     return count_difference(given_str, result_needed1, result_needed2)
# your_input = input("\nEnter Your Input String   :    ")
# your_input_clean = ''
# for i in your_input:
#     if i == '.' or i == 'b':
#         your_input_clean+=i
# final_pattern, counts = make_alternate_pattern(your_input_clean)
# print(your_input_clean)
# print(final_pattern)
# print(counts)
# print()

# def vishal(start=0, n=0, step=1):
#     return [i for i in range(start, n, step)]

#* nested list sum question using recursion 
# import numpy as np 
# l1 = [[1,2,[10,12],0],
#     [[13,14,15,[7,77,[90,50],0,[12,[12,123,[1],10]]]], 3, 4], 
#     [5,6]]
# output = [1, 2, 10, 12, 0, 13, 14, 15, 7, 77, 90, 50, 3, 4, 5, 6]

# def digrade(lst):
#     result = []

#     for item in lst:
#         if isinstance(item, list):
#             result.extend(digrade(item))
#         else:
#             result.append(item)
#     return result 

# print(digrade(l1))


#* coordination and direction question 
# person = [0,0]
# while True:
#     direction = input("Enter persons direction[up,left,down,right]: ")
#     if direction.lower() == "up":
#         person[0] += 1
#     elif direction.lower() == "down":
#         person[0] -= 1 
#     elif direction.lower() == "right":
#         person[1] += 1 
#     else:
#         person[1] -= 1 
    
#     run = input("You wanted to continue [Yes/No]: ")
#     if run.lower() == 'no':
#         break 

# distance = ((person[0]-0)**2 + (person[1]-0)**2)**0.5

# print("coordinat points of person : ",person)
# print("Distance of a person from initial point :",distance) 

#* Return a some of target  number with prime numbers 
# n = int(input("Enter range: "))
# target = int(input("Enter Target Element: "))

# def is_prime(num):
#     if num == 2:
#         return False
#     for i in range(2,num):
#         if num%i == 0:
#             return False
#     return True

# prime = [i for i in range(1,n) if is_prime(i)]
# print(prime)

# q, r = 0, len(prime)-1
# result = []
# while q < r:
#     temp = prime[q] + prime[r]
#     if temp == target:
#         result.append((prime[q], prime[r]))
#         q+=1
#     elif temp > target:
#         r -= 1
#     else:
#         q+=1

# print(result)

# students = ["Ajay", "Ravi", "Neha"]
# scores = [85, 90, 88]

# student_record = {"school": "DPS Indore"}
# records = []

# for i in range(len(students)):
#     student_record = {"school": "DPS Indore"}
#     student_record["name"] = students[i]
#     student_record["score"] = scores[i]
#     records.append(student_record)

# print(records)

#* Count zero from list without using any builtin methods 
# l = [0,1,0,1,0,1,0,-10,0,2,2,2,0,-1,]
# count = 0

# for i in l:
#     while i:   
#         break
#     else:
#         count += 1
# print(count)

#* checking hashing of the values in set and list: 

# l = [1,2,3,4,5,6]
# l1 = ['1','2','3','4','5','6']
# l2 = ['a','b','c','d','e','f']

# for i in range(len(l)):
    # if l[i] > l1[i]:
    #     print("\n",l[i], end=" ")
    # else:
    #     print("\n",l1[i], end=" ")
    # if l1[i] > l2[i]:
    #     print(l1[i], end=" ")
    # else:
    #     print(l2[i], end=" ")


#* use divmod()  python function 

# n = int(input("Enter number of days : "))

# years, rem = divmod(n, 365)

# leap, rem = divmod(years, 4) 
# years_of_days = (years - leap) * 365 + (leap * 366)
# no_of_days_left = n - years_of_days

# print(f"Years = {years-leap}")
# print(f"Leap Years = {leap}")

# if no_of_days_left > 330:
#     new_num = no_of_days_left - 330
#     month, remain = divmod(330,30)
#     remain += new_num
# else:
#     month, remain = divmod(no_of_days_left, 30)
# print(f'{month = }')

# week, remain = divmod(remain, 7)
# print(f'{week = }')

# print(f'Days = {remain}')



