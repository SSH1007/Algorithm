import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N = int(input())
    dap = 0
    for _ in range(N):
        S = list(map(int, input().split()))
        s = S[0]
        if s == 136:
            dap += 1000
        elif s == 142:
            dap += 5000
        elif s == 148:
            dap += 10000
        else:
            dap += 50000
    print(dap)


if __name__ == '__main__':
    main()