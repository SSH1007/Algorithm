import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import defaultdict


def main():
    n, m = map(int, input().split())
    dic = defaultdict(int)
    for _ in range(n):
        lst = list(map(int, input().split()))
        for i in range(m):
            dic[i+1] += lst[i]
    dap = list(dic.items())
    dap.sort(key=lambda x: (x[1], -x[0]), reverse=True)
    for d in dap:
        print(d[0], end=' ')


if __name__ == '__main__':
    main()