import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque


def main():
    _ = int(input())
    As = list(map(int, input().split()))
    q = deque(sorted(As, reverse=True))
    A, B = 0, 0
    while q:
        if len(q)%2:
            B += q.pop()
        else:
            A += q.popleft()
        if A <= B:
            print('Bob')
            break
    else:
        print('Alice')


if __name__ == '__main__':
    main()