# first warm up part
version = input()
if version == '1A':
    stringthing = input()
    count = 0

    for character in stringthing:
        if count == 0 and character == ')':
            print(False)
        elif character == '(':
            count += 1
        else:
            count -= 1

    if count == 0:
        print(True)
    else:
        print(False)


elif version == '1B':
    stringthing = input()
    openlist = []
    valid = True

    for char in stringthing:
        if char == '(' or char == '[' or char == '{':
            openlist.append(char)
        elif openlist == []:
            print(False)
        else:
            if char == ')':
                if openlist[-1] != '(':
                    print(False)
                    valid = False
                    break
            elif char == ']':
                if openlist[-1] != '[':
                    print(False)
                    valid = False
                    break
            else:
                if openlist[-1] != '}':
                    print(False)
                    valid = False
                    break
    if valid:
        print(True)

elif version == '2':
    #make a hashtable? dictionary
    #variable = dict()
    #h[key] = value
    #h[key
    

                
