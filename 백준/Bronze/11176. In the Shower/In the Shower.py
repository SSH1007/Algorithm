import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    T = int(input())
    for _ in range(T):
        E, N = map(int, input().split())
        dap = 0
        for _ in range(N):
            q = int(input())
            if q > E:
                dap += 1
        print(dap)


if __name__ == '__main__':
    main()