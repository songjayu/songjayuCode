floor = int(input())

for i in range(1,floor+1):
    print(' '*int(floor-i),end='')
    print('*'*int(2*i-1))

for j in range(floor-1):
    print(' '*int(j+1),end='')
    print('*'*int(2*floor-(2*j+3)))