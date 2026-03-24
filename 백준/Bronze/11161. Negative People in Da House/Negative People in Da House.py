import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    T = int(input())
    for _ in range(T):
        dap, h = 0, 0
        M = int(input())
        for _ in range(M):
            P1, P2 = map(int, input().split())
            h += P1
            if h < P2:
                dap += (P2-h)
                h = 0
            else:
                h -= P2
        print(dap)


if __name__ == '__main__':
    main()