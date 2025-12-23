import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    A, B, N = map(int, input().split())
    dap = 1001
    for _ in range(N):
        a = -1
        c, num = map(int, input().split())
        cities = list(map(int, input().split()))
        for n in range(num):
            if cities[n] == A:
                a = n
            elif cities[n] == B:
                if a == -1:
                    break
                else:
                    if a < n:
                        dap = min(dap, c)
    if dap == 1001:
        dap = -1
    print(dap)


if __name__ == '__main__':
    main()