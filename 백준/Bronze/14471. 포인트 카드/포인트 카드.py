import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N, M = map(int, input().split())
    dap, cnt = 0, 0
    lst = []
    for _ in range(M):
        A, B = map(int, input().split())
        if A < N:
            lst.append((A, B))
        else:
            cnt += 1
    lst.sort()
    while cnt < M-1:
        tmpA, tmpB = lst.pop()
        while tmpA < N:
            tmpA += 1
            tmpB -= 1
            dap += 1
        cnt += 1
    print(dap)


if __name__ == '__main__':
    main()