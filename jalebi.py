n = int(input("Enter Number:- "))
arr = [[0]*n for i in range(n)]

values = 1

aaa, bbb = 0, 0
fl, bl = n, 0

for i in range(0, n):

    aaa = i
    bbb = i   

    #* ====== LOOP ONE forward of b ======= 
    while bbb < fl:
        arr[aaa][bbb] = values
        values += 1
        bbb += 1
    #* ====== LOOP TWO forward of a ======= 
    bbb = bbb-1
    aaa = aaa + 1
    while aaa < fl:
        arr[aaa][bbb] = values
        values += 1
        aaa += 1
    fl-=1
    #* ========= LOOP THREE backward of b ========
    aaa = aaa-1 
    bbb = bbb-1
    while bbb >= bl:
        arr[aaa][bbb] = values 
        values += 1 
        bbb -= 1
    bl += 1
    #* ========= LOOP FOUR backward of a ======== 
    bbb = bbb+1 
    aaa = aaa-1
    while aaa >= bl:
        arr[aaa][bbb] = values
        values += 1
        aaa -= 1

    if i == (n//2):
        break

for i in range(len(arr)):
    print(arr[i])