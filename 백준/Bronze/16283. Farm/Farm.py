import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    a, b, n, w = map(int, input().split())
    lst = []
    for x in range(1, n):
        if w == a*x+b*(n-x):
            lst.append((x, n-x))
    L = len(lst)
    if L > 1 or L == 0:
        print(-1)
    else:
        print(*lst[0])


if __name__ == '__main__':
    main()