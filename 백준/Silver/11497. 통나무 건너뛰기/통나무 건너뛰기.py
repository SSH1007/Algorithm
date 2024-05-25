from collections import deque
import sys
input = sys.stdin.readline
T = int(input().rstrip())


def f(lst):
    tmp = deque([lst.pop()])
    chk = 0
    while lst:
        if chk % 2:
            tmp.append(lst.pop())
        else:
            tmp.appendleft(lst.pop())
        chk += 1
    minD = abs(tmp[-1]-tmp[0])
    for n in range(N-1):
        minD = max(minD, abs(tmp[n]-tmp[n+1]))
    return minD


for _ in range(T):
    N = int(input().rstrip())
    L = sorted(list(map(int, input().rstrip().split())))
    dap = f(L)
    print(dap)