scenarios = int(input())
for x in range(scenarios):
    pilesize = int(input())
    pile1 = input()
    pile2 = input()
    finalpile = ''
    for y in range(pilesize):
        finalpile = pile1[y] + finalpile
        finalpile = pile2[y] + finalpile
    print(finalpile)
