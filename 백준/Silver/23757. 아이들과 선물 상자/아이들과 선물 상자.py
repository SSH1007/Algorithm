import sys
input = lambda: sys.stdin.readline().rstrip()
import heapq


N, M = map(int, input().split())
lst = list(map(int, input().split()))
hq = [-1*l for l in lst]
kids = list(map(int, input().split()))
heapq.heapify(hq)

for k in kids:
    m = heapq.heappop(hq)
    if abs(m) >= k:
        heapq.heappush(hq, m+k)
    else:
        print(0)
        break
else:
    print(1)