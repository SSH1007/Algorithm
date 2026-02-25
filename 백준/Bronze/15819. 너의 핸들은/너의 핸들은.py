import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N, I = map(int, input().split())
    lst = [input() for _ in range(N)]
    print(sorted(lst)[I-1])


if __name__ == '__main__':
    main()