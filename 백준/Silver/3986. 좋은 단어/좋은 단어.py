import sys
input = sys.stdin.readline
N = int(input().rstrip())
dap = 0
for _ in range(N):
    AB = input().rstrip()
    stack = []
    for i in range(len(AB)):
        if stack and stack[-1] == AB[i]:
            stack.pop()
        else:
            stack.append(AB[i])
    if not stack:
        dap += 1

print(dap)