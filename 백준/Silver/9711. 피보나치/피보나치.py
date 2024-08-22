import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    fibo = [0]*10001
    fibo[0] = 1
    fibo[1] = 1
    fibo[2] = 2
    for i in range(3, 10001):
        fibo[i] = fibo[i-1] + fibo[i-2]

    T = int(input())
    for t in range(1, T+1):
        P, Q = map(int, input().split())
        print('Case #%d: %d' % (t, fibo[P-1] % Q))


if __name__ == '__main__':
    main()