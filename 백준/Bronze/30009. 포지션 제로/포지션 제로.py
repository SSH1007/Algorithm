import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N = int(input())
    X, Y, R = map(int, input().split())
    A, B = 0, 0
    for _ in range(N):
        T = int(input())
        if X-R < T < X+R:
            A += 1
        elif X-R == T or X+R == T:
            B += 1
    print(A, B)


if __name__ == '__main__':
    main()