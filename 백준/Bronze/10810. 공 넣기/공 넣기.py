N, M = map(int, input().split())
Nprint = list()

for x in range(N):
    Nprint.append(0)


for y in range(M):
    i, j, k = map(int, input().split())
    for z in range(i,j+1):
        Nprint[z-1] = k

print(' '.join(map(str, Nprint[0:N+1])))