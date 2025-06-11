import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    X = int(input())
    for i in range(1, X+1):
        n, d = map(int, input().split())
        I = n//d
        N = n%d
        if I==0 and N == 0:
            print(f'Case %d: %d' % (i, 0))
        elif I == 0:
            print(f'Case %d: %d/%d' % (i, N, d))
        elif N == 0:
            print(f'Case %d: %d' % (i, I))
        else:
            print(f'Case %d: %d %d/%d' % (i, I, N, d))


if __name__ == '__main__':
    main()