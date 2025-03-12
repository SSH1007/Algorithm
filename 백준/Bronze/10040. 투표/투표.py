import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N, M = map(int, input().split())
    lst = [[0]*N for _ in range(2)]
    for n in range(N):
        A = int(input())
        lst[0][n] = A
    for _ in range(M):
        B = int(input())
        for i in range(N):
            if B >= lst[0][i]:
                lst[1][i] += 1
                break
    dap, maxVote = 0, 0
    for i in range(N):
        if lst[1][i] > maxVote:
            maxVote = lst[1][i]
            dap = i
    print(dap+1)


if __name__ == '__main__':
    main()