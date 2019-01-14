print("Ready")
x = input()
while x != '  ':
    if x.lower() == 'pq' or x == 'qp' or x == 'db' or x == 'bd':
        print('Mirrored pair')
    else:
        print('Ordinary pair')
    x = input()
