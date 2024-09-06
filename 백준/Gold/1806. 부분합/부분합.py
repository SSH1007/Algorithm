import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N, S = map(int, input().split())
    hap = [0]*(N+1)
    nums = list(map(int, input().split()))
    for i in range(N):
        hap[i+1] = hap[i] + nums[i]
    dap = 100000
    for i in range(1, N+1):
        for j in range(max(0, i-dap), i):
            if hap[i]-hap[j] < S:
                break
            dap = min(dap, i-j)
    if dap == 100000:
        print(0)
    else:
        print(dap)


if __name__ == '__main__':
    main()