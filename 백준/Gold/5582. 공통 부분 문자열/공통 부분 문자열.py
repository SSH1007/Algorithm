import sys
input = sys.stdin.readline


def main():
    first = ' ' + input().rstrip()
    second = ' ' + input().rstrip()
    F, S = len(first), len(second)
    dp = [0]*F
    dap = 0

    for s in range(1, S):
        tmp = [0]*F
        for f in range(1, F):
            if first[f] == second[s]:
                tmp[f] = dp[f-1]+1
                dap = max(dap, tmp[f])
        dp = tmp[:]
    print(dap)


if __name__ == '__main__':
    main()