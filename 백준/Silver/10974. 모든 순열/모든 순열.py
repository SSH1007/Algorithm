# 순열 구현
import sys
input = sys.stdin.readline
N = int(input())
lst = [i+1 for i in range(N)]
stack = []
used = [0 for _ in range(N)]

def dfs(stack):
    if len(stack) == N:
        print(*stack)
        return
    for i in range(len(lst)):
        if not used[i]:
            stack.append(lst[i])
            used[i] = 1
            dfs(stack)
            used[i] = 0
            stack.pop()
dfs(stack)