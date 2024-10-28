import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque


def main():
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))
    lst.sort()
    q = deque(lst)
    dap, first = 0, 1
    while q:
        tmp = []
        if abs(q[0]) > abs(q[-1]):
            for _ in range(M):
                if not q or (tmp and tmp[-1]*q[0] < 0):
                    break
                tmp.append(q.popleft())
        else:
            for _ in range(M):
                if not q or (tmp and tmp[-1]*q[-1] < 0):
                    break
                tmp.append(q.pop())
        if tmp[0]*tmp[-1] > 0:
            dap += abs(tmp[0])*first
        else:
            dap += (abs(tmp[0]-tmp[-1]))*first
        first = 2

    print(dap)


if __name__ == '__main__':
    main()