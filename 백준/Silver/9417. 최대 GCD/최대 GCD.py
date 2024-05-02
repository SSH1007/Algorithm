import sys
input = sys.stdin.readline
N = int(input().rstrip())


def GCD(a, b):
    while b != 0:
        a, b = b, a % b
    return a


for _ in range(N):
    case = list(map(int, input().rstrip().split()))
    dap = 0
    L = len(case)
    for i in range(L):
        for j in range(i+1, L):
            dap = max(dap, GCD(case[i], case[j]))
    print(dap)