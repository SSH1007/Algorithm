import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    while 1:
        try:
            M, P, L, E, R, S, N = map(int, input().split())
            for n in range(N):
                cM = M
                M = P//S
                P = L//R
                L = cM*E
            print(M)
        except:
            break


if __name__ == '__main__':
    main()