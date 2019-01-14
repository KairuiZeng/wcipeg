holds, jump, special = input().split()
holds = int(holds)
jump = int(jump)
special = int(special)

height = 0

while holds != 0 and special >= 0:
    nexthold = int(input())
    if nexthold - height <= jump:
        holds -= 1
        height = nexthold
    elif nexthold - height <= 2*jump:
        holds -= 1
        height = nexthold
        special -= 1
    else:
        special = -1

if holds == 0:
    print('Too easy!')
else:
    print('Unfair!')
