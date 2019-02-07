import math

rounds = 5
while rounds != 0:
    astring = input()
    hold = astring.index("_")
    viable = []
    yeet = 0
    
    if hold == 0:
        yeet = 1
        
    for x in range(yeet,10):
        testnum = int(astring[:hold] + str(x) + astring[hold+1:])
        divisible = False
        tester = 2
        if testnum == 1:
            divisible = True
        
        while tester <= math.sqrt(testnum) and not(divisible):
            if testnum % tester == 0:
                divisible = True
            tester += 1
            
        if not(divisible):
            viable.append(x)
            
    if viable == []:
        print("Not possible")
    else:
        stringit = ''
        for length in range(len(viable)):
            if length == len(viable) -1:
                stringit += str(viable[length])
            else:
                stringit += str(viable[length]) + ' '
        print(stringit)


    rounds -= 1
