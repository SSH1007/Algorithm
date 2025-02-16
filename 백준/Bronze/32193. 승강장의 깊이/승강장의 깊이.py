import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N = int(input())
    dap = 0
    for _ in range(N):
        A, B = map(int, input().split())
        dap += A
        dap -= B
        print(dap)


if __name__ == '__main__':
    main()