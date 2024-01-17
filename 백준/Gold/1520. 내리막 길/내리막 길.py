import sys
input = sys.stdin.readline
# 세로 크기 M, 가로 크기 N
M, N = map(int, input().rstrip().split())
maps = [list(map(int, input().rstrip().split())) for _ in range(M)]
dp = [[-1]*N for _ in range(M)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def DFS(r, c):
    # 도착점이면 도착점까지의 길 1을 리턴
    if r == M-1 and c == N-1:
        return 1
    # 이미 간 곳이면 그 위치에서 출발하는 경우의 수 리턴
    if dp[r][c] != -1:
        return dp[r][c]
    # 해당 위치 r,c에서부터 도착점에 도달할 수 있는지를 판별하는 수
    # 끝까지 돌렸는데 canGo가 0이면,
    # 이 루트로 방문은 했지만 여기선 도착점까진 갈 수 없다는 의미
    canGo = 0
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < M and 0 <= nc < N:
            if maps[nr][nc] < maps[r][c]:
                canGo += DFS(nr, nc)
    dp[r][c] = canGo
    return dp[r][c]

print(DFS(0, 0))