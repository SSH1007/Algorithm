import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N = int(input())
    X, S = map(int, input().split())
    dap = 0
    for _ in range(N):
        c, p = map(int, input().split())
        if c <= X and dap < p:
            dap = p
    if dap > S:
        print('YES')
    else:
        print('NO')


if __name__ == '__main__':
    main()