import sys
input = sys.stdin.readline
N = int(input().rstrip())
for _ in range(N):
    c, p = map(int, input().rstrip().split())
    dap = p
    for _ in range(1,c):
        dap+=(p-2)
    print(c,p)
    print(dap)