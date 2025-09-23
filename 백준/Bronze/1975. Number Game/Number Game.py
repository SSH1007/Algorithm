import sys
input = lambda: sys.stdin.readline().rstrip()


def f(a, b):
    if b != 0 and a % b == 0:
        return 1+f(a//b, b)
    return 0


def main():
    T = int(input())
    Z = [0]*1001
    for i in range(2, 1001):
        for j in range(2, i+1):
            Z[i] += f(i, j)
    for _ in range(T):
        N = int(input())
        print(Z[N])


if __name__ == '__main__':
    main()