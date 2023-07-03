testCase = int(input())


for _ in range(testCase):
    a,b = input().split()
    for j in b:
        print(int(a) * j, end='')
    print()