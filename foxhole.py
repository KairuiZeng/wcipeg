scenarios = int(input())
answers = []
for scenarios in range(scenarios):
    height, width, moves = input().split()
    height = int(height)
    width = int(width)
    moves = int(moves)

    fox = [0, 0]
    treasures = 0
    level = []
    for x in range(width):
        level.insert(0, 'A') 
        
    foxhole = [level]
    for x in range(height):
        level = []
        current = input()
        for x in range(width):
            level.insert(len(level), current[x])
        foxhole.insert(len(foxhole), level)

        
    for moves in range(moves):
        reset = []
        newfoxhole = []
        while fox[0] < height and foxhole[fox[0]+1][fox[1]] == 'E':
            fox = [fox[0]+1, fox[1]]
        
        curmove = input()
        
        if curmove == 'L':
            
            if fox[1] != 0:
                left = foxhole[fox[0]][fox[1]-1]
                validleft = [fox[0], fox[1]-1]
                
                if left == 'T':
                    treasures += 1
                    fox = validleft
                    for x in range(width):
                        if x != fox[1]:
                            reset.insert(len(reset), foxhole[fox[0]][x])
                        else: reset.insert(len(reset), 'E')
                    for x in range(height+1):
                        if x != fox[0]:
                            newfoxhole.insert(len(newfoxhole), foxhole[x])
                        else:
                            newfoxhole.insert(len(newfoxhole), reset)
                    foxhole = newfoxhole
                elif left != 'S':
                    fox = validleft

        elif curmove == 'R':

            if fox[1] < width -1:
                right = foxhole[fox[0]][fox[1]+1]
                validright = [fox[0], fox[1]+1]

                if right == 'T':
                    treasures += 1
                    fox = validright
                    for x in range(width):
                        if x != fox[1]:
                            reset.insert(len(reset), foxhole[fox[0]][x])
                        else: reset.insert(len(reset), 'E')
                    for x in range(height+1):
                        if x != fox[0]:
                            newfoxhole.insert(len(newfoxhole), foxhole[x])
                        else:
                            newfoxhole.insert(len(newfoxhole), reset)
                    foxhole = newfoxhole
                elif right != 'S':
                    fox = validright

        else:

            if fox[0] < height:
                down = foxhole[fox[0]+1][fox[1]]
                validdown = [fox[0]+1, fox[1]]

                if down == 'T':
                    treasures += 1
                    fox = validdown
                    for x in range(width):
                        if x != fox[1]:
                            reset.insert(len(reset), foxhole[fox[0]][x])
                        else: reset.insert(len(reset), 'E')
                    for x in range(height+1):
                        if x != fox[0]:
                            newfoxhole.insert(len(newfoxhole), foxhole[x])
                        else:
                            newfoxhole.insert(len(newfoxhole), reset)
                    foxhole = newfoxhole
                    
                elif down != 'S':
                    fox = validdown
                    
    print(treasures)
