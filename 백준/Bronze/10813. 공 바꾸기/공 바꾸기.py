boxNum, countNum = map(int, input().split())
box = []
for j in range(1,boxNum+1):
    box.append(str(j))

for _ in range(countNum):
    firstbox, secondbox = map(int, input().split())
    box[firstbox-1], box[secondbox-1] = box[secondbox-1], box[firstbox-1]

print(' '.join(box))