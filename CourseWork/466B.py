import math
n, a, b = input().split(" ")
num, side1, side2 = int(n), int(a), int(b)
SQ = 10e18
if side1 * side2 < num * 6:
    swap = False
    a1, b1 = 0, 0
    if side1 > side2:
        side1, side2 = side2, side1
        swap = True
    for i in range (side1, int(math.ceil((math.sqrt(6*num))))):
        var = int(6* num / i)
        if var * i < 6 * num: var+=1
        if var < side2: continue
        if var * i < SQ:
            SQ = var * i
            a1 = i
            b1 = var
    if swap:
        a1, b1 = b1, a1
    print(SQ)
    print(a1, b1)
else:
    print (side1*side2)
    print(side1, side2)

    