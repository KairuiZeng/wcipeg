listsize = int(input())
list = []

for x in range(listsize):
    value = int(input())
    if list == []:
        list.insert(0, value)
    else:
        count = 0
        while count != -1:
            if count == len(list):
                list.insert(len(list), value)
                count = -1
            elif value < list[count]:
                list.insert(count, value)
                count = -1
            else:
                count += 1

for x in range(listsize):
    print(list[x])
