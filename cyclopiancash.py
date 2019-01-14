sizes = int(input())
sizelist = []
for x in range(sizes):
    asize = int(input())
    sizelist.insert(0, asize)

sizelist.sort()


if sizes % 2 == 0:
    median = (sizelist[sizes//2]+sizelist[sizes//2-1])/2
else:
    median = sizelist[sizes//2]/1

print(median)
