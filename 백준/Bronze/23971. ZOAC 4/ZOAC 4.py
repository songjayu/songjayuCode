H, W, N, M = map(int, input().split())
max_H = 0
max_W = 0

if H % (N+1) == 0 :
    max_H = (H // (N+1))
else:
    max_H = (H // (N+1)) + 1

if W % (M+1) == 0 :
    max_W = (W // (M+1))
else:
    max_W = (W // (M+1)) + 1

gross = max_H * max_W

print(gross)