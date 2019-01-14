start, stop = input().split()
start = int(start)
stop = int(stop)

listofprime = [3]
primetest = 5

if start <= 2 and stop >= 4:
    print(2)
    print(3)

while primetest <= stop:
    listcount = 0
    divisible = False
    while listofprime[listcount] <= primetest**(0.5) and not(divisible):
        if primetest % listofprime[listcount] == 0:
            divisible = True
        listcount +=1
        
    if not(divisible):
        listofprime.insert(len(listofprime), primetest)
        if primetest >= start:
            print(primetest)

    primetest += 2





