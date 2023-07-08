import sys
input = sys.stdin.readline

def fpow(A, B, C):
    dap = 1
    while B:
        if B & 1:
            dap *= A
            dap %= C
        A *= A
        A %= C
        B //= 2
    return dap


N = int(input().rstrip())
dap = 0
for _ in range(N):
    C, K = map(int, input().rstrip().split())
    D = 10**9+7
    if K > 0:
        dap += C * K * fpow(2, K-1, D)
    dap%=D
print(dap)