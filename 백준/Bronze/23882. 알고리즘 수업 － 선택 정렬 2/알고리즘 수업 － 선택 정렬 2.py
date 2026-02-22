import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    d = 0
    for i in range(N-1, 0, -1):
        tmp, t = 0, 0
        for j in range(i+1):
            if tmp < A[j]:
                tmp = A[j]
                t = j
        if i != t:
            d += 1
            A[i], A[t] = A[t], A[i]
            if K == d:
                print(*A)
                return
    print(-1)


if __name__ == '__main__':
    main()