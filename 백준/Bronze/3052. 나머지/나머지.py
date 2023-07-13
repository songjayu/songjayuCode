storage = set()
count = 0

for i in range(10):
    number = int(input())
    storage.add(number%42)

print(len(storage))