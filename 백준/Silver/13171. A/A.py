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


A = int(input().rstrip())
X = int(input().rstrip())
C = 10**9+7
print(fpow(A,X,C))