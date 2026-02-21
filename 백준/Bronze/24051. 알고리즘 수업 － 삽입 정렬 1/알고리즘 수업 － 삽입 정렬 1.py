import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    d, dap = 0, 0
    for i in range(1, N):
        loc = i-1
        newI = A[i]
        while 0 <= loc and newI < A[loc]:
            A[loc+1] = A[loc]
            d += 1
            if d == K:
                dap = A[loc]
            loc -= 1
        if loc+1 != i:
            A[loc+1] = newI
            d += 1
            if d == K:
                dap = A[loc]
    print(-1 if d < K else dap)


if __name__ == '__main__':
    main()