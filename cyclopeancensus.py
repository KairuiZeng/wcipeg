count = int(input())
table = []

for x in range(count):
    table.append(int(input()))

table.sort()

queries = int(input())
for queries in range(queries):
    index = int(input()) - 1
    print(table[index])
                 
                
