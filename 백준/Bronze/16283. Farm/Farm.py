import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    a, b, n, w = map(int, input().split())
    lst = []
    cnt = 0
    for x in range(1, n):
        if w == a*x+b*(n-x):
            lst.append((x, n-x))
            cnt += 1
    if cnt != 1:
        print(-1)
    else:
        print(*lst[0])


if __name__ == '__main__':
    main()