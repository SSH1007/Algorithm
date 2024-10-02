import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N = int(input())
    lst = list(map(int, input().split()))
    s, e = 0, 0
    dap = 0
    dic = dict()
    while e < N:
        dic[lst[e]] = dic.get(lst[e], 0) + 1
        e += 1

        if len(dic) > 2:
            dic[lst[s]] -= 1
            if dic[lst[s]] == 0:
                del dic[lst[s]]
            s += 1

        dap = max(dap, e-s)
    print(dap)


if __name__ == '__main__':
    main()