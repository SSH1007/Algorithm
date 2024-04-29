import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
N, M, R = map(int, input().rstrip().split())
visited = [0]*(N+1)
lst = [[] for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, input().rstrip().split())
    lst[u].append(v)
    lst[v].append(u)
for l in lst:
    l.sort(reverse=True)
cnt = 1


def dfs(r):
    global cnt
    visited[r] = cnt
    for node in lst[r]:
        if not visited[node]:
            cnt += 1
            dfs(node)
    return


dfs(R)
print(*visited[1:], sep='\n')