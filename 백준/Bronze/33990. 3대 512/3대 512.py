import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N = int(input())
    dap, cha = 0, 200
    for _ in range(N):
        rm = sum(map(int, input().split()))
        if 512 <= rm:
            if abs(512-rm) < cha:
                cha = abs(512-rm)
                dap = rm
    print(dap if dap > 0 else -1)


if __name__ == '__main__':
    main()