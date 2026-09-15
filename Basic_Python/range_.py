def vishal(*args):
    start, step, stop = 0, 1, 0

    # == HANDLING SINGE PARAMETER AS "STOP" ==
    if len(args) == 1:
        stop = args[0]
        if stop < 1:
            return []
    # == HANDLING TWO PARAMETER AS "START & STOP" ==
    elif len(args) == 2:
        start = args[0]
        stop = args[1]
        if start > stop:
            return []
    # == HANDLING THREE PARAMETER 
    elif len(args) == 3:
        start = args[0]
        stop = args[1]
        step = args[2]

        if step < 1 and start < stop:
            return []
        elif step < 1:
            l = []
            while start > stop:
                l.append(start)
                start += step
            return l

    # == CHECKING NUMBER OF ARGUMENTS ==
    else:
        raise ValueError("Expected atmost 3 arguments")
        
    l = []
    while start < stop:
        l.append(start)
        start += step
    return l

# for i in vishal(3,10):
#     print(i, end= " ")   



def test_vishal():
    # -------------------------
    # 1. One argument
    # -------------------------
    assert list(vishal(5)) == [0, 1, 2, 3, 4]
    assert list(vishal(1)) == [0]
    assert list(vishal(0)) == []
    assert list(vishal(-5)) == []


    # -------------------------
    # 2. Two arguments
    # -------------------------
    assert list(vishal(1, 5)) == [1, 2, 3, 4]
    assert list(vishal(0, 5)) == [0, 1, 2, 3, 4]
    assert list(vishal(-5, 0)) == [-5, -4, -3, -2, -1]
    assert list(vishal(-5, 5)) == [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4]


    # -------------------------
    # 3. Two arguments - invalid direction
    # -------------------------
    assert list(vishal(5, 1)) == []
    assert list(vishal(5, -5)) == []


    # -------------------------
    # 4. Positive step
    # -------------------------
    assert list(vishal(1, 10, 1)) == [1, 2, 3, 4, 5, 6, 7, 8, 9]

    assert list(vishal(1, 10, 2)) == [1, 3, 5, 7, 9]

    assert list(vishal(0, 20, 5)) == [0, 5, 10, 15]

    assert list(vishal(-10, 10, 2)) == [
        -10, -8, -6, -4, -2, 0, 2, 4, 6, 8
    ]


    # -------------------------
    # 5. Negative step
    # -------------------------
    assert list(vishal(5, 0, -1)) == [5, 4, 3, 2, 1]

    assert list(vishal(10, 0, -2)) == [10, 8, 6, 4, 2]

    assert list(vishal(0, -10, -1)) == [
        0, -1, -2, -3, -4, -5, -6, -7, -8, -9
    ]

    assert list(vishal(5, -5, -2)) == [
        5, 3, 1, -1, -3
    ]


    # -------------------------
    # 6. Negative step but wrong direction
    # -------------------------
    assert list(vishal(1, 10, -1)) == []

    assert list(vishal(-5, 5, -1)) == []


    # -------------------------
    # 7. Start == Stop
    # -------------------------
    assert list(vishal(5, 5)) == []
    assert list(vishal(5, 5, 1)) == []
    assert list(vishal(5, 5, -1)) == []


    # -------------------------
    # 8. Step larger than range
    # -------------------------
    assert list(vishal(1, 5, 10)) == [1]

    assert list(vishal(10, 1, -10)) == [10]


    # -------------------------
    # 9. Negative values
    # -------------------------
    assert list(vishal(-1, -10, -1)) == [
        -1, -2, -3, -4, -5, -6, -7, -8, -9
    ]

    assert list(vishal(-10, -1, 2)) == [
        -10, -8, -6, -4, -2
    ]


    print("All tests passed!")


test_vishal()


# l = [1,2,3,4,5]
# s = "Vishal"
# for i in vishal(len(s)):
#     print(s[i], end=" ")