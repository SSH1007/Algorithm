import sys
input = sys.stdin.readline
# 입력
N, M = map(int, input().rstrip().split())
graph = [input().rstrip() for _ in range(N)]
# 기타 변수 정의
sys.setrecursionlimit(10**6)
visited = [[0]*(M) for _ in range(N)]
dap = 0
# dfs 정의
def dfs(board, r, c):
    global dap
    visited[r][c] = 1
    for dr,dc in [(-1,0),(1,0),(0,-1),(0,1)]:
        nr = r + dr
        nc = c + dc
        if 0 <= nr < N and 0 <= nc < M:
            if not visited[nr][nc]:
                if board[nr][nc] == 'P':
                    dap += 1
                if board[nr][nc] != 'X':
                    dfs(board, nr, nc)
    return
# dfs 동작
for n in range(N):
    for m in range(M):
        if graph[n][m] == 'I':
            dfs(graph, n, m)
print(dap if dap else 'TT')