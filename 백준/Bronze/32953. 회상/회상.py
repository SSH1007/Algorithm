import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N, M = map(int, input().split())
    dic = dict()
    for _ in range(N):
        K = int(input())
        Ks = list(map(int, input().split()))
        for k in range(K):
            if Ks[k] not in dic:
                dic[Ks[k]] = 1
            else:
                dic[Ks[k]] += 1
    dap = 0
    for d in dic.values():
        if d >= M:
            dap += 1
    print(dap)


if __name__ == '__main__':
    main()