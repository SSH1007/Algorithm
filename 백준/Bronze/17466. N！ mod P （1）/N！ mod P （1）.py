import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N, P = map(int, input().split())
    tmp = 1
    for n in range(1, N+1):
        tmp *= n
        tmp %= P
    print(tmp)


if __name__ == '__main__':
    main()