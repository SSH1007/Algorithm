import sys
input = sys.stdin.readline
from collections import deque
N = int(input().rstrip())
stones = list(map(int, input().rstrip().split()))
s = int(input().rstrip())-1
q = deque([(s-stones[s], s+stones[s])])
visited = [0]*(N+1)
visited[s] = 1

while q:
    l, r = q.popleft()
    if l >= 0:
        if not visited[l]:
            visited[l] = 1
            q.append((l-stones[l], l+stones[l]))
    if r < N:
        if not visited[r]:
            visited[r] = 1
            q.append((r-stones[r], r+stones[r]))

print(sum(visited))