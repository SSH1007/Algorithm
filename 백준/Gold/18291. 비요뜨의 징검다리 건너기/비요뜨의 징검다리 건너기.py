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


T = int(input().rstrip())
for _ in range(T):
    N = int(input().rstrip())
    C = 10**9+7
    if N == 1 or N == 2:
        print(1)
    else:
        print(fpow(2,N-2,C))