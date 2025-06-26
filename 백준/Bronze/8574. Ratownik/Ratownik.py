import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    n, k, x, y = map(int, input().split())
    N = 0
    for _ in range(n):
        xi, yi = map(int, input().split())
        if abs(x-xi)**2+abs(y-yi)**2 > k**2:
            N += 1
    print(N)


if __name__ == '__main__':
    main()