cases = int(input())

for cases in range(cases):

    organization = input()
    ecount = 0
    ccount = 0
    ocount = 0
    final = ''
    
    for letter in organization:
        if letter == 'E':
            ecount += 1
        elif letter == 'C':
            ccount += 1
        else:
            ocount += 1

    for x in range(ecount):
        final += 'Educational '

    for x in range(ccount):
        final += 'Computing '

    for x in range(int(ocount / 2 - 1)):
        final += 'Organization of Ontario '

    final += 'Organization of Ontario'

    print(final)
