import sys
input = sys.stdin.readline


def uh(a, b):
    while b != 0:
        a, b = b, a % b
    return a


N, S = map(int, input().rstrip().split())
As = sorted(list(map(int, input().rstrip().split())), reverse=True)
if N == 1:
    print(abs(As[0]-S))
else:
    dap = abs(As[0]-S)
    for i in range(1, N):
        dap = uh(dap, abs(As[i]-S))
    print(dap)