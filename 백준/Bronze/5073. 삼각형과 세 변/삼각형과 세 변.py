import sys
list = []

while True:
    a, b, c = map(int, sys.stdin.readline().split())
    list.append(a)
    list.append(b)
    list.append(c)

    if a == 0 & b == 0 & c == 0:
        break

    maxNum = max(list)
    list.remove(maxNum)
    if maxNum >= list[0] + list[1]:
            print('Invalid')

    elif a == b == c:
        print('Equilateral')
        

    elif ((a == b) and (a != c)) or ((a == c) and (a != b)) or ((b == c) and (a != b)):
        print('Isosceles')
        
    
    elif (a != b) and (a != c):
        print('Scalene')
    list.clear()