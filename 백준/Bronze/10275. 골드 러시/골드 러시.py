import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    t = int(input())
    for _ in range(t):
        n, a, b = map(int, input().split())
        print(n-bin(min(a, b))[::-1].index('1'))


if __name__ == '__main__':
    main()