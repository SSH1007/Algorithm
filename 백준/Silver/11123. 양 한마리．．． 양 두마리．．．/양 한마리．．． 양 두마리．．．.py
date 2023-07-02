import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

T = int(input().rstrip())
for _ in range(T):
    H, W = map(int, input().rstrip().split())
    graph = [input().rstrip() for _ in range(H)]
    dap = 0
    visited = [[0]*W for _ in range(H)]

    def dfs(h, w):
        visited[h][w] = 1
        for dh, dw in [(-1,0), (1,0), (0,-1), (0,1)]:
            nh = h+dh
            nw = w+dw
            if 0 <= nh < H and 0 <= nw < W and not visited[nh][nw] and graph[nh][nw] == '#':
                dfs(nh, nw)

    for h in range(H):
        for w in range(W):
            if graph[h][w] == '#' and not visited[h][w]:
                dfs(h, w)
                dap += 1
    print(dap)