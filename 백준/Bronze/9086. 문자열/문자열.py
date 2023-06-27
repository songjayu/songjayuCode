testNum = int(input())
testCase = []
for _ in range(testNum):
    testCase.append(input())

for i in range(testNum):
    print(testCase[i][0], end='')
    print(testCase[i][-1])