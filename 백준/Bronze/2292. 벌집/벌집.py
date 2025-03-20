def find_layer(N):
    if N == 1:
        return 1
    layer = 1
    maxNum = 1
    while maxNum < N:
        maxNum += 6 * layer
        layer += 1
    return layer
print(find_layer(int(input())))