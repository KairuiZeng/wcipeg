count = int(input())
arrayofprime = [2]
primetest = 3
while len(arrayofprime) < count:
    divisible = False
    for x in range(len(arrayofprime)):
        if primetest % arrayofprime[x] == 0:
            divisible = True
    if not(divisible):
        arrayofprime.insert(len(arrayofprime), primetest)
    primetest += 2

for x in range(count):
    print(arrayofprime[x])
