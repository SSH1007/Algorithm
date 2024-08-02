import sys
input = lambda: sys.stdin.readline().rstrip()
import heapq

def main():
    N = int(input())
    info = []
    for _ in range(N):
        s, e = map(int, input().split())
        info.append((s, e))
    info.sort()
    
    hq = []
    for s, e in info:
        if hq and s >= hq[0][0]:
            heapq.heappop(hq)
        heapq.heappush(hq, (e, s))
    print(len(hq))


if __name__ == '__main__':
    main()