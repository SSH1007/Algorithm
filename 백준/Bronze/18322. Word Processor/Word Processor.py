import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N, K = map(int, input().split())
    words = list(input().split())
    tmp, dap = [], []
    for n in range(N):
        tmp.append(words[n])
        if sum([len(t) for t in tmp]) > K:
            a = tmp.pop()
            if tmp:
                dap.append(tmp)
            tmp = [a]
    dap.append(tmp)
    for d in dap:
        print(*d)


if __name__ == '__main__':
    main()