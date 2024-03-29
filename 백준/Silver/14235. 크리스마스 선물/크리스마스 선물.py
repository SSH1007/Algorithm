import heapq
import sys
input = sys.stdin.readline
n = int(input().rstrip())
sack = []
for _ in range(n):
    lst = list(map(int, input().rstrip().split()))
    if lst[0] == 0:
        print(-heapq.heappop(sack) if sack else -1)
    else:
        for l in lst[1:]:
            heapq.heappush(sack, -l)