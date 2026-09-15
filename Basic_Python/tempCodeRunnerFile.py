with open('data.txt', 'w') as f:
    f.write("Hello Python ke chahne walo!\n")
    f.write("Today you have to learn File Handling")
    print(f)
print("Done 👌")

f = open('data.txt','r')
print()
print(f)