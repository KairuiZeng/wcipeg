pplnum, pairs = input().split()
pplnum = int(pplnum)
pairs = int(pairs)
sum = 0

for x in range(pplnum):
    sum += x

print(sum - pairs)
