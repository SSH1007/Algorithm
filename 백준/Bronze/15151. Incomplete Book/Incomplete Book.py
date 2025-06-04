import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    k, d = map(int, input().split())
    dap = 0
    while d > 0:
        if d < k:
            break
        d -= k
        k *= 2
        dap += 1
    print(dap)


if __name__ == '__main__':
    main()