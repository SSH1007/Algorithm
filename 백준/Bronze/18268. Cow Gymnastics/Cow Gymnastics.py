import sys
input = lambda: sys.stdin.readline().rstrip()


def F(i, j, lst):
    for l in lst:
        if l.index(i+1) > l.index(j+1):
            return 0
    return 1


def main():
    K, N = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(K)]
    dap = 0
    for i in range(N):
        for j in range(N):
            if i != j:
                dap += F(i, j, lst)
    print(dap)


if __name__ == '__main__':
    main()