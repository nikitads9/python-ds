import math
n = int(input())
grades = []
for i in range (n):
    num = int(input())
    grades.append(num)
flag = True
for i in grades:
    if i % 2 != 0:
        if flag == True:
            i = math.ceil(i/2)
            flag = False
        else:
            i = math.floor(i/2)
            flag = True
    else:
        i = int(i / 2)
    print(i)

    

