teachers, budget = input().split()
teachers = int(teachers)
budget = int(budget)
sum = 0

for x in range(teachers):
    sum += int(input())

if sum > budget:
    print('The budget will balance itself')
else:
    print(budget-sum)
