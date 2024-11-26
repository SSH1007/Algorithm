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
        if parent[rootX] > parent[rootY]:
            parent[rootY] = rootX
        else:
            parent[rootX] = rootY
        return True
    return False


n = int(input())
parent = [i for i in range(n)]
info = []
for _ in range(n):
    x, y = map(float, input().split())
    info.append((x, y))
graph = []
for i in range(n):
    for j in range(i+1, n):
        ly = ((info[i][0]-info[j][0])**2 + (info[i][1]-info[j][1])**2)**0.5
        graph.append((ly, i, j))
graph.sort()

dap = 0
for cost, A, B in graph:
    if union(A, B):
        dap += cost
print(dap)