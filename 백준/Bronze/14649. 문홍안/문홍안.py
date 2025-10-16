import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque


def main():
    P = int(input())
    N = int(input())
    stone = [0]*100
    q = deque()
    for _ in range(N):
        p, d = input().split()
        p = int(p)-1
        q.append((p, d))
    while q:
        np, nd = q.popleft()
        if nd == 'R':
            np += 1
        else:
            np -= 1
        if 0 <= np < 100:
            stone[np] = (stone[np]+1)%3
            q.append((np, nd))
    print(f'{P*stone.count(0)/100:.2f}')
    print(f'{P*stone.count(1)/100:.2f}')
    print(f'{P*stone.count(2)/100:.2f}')


if __name__ == '__main__':
    main()