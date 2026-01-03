import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N, M = map(int, input().split())
    T, S = map(int, input().split())
    n, nl = N//8, N%8
    m, ml = M//8, M%8
    Nd = N+n*S+(-S if nl == 0 else 0)
    Md = T+M+m*S+(-S if ml == 0 else 0)+T*m*2+(-T*2 if ml == 0 else 0)
    print('Zip' if Nd < Md else 'Dok')
    print(min(Nd, Md))


if __name__ == '__main__':
    main()