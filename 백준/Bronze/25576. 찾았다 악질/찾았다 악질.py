import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N, M = map(int, input().split())
    Ls = list(map(int, input().split()))
    dap = 0
    for _ in range(N-1):
        Ks = list(map(int, input().split()))
        tmp = 0
        for m in range(M):
            tmp += abs(Ls[m]-Ks[m])
        if tmp > 2000:
            dap += 1
    print('YES' if dap >= (N-1)/2 else 'NO')


if __name__ == '__main__':
    main()