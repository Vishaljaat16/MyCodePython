# f = open('data.txt', "r")
# print(f.name)
# print(f.mode)
# print(f.read())

# with open('data.txt', 'w') as f:
#     f.write("Hello Python ke chahne walo!\n")
#     f.write("Today you have to learn File Handling")
#     print(f)
# print("Done 👌")

# f = open('data.txt','r')
# print()
# print(f)

# try:
#     file = open("data.txt", "r")
#     content = file.read()
#     print(content)
# except FileNotFoundError as e:
#     print("Error:", e)
# finally:
#     file.close()

import os 
# directory = os.listdir('D:/')  #* It returns the list 
# osdir = os.scandir("D:/")  #* It returns iterator object 
# print(directory)
# print(osdir)

print(list(map(x+y, 10)))

