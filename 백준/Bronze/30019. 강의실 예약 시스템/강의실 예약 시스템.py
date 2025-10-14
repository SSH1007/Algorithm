import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N, M = map(int, input().split())
    sch = [[1e9, 0] for _ in range(N+1)]
    for _ in range(M):
        k, s, e = map(int, input().split())
        cur_min, cur_max = sch[k][0], sch[k][1]
        if cur_min < s < cur_max:
            print('NO')
            continue
        print('YES')
        sch[k][0], sch[k][1] = min(sch[k][0], s), max(sch[k][1], e)


if __name__ == '__main__':
    main()