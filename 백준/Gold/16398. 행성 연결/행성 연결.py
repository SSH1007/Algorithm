import sys
input = lambda: sys.stdin.readline().rstrip()


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    rootX = find(x)
    rootY = find(y)
    if rootX != rootY:
        if rootX > rootY:
            parent[rootX] = rootY
        else:
            parent[rootY] = rootX
        return True
    return False


N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
parent = [i for i in range(N)]
graph = []
for r in range(N):
    for c in range(N):
        if r > c:
            graph.append((matrix[r][c], r, c))
graph.sort()

dap, cnt = 0, 0
for cost, A, B in graph:
    if union(A, B):
        dap += cost
        cnt += 1
        if cnt == N-1:
            break
print(dap)