import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    T = int(input())
    for _ in range(T):
        n, k, t, m = map(int, input().split())
        # 팀당 문제별 점수(n*k), 팀당 제출횟수(n), 팀당 제출시간(n)
        score = [[0]*(k+1) for _ in range(n+1)]
        cnt = [0]*(n+1)
        time = [0]*(n+1)
        for M in range(1, m+1):
            i, j, s = map(int, input().split())
            score[i][j] = max(score[i][j], s)
            cnt[i] = cnt[i]+1
            time[i] = M

        lst = []
        for N in range(1, n+1):
            lst.append((N, sum(score[N]), cnt[N], time[N]))
        lst.sort(key= lambda x: (-x[1], x[2], x[3]))
        dap = 1
        for l in lst:
            if l[0] == t:
                break
            dap += 1
        print(dap)


if __name__ == '__main__':
    main()