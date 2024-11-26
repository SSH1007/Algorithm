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
        if rank[rootX] > rank[rootY]:
            parent[rootY] = rootX
        elif rank[rootX] < rank[rootY]:
            parent[rootX] = rootY
        else:
            parent[rootY] = rootX
            rank[rootX] += 1
        return True
    return False


N, M, t = map(int, input().split())
parent = [i for i in range(N)]
rank = [0]*N
graph = []
for _ in range(M):
    A, B, C = map(int, input().split())
    graph.append((C, A-1, B-1))
graph.sort()
dap = 0

cost = 0
for C, A, B in graph:
    if union(A, B):
        dap += C + cost
        cost += t
print(dap)