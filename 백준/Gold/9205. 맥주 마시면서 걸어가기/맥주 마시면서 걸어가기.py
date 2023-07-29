import sys
input = sys.stdin.readline
from collections import deque


def BFS():
    q = deque([(homeX, homeY)])
    if abs(homeX-rockX)+abs(homeY-rockY) <= 1000:
        return 'happy'
    while q:
        x, y = q.popleft()
        for sX, sY, n in store:
            if abs(x-sX)+abs(y-sY) <= 1000 and not visited[n]:
                q.append((sX, sY))
                visited[n] = True
                if abs(sX-rockX)+abs(sY-rockY) <= 1000:
                    return 'happy'

    return 'sad'

T = int(input().rstrip())
for _ in range(T):
    N = int(input().rstrip())
    homeX, homeY = map(int, input().rstrip().split())
    store = []
    for n in range(N):
        storeX, storeY = map(int, input().rstrip().split())
        store.append((storeX, storeY, n))
    rockX, rockY = map(int, input().rstrip().split())
    visited = [False]*(N+1)
    print(BFS())