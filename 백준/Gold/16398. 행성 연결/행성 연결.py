import sys
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10**6)


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    rootX = find(x)
    rootY = find(y)
    if rootX != rootY:
        if rootX > rootY:
            parent[rootY] = rootX
        else:
            parent[rootX] = rootY
        return True
    return False


N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
parent = [i for i in range(N)]
graph = []
for r in range(N):
    for c in range(r+1, N):
        graph.append((matrix[r][c], r, c))
graph.sort()

dap = 0
for cost, A, B in graph:
    if union(A, B):
        dap += cost
print(dap)