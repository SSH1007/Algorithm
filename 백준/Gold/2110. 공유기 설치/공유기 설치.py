import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    # 2<=C<=N<=200,000
    N, C = map(int, input().split())
    # 집의 좌표가 10억까지임 -> 이분탐색
    houses = sorted([int(input()) for _ in range(N)])

    s, e = 1, houses[-1]-houses[0]
    dap = 0
    while s <= e:
        mid = (s+e)//2
        tmp = houses[0]
        cnt = 1
        for n in range(1, N):
            if houses[n]-tmp >= mid:
                tmp = houses[n]
                cnt += 1
        if cnt >= C:
            dap = mid
            s = mid+1
        else:
            e = mid-1
    print(dap)


if __name__ == '__main__':
    main()