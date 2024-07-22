import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N = int(input())
    if N == 1:
        print('*')
    else:
        width = 4*N-3
        height = 4*N-1
        maps = [[' ']*width for _ in range(height)]

        # 가운데 3개 채우기
        maps[height//2-1][N*2-2] = '*'
        maps[height//2][N*2-2] = '*'
        maps[height//2+1][N*2-2] = '*'

        # 재귀
        def rec(r, c, cnt):
            if cnt == N:
                return
            maps[r][c+1] = '*'
            # 우
            for i in range(4*cnt):
                maps[r+i][c+2] = '*'
            # 하
            for i in range(4*cnt):
                maps[r+4*cnt][c-(4*cnt-3)+i] = '*'
            # 좌
            for i in range(4*cnt+2+1):
                maps[r-2+i][c-(2+4*(cnt-1))] = '*'
            # 상
            for i in range(4*cnt):
                maps[r-2][c-(1+4*(cnt-1))+i] = '*'

            rec(r-2, c+2, cnt+1)

        rec(height//2-1, N*2-2, 1)

        for m in maps:
            print(''.join(m).rstrip())


if __name__ == '__main__':
    main()