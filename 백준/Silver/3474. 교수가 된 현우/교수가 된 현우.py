import sys
input = sys.stdin.readline
T = int(input().rstrip())
for _ in range(T):
    dap = 0
    N = int(input().rstrip())
    n = 5
    while n <= N:
        dap += N//n
        n *= 5
    print(dap)