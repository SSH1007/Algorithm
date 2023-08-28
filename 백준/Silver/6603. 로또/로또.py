import sys
input = sys.stdin.readline


def DFS(start):
    if len(stack) == 6:
        print(*stack)
        return
    for i in range(start, k):
        if not visited[i]:
            stack.append(S[i])
            visited[i] = 1
            DFS(i)
            stack.pop()
            visited[i] = 0


t = 0
while 1:
    if t != 0:
        print()
    lst = list(map(int, input().rstrip().split()))
    if lst == [0]:
        break
    k = lst[0]
    S = lst[1:]
    visited = [0]*(k+1)
    stack = []
    DFS(0)
    t += 1