import sys
input = lambda: sys.stdin.readline().rstrip()


def GCD(A, B):
    while B != 0:
        A, B = B, A % B
    return A


N, M = map(int, input().split())
print(M-GCD(N, M))