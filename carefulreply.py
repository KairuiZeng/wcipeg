texts = int(input())
for x in range(texts):
    text = input()
    count = 0
    reply = '<3'
    for x in range(len(text)):
        if text[x:x+2] == '<3':
            count+=1
    for x in range(count):
        reply += ' <3'
    print(reply)
