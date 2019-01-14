testcases = int(input())
while testcases != 0:
    value = int(input())
    if value % 10 >= 2:
        value = ((value // 10) * 10) + 12
    else:
        value = ((value // 10) * 10) + 2
    while (value**3) % 1000 != 888:
        value += 10
    print(value)
    testcases -= 1

    
