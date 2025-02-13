import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    while 1:
        n = int(input())
        if n == -1:
            break
        dap, f = 0, 0
        for _ in range(n):
            s, t = map(int, input().split())
            dap += s*(t-f)
            f = t
        print(f'{dap} miles')


if __name__ == '__main__':
    main()