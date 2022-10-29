import sys
input = sys.stdin.readline
# 상자의 크기 M * N  (2~1000)
M, N = map(int, input().split())
# 1 : 익은 토마토, 0 : 익지 않은 토마토, -1 : 토마토가 들어있지 않은 칸
tomatoes = [list(map(int, input().split())) for _ in range(N)]

from collections import deque
q = deque()
for n in range(N):
    for m in range(M):
        if tomatoes[n][m] == 1:
            q.append((n,m))

while q:
    x, y = q.popleft()
    for c, r in [(1,0), (-1,0), (0, -1), (0,1)]:
        xc = x+c
        yr = y+r
        if 0 <= xc < N and 0 <= yr < M:
            if tomatoes[xc][yr] == 0:
                tomatoes[xc][yr] = tomatoes[x][y]+1
                q.append((xc,yr))

def judge(tomatoes):
    dap = 0
    for tomato in tomatoes:
        for t in tomato:
            if t==0:
                return -1
        else:
            dap = max(dap, max(tomato))
            # 토마토가 익은 상태 1부터 시작하기 때문에 1을 빼준다.
    return dap-1

print(judge(tomatoes))