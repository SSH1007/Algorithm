import sys
input = sys.stdin.readline
N, M = map(int, input().rstrip().split())
lst = list(map(int, input().rstrip().split()))
lst.sort()
stack = []

def dfs(stack):
    if len(stack) == M:
        print(*stack)
        return
    for i in range(len(lst)):
        stack.append(lst[i])
        dfs(stack)
        stack.pop()

dfs(stack)