attendant = []

for k in range(1,31):
    attendant.append(k)

for _ in range(28):
    number = int(input())
    for i in attendant:
        if i == number:
            attendant.remove(i)

for l in attendant:
    print(l)