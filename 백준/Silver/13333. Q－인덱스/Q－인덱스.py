import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N = int(input())
    Ns = sorted(list(map(int, input().split())))
    dap = 0
    for n in range(N, -1, -1):
        if Ns[-n] >= n:
            dap = n
            break
    print(dap)


if __name__ == '__main__':
    main()