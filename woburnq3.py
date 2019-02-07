z = int(input())
table = []
row = []
for rows in range(z):
    placeholder = ''
    arow = input()
    for digit in arow:
        if digit == ' ':
            row.append(int(placeholder))
            placeholder = ''
        else:
            placeholder += digit
    row.append(int(placeholder))
    table.append(row)
    row = []


sum = 0
computes = int(input())
for computing in range(computes):
    x, y = input().split()
    
    for num in table[int(x)-1]:
        sum += num
    for row in table:
        sum += row[int(y)-1]
    print(sum)
    sum = 0
