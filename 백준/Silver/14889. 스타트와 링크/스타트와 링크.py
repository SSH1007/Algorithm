N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
visited = [False] * N
dap = 1000000000000

# DFS-백트래킹 함수
def DFS(n, idx):
    global dap

    if n == N//2:
        A, B = 0, 0
        for i in range(N-1):
            for j in range(i+1, N):
                if visited[i] and visited[j]:
                    A += (graph[i][j] + graph[j][i])
                elif not visited[i] and not visited[j]:
                    B += (graph[i][j] + graph[j][i])
        dap = min(dap, abs(A-B))
        return

    for i in range(idx, N):
        if not visited[i]:
            visited[i] = True
            DFS(n+1, i+1)
            visited[i] = False


DFS(0, 0)
print(dap)