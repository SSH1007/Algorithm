import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N = int(input())
    buckets = [0]*101
    slst, tlst = [0]*1001, [0]*1001
    for n in range(1, N+1):
        s, t, b = map(int, input().split())
        buckets[n] = b
        slst[s] = n
        tlst[t] = n
    dap, tmp = 0, 0
    for n in range(1, 1000):
        if slst[n]:
            tmp += buckets[slst[n]]
        dap = tmp if tmp > dap else dap
        if tlst[n]:
            tmp -= buckets[tlst[n]]
    print(dap)


if __name__ == '__main__':
    main()