# s = "qwertyuiopasdfghjklzxcvbnm"
# l = list(s)

# i = len(l)-1
# while i >= 1:
#     j = 0
#     while j < i:
#         if l[j] > l[j+1]:
#             l[j], l[j+1] = l[j+1], l[j]
#         j += 1
#     i -= 1 
# print("".join(l))

# s = "dsdgdsfhshsffaaaaaaaddddaaaaeeaaa"
# n = int(input("Enter a num: "))
# st = input("replacement value: ")

# temp = ""
# count = 0
# for i in range(len(s)):
#     if s[i] == "a" and count != n:
#         temp += st 
#         count += 1
#     else:
#         temp += s[i]

# print(temp)


# * Circular gunshot 

# l = [int(i) for i in range(1,101)]
# temp = []
# while len(l) > 1:
#     for i in range(0,len(l),2):
#         temp.append(l[i])
#     l = temp[:]
#     print(temp)
#     temp = []
# print(l)

# l = [i for i in range(1,10)]
# i = 0
# while len(l) > 1:
#     i = (i+1) % len(l)
#     l.pop(i)

# print(l)

s = ".b.bb..b.b.b.b.bbbb...bb..."
sl = list(s)
print(s)
dot = s.count('.')
char = len(s)-dot 

if dot < (char-1):
    print(-1)

swap_count = 0

i = 0
j = len(s)-1
while i < j:
    if sl[i] != "." and sl[i+1] != ".":
        if sl[j] == "." and sl[j-1] == ".":
            sl[i+1], sl[j] = sl[j], sl[i+1]
            swap_count += 1 
            j -= 1
    i += 1

# sl.reverse()
start = 1 
end = len(sl)-1 
while start < end:
    if sl[start-1] == "." and sl[start] == "." and sl[start+1]:
        if sl[end] != ".":
            sl[start], sl[end] = sl[end], sl[start]
            swap_count += 1
            end -= 1
    start += 1

print(''.join(sl))
print(swap_count)
