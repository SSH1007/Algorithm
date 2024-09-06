import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N, S = map(int, input().split())
    lst = list(map(int, input().split()))
    hap, l, r = 0, 0, 0
    dap = 100000
    while 1:
        if hap >= S:
            dap = min(dap, r - l)
            hap -= lst[l]
            l += 1
        else:
            if r == N:
                break
            hap += lst[r]
            r += 1

    if dap == 100000:
        print(0)
    else:
        print(dap)


if __name__ == '__main__':
    main()