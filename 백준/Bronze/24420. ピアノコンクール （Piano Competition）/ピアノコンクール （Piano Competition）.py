import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N = int(input())
    As = sorted(list(map(int, input().split())))
    print(sum(As[1:N-1]))


if __name__ == '__main__':
    main()