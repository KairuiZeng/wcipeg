n = int(input())
count = 5
oddprimes =[3]

if n == 2:
    print('prime')
elif n % 2 == 0:
    print('not')
elif n <= 1:
    print('not')
else:
    while count <= n**(0.5):
        divisible = False
        for x in range(len(oddprimes)):
            if count % oddprimes[x] == 0:
                divisible = True

        if not(divisible):
            oddprimes.insert(len(oddprimes), count)

        count += 2

    divisible = False
    for x in range(len(oddprimes)):
        if n % oddprimes[x] == 0:
            divisible = True

    if divisible:
        print('not')
    else:
        print('prime')
        
