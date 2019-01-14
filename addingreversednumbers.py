scenarios = int(input())
for x in range(scenarios):
    textnum1, textnum2 = input().split()
    num1 = int(textnum1)
    num2 = int(textnum2)
    while num1 % 10 == 0:
        num1 = num1 // 10
    while num2 % 10 == 0:
        num2 = num2 // 10
    num1 = str(num1)
    num2 = str(num2)
    rnum1 = ''
    rnum2 = ''
    for x in range(len(num1)):
        rnum1 = num1[x] + rnum1
    for x in range(len(num2)):
        rnum2 = num2[x] + rnum2
    totalnum = int(rnum1) + int(rnum2)
    while totalnum % 10 == 0:
        totalnum = totalnum // 10
    totalnum = str(totalnum)
    rtotalnum = ''
    for x in range(len(totalnum)):
        rtotalnum = totalnum[x] + rtotalnum
    print(rtotalnum)
    
            
