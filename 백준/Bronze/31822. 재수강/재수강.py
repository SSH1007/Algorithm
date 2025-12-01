import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    J = input()
    N = int(input())
    dap = 0
    for _ in range(N):
        G = input()
        if G[:5] == J[:5]:
            dap += 1
    print(dap)


if __name__ == '__main__':
    main()