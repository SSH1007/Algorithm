import sys
input = sys.stdin.readline
T = int(input().rstrip())
for _ in range(T):
    dap = 0
    N = int(input().rstrip())
    for _ in range(N):
        a, b, c = map(int, input().rstrip().split())
        plus = max(a,b,c)
        if plus>0:
            dap+=plus
    print(dap)