moves = int(input())
curtruck = [0, 0]   #[N+, W+]
newtruck = [0, 0]
rest = 5
count = 0
returned = False

while moves != 0:
    direction, time, speed = input().split()
    if direction == '3':
        direction = 'E'
    elif direction == '6':
        direction = 'S'
    elif direction == '9':
        direction = 'W'
    else:
        direction = 'N'
    time = int(time)
    speed = int(speed)
    
    while time != 0:
        if rest == 0:
            count += 1
            rest = 5
        
        if direction == 'N':
            newtruck = [curtruck[0] + speed, curtruck[1]]
        elif direction == 'S':
            newtruck = [curtruck[0] - speed, curtruck[1]]
        elif direction == 'W':
            newtruck = [curtruck[0], curtruck[1]+speed]
        elif direction == 'E':
            newtruck = [curtruck[0], curtruck[1]-speed]

        if newtruck == [0, 0]:
            returned = True
        elif (direction == 'N' or direction == 'S') and curtruck[1] == 0:
            if newtruck[0] > 0 and curtruck[0] < 0:
                returned = True
            elif newtruck[0] < 0 and curtruck[0] > 0:
                returned = True
        elif (direction == 'W' or direction == 'E') and curtruck[0] == 0:
            if newtruck[1] > 0 and curtruck[1] < 0:
                returned = True
            elif newtruck[1] < 0 and curtruck[1] > 0:
                returned = True

        curtruck = newtruck

        if not(returned):
            rest -= 1
        time -= 1

    moves -=1
    
if returned:
    print(count)
else:
    print(-1)
    
