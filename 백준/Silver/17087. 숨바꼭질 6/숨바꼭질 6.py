import sys
input = sys.stdin.readline


def uh(a, b):
    while b != 0:
        a, b = b, a % b
    return a


N, S = map(int, input().rstrip().split())
As = sorted(list(map(int, input().rstrip().split())), reverse=True)
dap = 0
if N == 1:
    print(abs(As[0]-S))
else:
    for i in range(1, N):
        dap = uh(dap, uh(abs(As[i-1]-S), abs(As[i]-S)))
    print(dap)