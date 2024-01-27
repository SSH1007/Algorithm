from collections import deque
N = int(input())
bridge = [0]+list(map(int, input().split()))
a, b = map(int, input().split())
visited = [-1]*(N+1)


def BFS():
    q = deque([])
    q.append(a)
    visited[a] = 0
    while q:
        start = q.popleft()
        if start == b:
            return visited[start]
        for i in range(start, N+1, bridge[start]):
            if visited[i] == -1:
                q.append(i)
                visited[i] = visited[start]+1
        for i in range(start, 0, -bridge[start]):
            if visited[i] == -1:
                q.append(i)
                visited[i] = visited[start]+1
    return -1


print(BFS())