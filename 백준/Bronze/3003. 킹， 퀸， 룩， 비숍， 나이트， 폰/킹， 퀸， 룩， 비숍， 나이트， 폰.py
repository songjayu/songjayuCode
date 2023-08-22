a, b, c, d, e, f = map(int,input().split())
chess = [a,b,c,d,e,f]
originalChess = [1,1,2,2,2,8]
chessChange = []

for i in range(0,6):
    chessChange.append(str(originalChess[i]-chess[i]))

print(' '.join(chessChange))