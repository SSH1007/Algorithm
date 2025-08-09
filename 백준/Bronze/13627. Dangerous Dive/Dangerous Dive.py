import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N, R = map(int, input().split())
    Rs = sorted(list(map(int, input().split())))
    if N == R:
        print('*')
    else:
        lst = [i for i in range(N+1)]
        for r in Rs:
            lst[r] = 0
        for l in lst:
            if l != 0:
                print(l, end=' ')


if __name__ == '__main__':
    main()