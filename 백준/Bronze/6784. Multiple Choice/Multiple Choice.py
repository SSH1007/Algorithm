import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N = int(input())
    lst = [input() for _ in range(N)]
    dap = 0
    for i in range(N):
        if lst[i] == input():
            dap += 1
    print(dap)


if __name__ == '__main__':
    main()