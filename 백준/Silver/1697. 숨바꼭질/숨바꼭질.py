import sys
input = sys.stdin.readline

from collections import deque

def bfs(x):
    q = deque([x])
    while q:
        v = q.popleft()
        if v == K:
            break
        # -1, +1 *2 범위로만 이동한다는게 중요
        for i in [v-1, v+1, v*2]:
            if 0 <= i <= max_ and distance[i]==0:
                q.append(i)
                distance[i] += distance[v]+1

max_ = 100000
distance = [0 for _ in range(max_+1)]
N, K = map(int, input().split())
bfs(N)
print(distance[K])