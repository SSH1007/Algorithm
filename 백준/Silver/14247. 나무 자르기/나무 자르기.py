import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    dap = 0
    N = int(input())
    lst = [[] for _ in range(N)]
    tree = list(map(int, input().split()))
    for n in range(N):
        lst[n].append(tree[n])
    grow = list(map(int, input().split()))
    for n in range(N):
        lst[n].append(grow[n])

    lst.sort(key=lambda x:x[1])
    for n in range(N):
        dap += lst[n][0]+(lst[n][1]*n)
    print(dap)


if __name__ == '__main__':
    main()