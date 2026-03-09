import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    c = 0
    for i in range(N-1, 0, -1):
        for j in range(i):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
                c += 1
                if c == K:
                    print(*A)
                    return
    print(-1)


if __name__ == '__main__':
    main()