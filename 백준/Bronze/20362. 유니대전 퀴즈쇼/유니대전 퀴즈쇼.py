import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import defaultdict


def main():
    N, S = input().split()
    dic = defaultdict(int)
    for _ in range(int(N)):
        n, c = input().split()
        if n == S:
            print(dic[c])
            return
        if c not in dic:
            dic[c] = 1
        else:
            dic[c] += 1


if __name__ == '__main__':
    main()