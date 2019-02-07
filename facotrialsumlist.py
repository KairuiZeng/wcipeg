import math

value = -1

while int(value) != 0:
    
    value = input()
    present = False
    holder = [value]

    while not present and int(value) != 0:
        sum = 0
        
        for digit in holder[-1]:
            sum += math.factorial(int(digit))
            
        for x in holder:
            if int(x) == sum:
                print(len(holder)+1)
                present = True
            
        holder.append(str(sum))
