from collections import deque
A, B = map(int, input().split())
q = deque([(A, 0)])
while q:
    a, cnt = q.popleft()
    if a == B:
        print(cnt+1)
        exit(0)
    for i in [a*2, a*10+1]:
        if i <= B:
            q.append((i, cnt+1))
print(-1)