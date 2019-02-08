rabbits = int(input())
groupsize = int(input())

remaining = rabbits % groupsize

if rabbits < groupsize:
    print(groupsize-rabbits)
elif remaining < groupsize - remaining:
    print(remaining)
else:
    print(groupsize - remaining)
