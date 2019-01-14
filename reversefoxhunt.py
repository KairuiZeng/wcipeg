scenarios = int(input())
for x in range(scenarios):
    hwstring = input()
    height = 0 #both between 1-6
    width = 0
    for y in range(len(hwstring)):
        if hwstring[y] != ' ':
            if height = 0:
                height = hwstring[y]
            else:
                width = hwstring[y]
    list = []
    farmerpoint = [0,0]
    housepoint = [0,0]
    for y in range(height):
        line = input()
        list.insert(len(list), line)
        if searchforhouse(line) != False:
            housepoint = [y, searchforhouse(line)]
        elif searchforfarmer(line):
            farmerpoint = [y, searchforfarmer(line)]


    if farmerpoint[0] < housepoint[0]    

#---------------------------------------------------------------

def searchforhouse(line):
    for char in range(len(line)):
        if line[char] == 'H':
            return char
        else:
            return False

def searchforfarmer(line):
    for char in range(len(line)):
        if line[char] == 'F':
            return char
        else:
            return False
    
