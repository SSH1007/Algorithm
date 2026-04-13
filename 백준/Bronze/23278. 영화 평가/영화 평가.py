import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N, L, H = map(int, input().split())
    lst = sorted(list(map(int, input().split())))
    tmp = 0
    for n in range(L, N-H):
        tmp += lst[n]
    print(tmp/(N-L-H))


if __name__ == '__main__':
    main()