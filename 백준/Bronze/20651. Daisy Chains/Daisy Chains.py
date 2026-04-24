import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N = int(input())
    lst = list(map(int, input().split()))
    dap = N
    for i in range(N):
        for j in range(i+1, N):
            tmp = sum(lst[i:j+1])/(j-i+1)
            for k in range(i, j+1):
                if lst[k] == tmp:
                    dap += 1
                    break
    print(dap)


if __name__ == '__main__':
    main()