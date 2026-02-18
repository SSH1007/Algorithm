import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N = int(input())
    Ns = sorted(list(map(int, input().split())))
    for n in range(N):
        if Ns[n] != n+1:
            print(n+1)
            return
    else:
        print(N+1)


if __name__ == '__main__':
    main()