# 데큐 임포트
from collections import deque
# N : 인원 수, K : 제거할 K번째 순번
N, K = map(int, input().split())

baskets= deque([i for i in range(1,N+1)])
dap = []
while baskets:
    for _ in range(K-1):
        a = baskets.popleft()
        baskets.append(a)
    b = baskets.popleft()
    dap.append(b)
print('<', end='')
print(*dap, sep=', ', end='')
print('>')