factories = int(input())

for factories in range(factories):
    sizes = int(input())
    typeline = input()
    typelist = []
    numline = input()
    numlist = []

    holder = ''
    for letter in range(len(typeline)):
        if typeline[letter] == ' ':
            typelist.append(int(holder))
            holder = ''
        else:
            holder += typeline[letter]
    typelist.append(int(holder))
    holder = ''
    
    for letter in range(len(numline)):
        if numline[letter] == ' ':
            numlist.append(int(holder))
            holder = ''
        else:
            holder += numline[letter]
    numlist.append(int(holder))

    sum = 0
    for x in range(sizes):
        sum += typelist[x] * numlist[x]

    print(sum)
