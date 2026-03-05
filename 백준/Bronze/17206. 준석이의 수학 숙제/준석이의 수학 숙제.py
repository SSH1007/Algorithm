import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    T = int(input())
    Ns = list(map(int, input().split()))
    dp = [0]*80001
    tmp = 0
    for i in range(1, 80001):
        if i%3 == 0 and i%7 == 0:
            tmp += i
        elif i%3 == 0:
            tmp += i
        elif i%7 == 0:
            tmp += i
        dp[i] = tmp
    for t in range(T):
        print(dp[Ns[t]])


if __name__ == '__main__':
    main()