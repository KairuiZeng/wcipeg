rounds = int(input())
play = True
while play and rounds != 0:
    opphand = input()
    if opphand == 'Scissors':
        print('Rock')
    elif opphand == 'Rock':
        print('Paper')
    elif opphand == 'Paper':
        print('Scissors')
    elif opphand == 'Fox':
        print('Foxen')
    else:
        play = False
    rounds -=1
