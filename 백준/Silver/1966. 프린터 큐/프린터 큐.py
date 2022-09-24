from collections import deque
T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    que = deque(map(int, input().split()))
    idx = deque(range(N))
    cnt = 1 
    while 1:
        if que[0] == max(que):
            if idx[0] == M:
                print(cnt)
                break
            cnt+=1
            que.popleft()
            idx.popleft()
        else:
            que.append(que.popleft())
            idx.append(idx.popleft())