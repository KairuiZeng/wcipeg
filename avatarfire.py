total, doable = input().split()
total = int(total)
doable = int(doable)

leaflist = []

leafline = input()
holder = ''
for x in range(len(leafline)):
    if leafline[x] == ' ':
        leaflist.append(int(holder))
        holder = ''
    else:
        holder += leafline[x]
        
leaflist.append(int(holder))

leaflist.sort()

if total <= doable:
    print(leaflist[0] * 2)
else:
    if (leaflist[0] * 2) < leaflist[doable]:
        print(leaflist[0] * 2)
    else:
        print(leaflist[doable])
