import sys
input = sys.stdin.readline
N, M = map(int, input().rstrip().split())
lst = list(map(int, input().rstrip().split()))
lst.sort()
visited = [0]*N
stack = []


def DFS():
    if len(stack) == M:
        print(*stack)
        return
    duplicated = -1
    for i in range(N):
        if not visited[i] and duplicated != lst[i]:
            stack.append(lst[i])
            visited[i] = 1
            duplicated = lst[i]
            DFS()
            stack.pop()
            visited[i] = 0


DFS()