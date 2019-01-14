for scenarios in range(int(input())):
    list = []
    maxcycles = 1
    curcycle = 0

    for foxes in range(int(input())):
       a, b, c = input().split()
       a = int(a)
       b = int(b)
       c = int(c)
       list.insert(len(list), [a, b, c])
       
       refresh = a+b
       count = 1
       gcd = 0
       while count <= min(refresh, maxcycles):
            if refresh % count ==0 and maxcycles % count == 0:
               gcd = count
            count += 1
       maxcycles = maxcycles * refresh / gcd

       
    while curcycle < maxcycles and curcycle != -1:
        sleeping = True
        count = 0
        while count < len(list) and sleeping:
            awake = list[count][0]
            sleep = list[count][1]
            start = list[count][2]
            totalhours = start + curcycle
            acycle = sleep + awake
            totalhours = totalhours - (totalhours // acycle) * acycle        
            if totalhours < awake:
                sleeping = False
            count += 1
        if not(sleeping):
            curcycle+=1
        else:
            print(curcycle)
            curcycle = -1

    if curcycle == maxcycles:
        print('Foxen are too powerful')
            
            
            
