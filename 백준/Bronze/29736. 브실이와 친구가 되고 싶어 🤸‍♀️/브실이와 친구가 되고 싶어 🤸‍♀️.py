import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    A, B = map(int, input().split())
    K, X = map(int, input().split())
    m, n = K+X, K-X
    dap = 0
    for i in range(A, B+1):
        if n <= i <= m:
            dap += 1
    if dap:
        print(dap)
    else:
        print('IMPOSSIBLE')


if __name__ == '__main__':
    main()