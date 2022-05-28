def steps(init, res):
    count = 0
    if init == res:
        return 0
    while init < res:
        if res % (init * 2) == 0:
            init *= 2
        else:
            init *= 3
        count += 1
    if init == res:
        return count
    return -1
    

a, b = input().split(" ")

if a != "" and b != "" and a.isdigit() and b.isdigit():
    initial = int(a)
    res = int(b)
    if initial != 0 and res != 0 and ((initial > 0 and res > 0) or(initial < 0 and res < 0)):
        if res % 2 != 0 and res % 3 != 0 and res != initial:
            print(-1)
        else:
            print(steps(initial, res))
    else:
        print(-1)