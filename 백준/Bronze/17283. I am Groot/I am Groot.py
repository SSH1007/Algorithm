import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    L = int(input())
    R = int(input())
    cur, cnt, dap = L, 2, 0
    while 1:
        cur = cur* R // 100
        if cur <= 5:
            break
        dap += cur*cnt
        cnt *= 2
    print(dap)


if __name__ == '__main__':
    main()