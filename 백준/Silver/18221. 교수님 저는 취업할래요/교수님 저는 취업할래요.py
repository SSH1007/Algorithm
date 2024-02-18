import sys
input = sys.stdin.readline
N = int(input().rstrip())
classroom = [list(map(int, input().rstrip().split())) for _ in range(N)]
s, p = [], []
for i in range(N):
    for j in range(N):
        if classroom[i][j] == 2:
            s = [i, j]
        elif classroom[i][j] == 5:
            p = [i, j]
distance = ((s[0]-p[0])**2 + (s[1]-p[1])**2)**0.5

cnt = 0
for i in range(min(s[0], p[0]), max(s[0], p[0])+1):
    for j in range(min(s[1], p[1]), max(s[1], p[1])+1):
        if classroom[i][j] == 1:
            cnt += 1

if distance >= 5 and cnt >= 3:
    print(1)
else:
    print(0)