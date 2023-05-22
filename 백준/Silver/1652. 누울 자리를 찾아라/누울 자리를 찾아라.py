import sys
input = sys.stdin.readline
N = int(input().rstrip())
roomInfo = [list(input().rstrip()) for _ in range(N)]
newRoom = [[[] for _ in range(N)] for _ in range(N)]
for i in range(N):
    for j in range(N):
        newRoom[j][N-1-i] = roomInfo[i][j]
h, v = 0, 0
for i in range(N):
    tmplst1 = (''.join(roomInfo[i]).split('X'))
    for t in tmplst1:
        if len(t) > 1:
            h+=1
    tmplst2 = (''.join(newRoom[i]).split('X'))
    for t in tmplst2:
        if len(t) > 1:
            v+=1
print(h, v)