N = int(input())
graph = [[] for _ in range(N+1)]
root = 0
# 트리에 맞게 부모 []에 자식들 번호 집어넣기
# -1은 루트
for n in range(1, N+1):
    parent = int(input())
    if parent == -1:
        root = n
    else:
        graph[parent].append(n)

visited = [0]*(N+1)


def DFS(start):
    for node in graph[start]:
        if not visited[node]:
            visited[node] = visited[start]+1
            DFS(node)


DFS(root)
for v in visited[1:]:
    print(v)