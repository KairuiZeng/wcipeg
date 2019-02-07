rows, columns = input().split()
rows = int(rows)
columns = int(columns)
spreadsheet = []

for rows in range(rows):
    createnum = ''
    x = 0
    arow = []
    anum = input()
    while x < len(anum):
        if anum[x] != ' ':
            createnum += anum[x]
        else:
            arow.append(int(createnum))
            createnum = ''
        x += 1
    arow.append(int(createnum))
    
    spreadsheet.append(arow)
        
#----------------------------------------------------------


sorts = int(input())
for sorts in range(sorts):
    newsheet = []
    sorttable = []
    columnsort = int(input()) - 1
    for get in range(len(spreadsheet)):
        sorttable.append(spreadsheet[get][columnsort])
    sorttable.sort()
    
    while sorttable != []:
        x = 0
        while x < len(spreadsheet):
            if spreadsheet[x][columnsort] == sorttable[0]:
                newsheet.append(spreadsheet[x])
                del spreadsheet[x]
                del sorttable[0]
                x = len(spreadsheet)
            x += 1

    spreadsheet = newsheet
    
for x in range(len(spreadsheet)):

    answer = ''
    
    for y in range(len(spreadsheet[x])):
        if y == len(spreadsheet[x])-1:
            answer += str(spreadsheet[x][y])
        else:
            answer += str(spreadsheet[x][y]) + ' '
    print(answer)


            
