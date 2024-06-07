import sys
input = sys.stdin.readline


def main():
    N, K = map(int, input().rstrip().split())
    # N = len(info)
    info = list(map(int, input().rstrip().split()))
    s, e = 0, K
    cnt = info[s:e].count(1)
    dap = 10**6
    while s <= e and e <= N:
        if cnt >= K:
            dap = min(dap, e-s)
            s += 1
            if s < e and info[s-1] == 1:
                cnt -= 1
        else:
            e += 1
            if e <= N and info[e-1] == 1:
                cnt += 1
    if dap == 10**6:
        print(-1)
    else:
        print(dap)


if __name__ == '__main__':
    main()