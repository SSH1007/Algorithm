import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N = int(input())
    g = 'gori'
    S = input()
    for n in range(N):
        if S[n:n+4] == g:
            print('YES')
            return
    print('NO')


if __name__ == '__main__':
    main()