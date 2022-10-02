import heapq
import sys
input = sys.stdin.readline
N = int(input())
que = []
for _ in range(N):
    x = int(input())
    if x:
        heapq.heappush(que,(abs(x),x))
    else:
        if len(que):
            absdap, dap = heapq.heappop(que)
            print(dap)
        else:
            print(0)