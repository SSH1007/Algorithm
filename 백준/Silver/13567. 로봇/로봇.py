import sys
input = lambda: sys.stdin.readline().rstrip()


M, N = map(int, input().split())
r, c = 0, 0
drc = [(0, 1), (-1, 0), (0, -1), (1, 0)]
dir = 0
for _ in range(N):
    C, n = input().split()
    n = int(n)
    if C == 'MOVE':
        r += drc[dir][0]*n
        c += drc[dir][1]*n
        if r < 0 or r > M or c < 0 or c > M:
            print(-1)
            exit(0)
    else:
        if n:
            dir = (dir+1)%4
        else:
            dir = (dir-1)%4

print(c, r)