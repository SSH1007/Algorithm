import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N = int(input())
    lst = list(map(int, input().split()))
    dp = [0]*(N+1)
    for i in range(N):
        minV, maxV = lst[i], lst[i]
        j = i-1
        while j >= 0:
            maxV, minV = max(maxV, lst[j]), min(minV, lst[j])
            dp[i] = max(dp[i], dp[j-1]+maxV-minV)
            j -= 1
    print(dp[N-1])


if __name__ == '__main__':
    main()