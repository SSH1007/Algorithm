from collections import deque
import sys
input = sys.stdin.readline
N = int(input().rstrip())
In, Out = deque(), []
dap = 0
for _ in range(N):
    In.append(input().rstrip())
for _ in range(N):
    out = input().rstrip()
    while In[0] != out:
        Out.append(In.popleft())
    In.popleft()
    if Out:
        dap += 1
    while Out:
        In.appendleft(Out.pop())
print(dap)