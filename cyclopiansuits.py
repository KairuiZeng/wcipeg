sizes = int(input())

count = []
sizetable = []
common = -1

for sizes in range(sizes):
    asize = int(input())
    present = False
    for x in range(len(sizetable)):
        if asize == sizetable[x]:
            count.insert(x, count[x]+1)
            common = max(common, count[x])
            del count[x+1]
            present = True
    if not(present):
        sizetable.insert(len(sizetable), asize)
        count.insert(len(count), 0)
  
commonsize = []
for x in range(len(count)):
    if common == count[x]:
        commonsize.insert(0, sizetable[x])

commonsize.sort()
print(len(commonsize))
for x in range(len(commonsize)):
    print(commonsize[x])
