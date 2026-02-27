import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N, M = map(int, input().split())
    S = input()
    for _ in range(M):
        P = input()
        i = 0
        for s in S:
            f = False
            for n in range(i, len(P)):
                if s == P[n]:
                    i = n+1
                    f = True
                    break
            if not f:
                print('false')
                break
        else:
            print('true')


if __name__ == '__main__':
    main()