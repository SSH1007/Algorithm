import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    X, Y = map(int, input().split())
    N = int(input())
    for _ in range(N):
        x, y = map(int, input().split())
        if x == X or Y == y:
            print(0)
        else:
            print(1)


if __name__ == '__main__':
    main()