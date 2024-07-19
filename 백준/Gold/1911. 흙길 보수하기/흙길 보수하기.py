import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    # 1 <= N <= 10000,  1 ≤ L ≤ 1000000
    N, L = map(int, input().split())
    lst = []
    for _ in range(N):
        a, b = map(int, input().split())
        lst.append((a, b))
    lst.sort()
    dap = 0
    # 웅덩이의 시작 포인트 기억
    point = lst[0][0]
    for s, e in lst:
        if point < s:
            point = s
        pool = e - point

        up = 1
        if pool % L == 0:
            up = 0
        cnt = pool//L + up
        point += (cnt*L)
        dap += cnt
    print(dap)


if __name__ == '__main__':
    main()