from collections import deque
N, K = map(int, input().split())
que = deque()
for i in range(1,N+1):
    que.append(str(i))
seq = []
while que:
    for i in range(K-1):
        a = que.popleft()
        que.append(a)
    c = que.popleft()
    seq.append(c)
print(f'<{", ".join(seq)}>')