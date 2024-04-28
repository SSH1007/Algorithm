import sys
input = sys.stdin.readline
M, N = map(int, input().rstrip().split())
lst = list(map(int, input().rstrip().split()))


def f(ist):
    dap = 0
    s, e = 1, max(ist)
    while s <= e:
        mid = (s+e)//2
        tmp = 0
        for i in ist:
            tmp += i//mid
            if tmp >= M:
                break
        if tmp >= M:
            dap = mid
            s = mid+1
        else:
            e = mid-1
    return dap


print(f(lst))