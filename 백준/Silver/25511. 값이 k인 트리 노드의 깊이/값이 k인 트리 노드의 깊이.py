import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000000)
n, k = map(int, input().rstrip().split())
tree = [[] for _ in range(n)]
for _ in range(n-1):
    p, c = map(int, input().rstrip().split())
    tree[p].append(c)
value = list(map(int, input().rstrip().split()))

dap = 0
depth = 0
visited = [False] * n
def DFS(start):
    global dap, depth
    if value[start] == k:
        dap = depth
    visited[start] = True
    for node in tree[start]:
        if not visited[node]:
            depth += 1
            DFS(node)
            depth -= 1

DFS(0)
print(dap)