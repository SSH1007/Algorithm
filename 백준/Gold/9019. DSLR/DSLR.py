import sys
input = sys.stdin.readline
from collections import deque


def D(n):
    n = (n * 2) % 10000
    return n, 'D'


def S(n):
    n = n - 1 if n > 0 else 9999
    return n, 'S'


def L(n):
    n = (n % 1000) * 10 + n // 1000
    return n, 'L'


def R(n):
    n = (n % 10) * 1000 + n // 10
    return n, 'R'


T = int(input().rstrip())
for _ in range(T):
    A, B = map(int, input().rstrip().split())
    visited = [0]*10001
    dap = ''

    q = deque([(A, '')])
    while q:
        start, command = q.popleft()
        visited[start] = 1

        if start == B:
            print(command)
            break

        for i,j in [D(start), S(start), L(start), R(start)]:
            if not visited[i]:
                visited[i] = 1
                q.append((i, command+j))