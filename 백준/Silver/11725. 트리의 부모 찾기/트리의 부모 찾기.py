def BFS(tree, start, visited):
    que = deque([start])
    while que:
        new_node = que.popleft()
        for node in tree[new_node]:
            if visited[node]==0:
                visited[node] = new_node
                que.append(node)
import sys
input = sys.stdin.readline
from collections import deque
N = int(input())
tree = [[] for _ in range(N+1)]
visited = [0]*(N+1)
for _ in range(N-1):
    a,b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)
visited[1] = 1
BFS(tree, 1, visited)
for t in visited[2:]:
    print(t)