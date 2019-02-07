name = input()
acount = 0
vowel = 0

for x in name:
    if x.lower() == 'a':
        acount += 1
    elif x.lower() == 'e' or x.lower() == 'i' or x.lower() == 'o' or x.lower() == 'u':
        vowel += 1

if acount >= vowel:
    print('Advance to next round')
else:
    print('Does not advance to next round')
