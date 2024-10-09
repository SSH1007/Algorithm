import sys
input = lambda: sys.stdin.readline().rstrip()


def check(M, lst, mid):
    low, high = lst[0], lst[0]
    cnt = 1
    for l in lst:
        low = min(low, l)
        high = max(high, l)
        if high-low > mid:
            cnt += 1
            low = l
            high = l
    return cnt <= M


def main():
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))
    s, e = 0, max(lst)
    dap = float('inf')
    while s <= e:
        mid = (s+e)//2
        if check(M, lst, mid):
            dap = min(dap, mid)
            e = mid-1
        else:
            s = mid+1
    print(dap)


if __name__ == '__main__':
    main()