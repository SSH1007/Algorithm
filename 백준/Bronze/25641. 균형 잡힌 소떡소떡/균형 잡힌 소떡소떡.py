from collections import deque
N = int(input())
S = deque(input())
while 1:
    if S.count('t') == S.count('s'):
        break
    S.popleft()
print(*S, sep='')