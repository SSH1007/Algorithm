import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque


def main():
    N = int(input())
    q = deque([N])
    v, cnt = N-1, N-1
    while v != 0:
        q.appendleft(v)
        for _ in range(cnt):
            q.appendleft(q.pop())
        cnt -= 1
        v -= 1
    print(*q)


if __name__ == '__main__':
    main()