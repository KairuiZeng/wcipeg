students = int(input())
marks = []
for x in range(students):
    testscore = int(input())
    marks.insert(0, testscore)
marks.sort()

if students % 2 == 0:
    median = (marks[students//2-1] + marks[students//2]) / 2
else:
    median = marks[students//2] / 1

print('The median on the test is ' + str(median))
