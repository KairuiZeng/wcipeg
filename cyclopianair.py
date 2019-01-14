cards = int(input())
firstcard = int(input())
heldcard = firstcard
cards -= 1
best = 'nothing'
while cards > 0:
    card = int(input())
    if best == 'nothing':
        best = heldcard*card
    else:
        best = max(heldcard*card, best)
    heldcard = card
    cards -=1
    
best = max(heldcard*firstcard, best)
print(best)
    
