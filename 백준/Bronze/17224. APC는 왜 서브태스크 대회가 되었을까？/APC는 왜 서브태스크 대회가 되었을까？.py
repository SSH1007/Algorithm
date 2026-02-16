import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N, L, K = map(int, input().split())
    lst = []
    for _ in range(N):
        s1, s2 = map(int, input().split())
        lst.append((s1, s2))
    lst.sort(key=lambda x: -x[1])
    dap = []
    for l in lst:
        if l[1] <= L:
            dap.append(140)
        elif l[0] <= L:
            dap.append(100)
    dap.sort(reverse=True)
    print(sum(dap[:K]))


if __name__ == '__main__':
    main()