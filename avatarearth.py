x, y = input().split()
x = int(x)
y = int(y)

x1, y1, x2, y2 = input().split()
x1 = int(x1)
x2 = int(x2)
y1 = int(y1)
y2 = int(y2)

if x1 < x and x2 > x and y1 < y and y2 > y:
    print('Yes')
else:
    print('No')
