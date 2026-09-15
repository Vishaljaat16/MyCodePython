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

# import os 
# directory = os.listdir('D:/')  #* It returns the list 
# osdir = os.scandir("D:/")  #* It returns iterator object 
# print(directory)
# print(osdir)



# ^ =========== STARTING MY FILE-HANDLING CONCEPT ========== 
#* 1)--> r --  open an existing file for read operation. The file pointer is positioned at the beginning of the file.If the specified file does not exist then we will get FileNotFoundError.This is default mode.
#* 2)--> w --  open an existing file for write operation. If the file already contains some datathen it will be overridden. If the specified file is not already avaialble then this mode will create that file.
#* 3)--> a --  open an existing file for append operation. It won't override existing data.If the specified file is not already avaialble then this mode will create a new file.

#* 5)--> w+ --  To write and read data. It will override existing data.

#* 7)--> x --  To open a file in exclusive creation mode for write operation. If the file already exists then we will get FileExistsError.

# f = open('data.txt', 'a') 
# f.write("\nHello Public!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

# f = open('data.txt', 'r+')
# first = f.read()
# f.write("!!!!!!!!!!!!!!!!!!!!!")
# print(f.tell())
# second = f.read() 
# print("our fist data : " , first)
# print(f"SEcond data : {second}")

#* 4)--> r+ --  To read and write data into the file. The previous data in the file will not be deleted.The file pointer is placed at the beginning of the file.

# with open('data.txt', "r+") as f:
#     f.write('Hello My Name is Vishal Jaat')
#     print(f.tell())
#     print(f.read())

#* 6)--> a+ --  To append and read data from the file.It wont override existing data.

# with open("data.txt", "a+") as f:
#     f.write("I am appending the data to the end ")
#     f.seek(0)
#     print(f.read())

#^ f.writelines() 
# f = open('data.txt', 'a+')
# l = ["Hello ", "108 bar Hello "]
# f.writelines(l)
# f.writelines(" ROM ROM bhaiyoo")

#^ f.read(), f.read(10), f.readline(), f.readlines()
# with open("data.txt", 'r') as f:
    # print(f.read())
    # print(f.read(10))
    # print(f.readline())
    # print(f.readlines())

# import os 
# print(os.path.isfile('data.txt'))

#* Program to print the Number of Lines, Words and Characters present in the given File? 

import os, sys 
filename = input("Enter file name :- ")

if os.path.isfile(filename):
    print("file exist: ", filename)
    f = open(filename, 'r')
else:
    print("file doesn't : ", filename)
    sys.exit(0)

lcount = wcount = ccount = 0 

for line in f:
    lcount += 1
    ccount += len(line)
    wcount += len(line.split(" "))

print(f"lcount = {lcount}")
print(f"ccount = {ccount}") 
print(f"wcount = {wcount}") 

