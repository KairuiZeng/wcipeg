receive = -1
while receive != 0:
    surfacelist = []
    voidtotal = 0
    maximum = -1
    minimum = 25
    receive = int(input())    
    for receive in range(receive):
        count = 0
        spaced = False
        surface = input()
        
        while count < len(surface) and not(spaced):
            if surface[count] == ' ':
                spaced = True
            count += 1
                
        if spaced:
            parta, partb = surface.split()
            surface = parta + partb
            
        surfacelist.append(len(surface))

        maximum = max(len(surface), maximum)

    for x in range(len(surfacelist)):
        voidtotal += maximum - surfacelist[x]
    print(voidtotal)
        
