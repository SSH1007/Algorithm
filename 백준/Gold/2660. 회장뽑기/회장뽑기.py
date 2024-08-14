import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N = int(input())
    # 2차원 배열 초기화
    inf = int(1e9)
    lst = [[inf]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if i == j:
                lst[i][j] = 0

    while 1:
        a, b = map(int, input().split())
        if a == -1 and b == -1:
            break
        lst[a-1][b-1] = 1
        lst[b-1][a-1] = 1

    for k in range(N):
        for i in range(N):
            for j in range(N):
                lst[i][j] = min(lst[i][j], lst[i][k] + lst[k][j])

    score = inf
    cand = []
    for l in lst:
        score = min(score, max(l))
    for i in range(N):
        if max(lst[i]) == score:
            cand.append(i+1)
    print(score, len(cand))
    print(*cand)


if __name__ == '__main__':
    main()