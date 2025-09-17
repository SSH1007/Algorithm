import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N, X = map(int, input().split())
    dap = 0
    for _ in range(N):
        S, T = map(int, input().split())
        if S + T > X:
            continue
        dap = max(dap, S)
    if dap:
        print(dap)
    else:
        print(-1)


if __name__ == '__main__':
    main()