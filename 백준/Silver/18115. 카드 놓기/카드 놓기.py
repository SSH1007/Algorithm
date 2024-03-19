import sys
input = sys.stdin.readline
from collections import deque
N = int(input().rstrip())
A = list(map(int, input().rstrip().split()))
A.reverse()
q = deque()
for i in range(N):
    if A[i] == 1:
        q.appendleft(i+1)
    elif A[i] == 2:
        q.insert(1, i+1)
    else:
        q.append(i+1)
print(*q)