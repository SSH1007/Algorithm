import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N, K = map(int, input().split())
    As = list(map(int, input().split()))
    k = 0
    for n in range(N-1, 0, -1):
        m, idx = 0, 0
        for i in range(n, -1, -1):
            if As[i] > m:
                m = As[i]
                idx = i
        if idx != n:
            As[n], As[idx] = As[idx], As[n]
            k += 1
            if k == K:
                print(As[idx], As[n])
                return
    else:
        print(-1)


if __name__ == '__main__':
    main()