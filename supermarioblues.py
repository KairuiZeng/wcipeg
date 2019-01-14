gettogs = int(input())
for x in range(gettogs):
    currentlvl = input()
    level = [int(currentlvl[0]), int(currentlvl[2])]
    count = 1
    while level != [8, 4]:
        if level == [1, 2]:
            count += 1
            level = [4, 1]
        elif level == [4, 2]:
            count += 1
            level = [8, 1]
        elif level[1] == 4:
            count += 1
            level = [level[0] + 1, 1]
        else:
            count += 1
            level = [level[0], level[1] + 1]
    print(count)
        
