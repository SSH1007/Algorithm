import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    _ = int(input())
    Ns = list(input().split())
    print(Ns.count(input()))


if __name__ == '__main__':
    main()