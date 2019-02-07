sizes = int(input())
curmax = 0
count = 0
sizelist = []
x = 0
maxholder = []


for sizes in range(sizes):
    sizelist.append(int(input()))

sizelist.sort()

holder = sizelist[0]

while x < len(sizelist):
    if holder == sizelist[x]:
        count += 1
        
    else:
        if curmax == 0:
            curmax = count
            maxholder = [holder]
            
        elif count > curmax:
            maxholder = [holder]
            curmax = count
        elif count == curmax:
            maxholder.append(holder)
            
        count = 1
        holder = sizelist[x]
    x += 1

if count > curmax:
    maxholdler = [holder]
elif count == curmax:
    maxholder.append(holder)

print(len(maxholder))
for x in range(len(maxholder)):
    print(maxholder[x])
        
                    
                
