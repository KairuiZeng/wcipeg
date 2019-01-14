setnum = int(input())
for x in range(setnum):
    y = 0
    numholder = ''
    dataset = input()
    while dataset[y] != ' ':
        numholder += dataset[y]
        y += 1
    if int(numholder) < 1:
        newword = dataset[2:]
    else:
        remove = int(numholder) - 1
        word = dataset[1+y:]
        newword = word[:remove] + word[remove+1:]
    numtoprint = x + 1
    finalprint = str(numtoprint) + ' ' + newword
    print(finalprint)
