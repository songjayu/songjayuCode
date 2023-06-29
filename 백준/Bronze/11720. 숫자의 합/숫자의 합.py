testNumber = int(input())
number = list(input())
sum = int(0)

for i in range(len(number)):
    sum += int(number[i])

print(sum)