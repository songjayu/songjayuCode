A, B = map(list, input().split())
A = A[::-1]
B = B[::-1]

if A > B:
    print(''.join(A))
elif A < B:
    print(''.join(B))
else:
    pass