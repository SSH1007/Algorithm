from collections import deque
N = int(input())
In, Out = deque(), []
dap = 0
for _ in range(N):
    In.append(input())
for _ in range(N):
    out = input()
    while In[0] != out:
        Out.append(In.popleft())
    In.popleft()
    if Out:
        dap += 1
    while Out:
        In.appendleft(Out.pop())
print(dap)