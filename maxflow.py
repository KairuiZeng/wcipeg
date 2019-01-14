scenarios = int(input())
for x in range(scenarios):
    flows = int(input())
    for y in range(flows):
        newvalue = int(input())
        if y == 0 or newvalue > value:
            value = newvalue
    print(value)    
