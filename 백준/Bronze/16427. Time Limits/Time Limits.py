import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    n, s = map(int, input().split())
    ms = list(map(int, input().split()))
    dap = max(ms)*s*0.001
    print(int(dap)+1 if dap%1>0 else int(dap))


if __name__ == '__main__':
    main()