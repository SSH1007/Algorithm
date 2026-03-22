import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N = int(input())
    ans = 0
    for _ in range(N):
        I = input()
        h, m, d = int(I[:2]), int(I[3:5]), int(I[6:])
        dap = 0
        while d > 0:
            if 7 <= h < 19:
                dap += 10
            elif 19 <= h or h < 7:
                dap += 5
            m += 1
            if m > 59:
                m = 0
                h += 1
                if h > 23:
                    h = 0
            d -= 1
        ans += dap
    print(ans)


if __name__ == '__main__':
    main()