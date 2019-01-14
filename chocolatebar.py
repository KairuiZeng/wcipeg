scenarios = int(input())
for scenarios in range(scenarios):
    height, width = input().split()
    height = int(height)
    width = int(width)
    print(height*width-1)
