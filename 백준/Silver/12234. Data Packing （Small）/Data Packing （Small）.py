from collections import deque
T = int(input())
for t in range(1, T+1):
    N, X = map(int, input().split())
    lst = list(map(int, input().split()))
    lst.sort()
    que = deque()
    for i in range(N):
        que.append(lst[i])
    arr = []
    while que:
        a = que.pop()
        if len(que)>0:
            b = que.popleft()
            if a+b <= X:
                arr.append((a,b))
            else:
                arr.append(a)
                que.appendleft(b)
        else:
            arr.append(a)
    print(f'Case #{t}: {len(arr)}')