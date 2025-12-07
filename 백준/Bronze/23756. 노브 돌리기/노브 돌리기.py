import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N = int(input())
    A = int(input())
    dap = 0
    for _ in range(N):
        a = int(input())
        dap += min((A-a)%360, (a-A)%360)
        A = a
    print(dap)


if __name__ == '__main__':
    main()