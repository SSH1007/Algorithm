import sys
input = sys.stdin.readline
from collections import deque


def main():
    N, K = map(int, input().rstrip().split())
    lst = deque(['?']*N)
    for _ in range(K):
        S, t = input().rstrip().split()
        S = int(S)
        lst.rotate(S)
        if lst[0] == '?':
            lst[0] = t
        elif lst[0] == t:
            continue
        else:
            print('!')
            exit(0)
    for l in lst:
        if l != '?' and lst.count(l) > 1:
            print('!')
            exit(0)
    print(''.join(lst))


if __name__ == '__main__':
    main()