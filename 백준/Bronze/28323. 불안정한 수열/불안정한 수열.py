import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N = int(input())
    As = list(map(int, input().split()))
    c = As[0]%2
    dap = 1
    for i in range(1, N):
        if As[i]%2 != c:
            c = 1-c
            dap += 1
    print(dap)


if __name__ == '__main__':
    main()