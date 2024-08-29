import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import defaultdict


def main():
    N = int(input())
    for _ in range(N):
        V = int(input())
        dic = defaultdict(int)
        for _ in range(V):
            S = int(input())
            dic[S] += 1
        item = sorted(dic.items(), key=lambda x: (-x[1], x[0]))
        print(item[0][0])


if __name__ == '__main__':
    main()