import sys
input = lambda: sys.stdin.readline().rstrip()
from math import gcd


def F():
    D1, D2 = map(int, input().split())
    s = [[0]*(D2+1) for _ in range(D2+1)]
    cnt = 0
    for i in range(D1, D2+1):
        for j in range(1, i+1):
            k = gcd(i, j)
            a, b = i//k, j//k
            if not s[a][b]:
                s[a][b] = 1
                cnt += 1
    print(cnt)


F()