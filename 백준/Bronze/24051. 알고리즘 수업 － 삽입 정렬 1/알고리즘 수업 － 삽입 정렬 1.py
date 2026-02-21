import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    d = []
    for i in range(1, N):
        loc = i-1
        newI = A[i]
        while 0 <= loc and newI < A[loc]:
            A[loc+1] = A[loc]
            d.append(A[loc])
            loc -= 1
        if loc+1 != i:
            A[loc+1] = newI
            d.append(A[loc+1])
    print(-1 if len(d) < K else d[K-1])


if __name__ == '__main__':
    main()