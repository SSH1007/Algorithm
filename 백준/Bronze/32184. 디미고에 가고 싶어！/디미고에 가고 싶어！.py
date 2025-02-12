import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    A, B = map(int, input().split())
    dap = 0
    if A%2 == 0:
        dap += 1
        A += 1
    for i in range(A, B+1, 2):
        dap += 1
    print(dap)


if __name__ == '__main__':
    main()