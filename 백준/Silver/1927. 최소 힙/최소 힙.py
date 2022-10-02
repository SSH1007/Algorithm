import heapq
import sys
input = sys.stdin.readline
N = int(input())
que = []
for _ in range(N):
    x = int(input())
    if x:
        heapq.heappush(que,x)
    else:
        if len(que):
            print(heapq.heappop(que))
        else:
            print(0)