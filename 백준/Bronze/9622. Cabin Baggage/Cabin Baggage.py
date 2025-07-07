import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N = int(input())
    dap = 0
    for _ in range(N):
        l, w, d, k = map(float, input().split())
        if k <= 7.0:
            if (l>56 or w>45 or d>25) and l+w+d > 125:
                print(0)
            else:
                dap += 1
                print(1)
        else:
            print(0)
    print(dap)


if __name__ == '__main__':
    main()