import sys
input = sys.stdin.readline
N, M = map(int, input().rstrip().split())
city = [list(map(int, input().rstrip().split())) for _ in range(N)]
tmp = []
for i in range(N):
    for j in range(M):
        if city[i][j] == 1:
            tmp.append((i, j))
print(abs(tmp[0][0]-tmp[1][0]) + abs(tmp[0][1]-tmp[1][1]))