import sys
input = sys.stdin.readline
T = int(input().rstrip())
for _ in range(T):
    m, n = map(int, input().rstrip().split())
    box = [list(map(int, input().rstrip().split())) for _ in range(m)]
    box90 = list(map(list, zip(*box)))
    dap = 0
    for b in box90:
        for i in range(m):
            if b[i] == 1:
                dap += b[i+1:].count(0)
    print(dap)