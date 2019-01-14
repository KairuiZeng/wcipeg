guynum = int(input())
for x in range(guynum):
    picnum = int(input())
    picline = input()
    count = 0
    makenum = ''
    listofnum = []
    while count < len(picline):
        if picline[count] == ' ':
            listofnum.insert(0, int(makenum))
            makenum = ''
        else:
            makenum += picline[count]
        count+=1
    listofnum.insert(0, int(makenum))
    listofnum.sort()
    print(str(listofnum[0]) + ' ' + str(listofnum[-1]))
