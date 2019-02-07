cases = int(input())

for cases in range(cases):
    if cases != 0:
        wastestring = input()
    grid = []
    for x in range(4):
        grid.append(input())


    #check rows
    valid = False
    
    for x in range(4):
        if grid[x] == 'XXXX':
            valid = True

    if valid:
        print('Yes')
        continue

    for x in range(4):
        valid = True
        for columns in range(4):
            if grid[columns][x] != 'X':
                valid = False
        if valid:
            break
    if valid:
        print('Yes')
        continue

    valid = True
    for x in range(4):
        if grid[x][x] != 'X':
            valid = False

    if valid:
        print('Yes')
        continue

    valid = True
    for x in range(4):
        if grid[x][3-x] != 'X':
            valid = False
    if valid:
        print('Yes')
        continue
    
    print('No')
            
            
    
