import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    _ = int(input())
    Ns = set(input().split())
    H = set(input().split())
    print(*Ns-H)


if __name__ == '__main__':
    main()