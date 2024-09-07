import sys
input = sys.stdin.readline


def main():
    N, K = map(int, input().split())
    lvs = [int(input()) for _ in range(N)]
    l, r = 0, 1000000001
    while l <= r:
        mid = (l+r)//2
        tmp = 0
        for lv in lvs:
            if lv < mid:
                tmp += (mid-lv)
        if tmp > K:
            r = mid-1
        else:
            l = mid+1
    print(r)


if __name__ == '__main__':
    main()