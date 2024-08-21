import sys
input = lambda: sys.stdin.readline().rstrip()
from bisect import bisect_left


def main():
    N = int(input())
    As = list(map(int, input().split()))

    def F(lst, flag):
        if len(lst) == 0:
            return 0
        if flag:
            lst = [l*-1 for l in lst]
        dp = [lst[0]]
        for x in range(len(lst)):
            if lst[x] > dp[-1]:
                dp.append(lst[x])
            else:
                idx = bisect_left(dp, lst[x])
                dp[idx] = lst[x]
        return len(dp)

    dap = -1
    for i in range(N):
        dap = max(dap, F(As[:i+1], 0)+F(As[i:], 1))
    # i를 분기점으로 최장증가부분수열, 최장감소부분수열을 구해 더했으니
    # i가 중복됨. 따라서 -1
    print(dap-1)


if __name__ == '__main__':
    main()