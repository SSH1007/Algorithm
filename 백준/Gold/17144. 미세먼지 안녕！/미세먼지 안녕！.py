import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]

    flow_dr = [1, 0, -1, 0]
    flow_dc = [0, 1, 0, -1]

    R, C, T = map(int, input().split())
    maps = [list(map(int, input().split())) for _ in range(R)]

    # 공기청정기 찾기
    air_filter = []
    for r in range(R):
        for c in range(C):
            if maps[r][c] == -1:
                air_filter.append((r, c))

    # 1초마다 순서대로 진행
    for _ in range(T):
        # 확산된 먼지 기록
        diff = [[0]*C for _ in range(R)]
        for r in range(R):
            for c in range(C):
                if maps[r][c] > 4:
                    diff[r][c] = maps[r][c]//5
        for r in range(R):
            for c in range(C):
                if maps[r][c] == 0:
                    continue
                for i in range(4):
                    nr = r + dr[i]
                    nc = c + dc[i]
                    if 0 <= nr < R and 0 <= nc < C:
                        if maps[nr][nc] != -1:
                            maps[r][c] -= diff[r][c]
                            maps[nr][nc] += diff[r][c]
                            
        # 상단
        r, c = air_filter[0]
        cur_r, cur_c = r-1, c
        k = 2
        while 1:
            nr = cur_r + flow_dr[k]
            nc = cur_c + flow_dc[k]

            if 0 > nr or nr > r or 0 > nc or nc >= C:
                k -= 1
                if k < 0:
                    k = 3
                continue

            if maps[nr][nc] == -1:
                maps[cur_r][cur_c] = 0
                break

            maps[cur_r][cur_c] = maps[nr][nc]
            cur_r, cur_c = nr, nc

        # 하단
        r, c = air_filter[1]
        cur_r, cur_c = r+1, c
        k = 0
        while 1:
            nr = cur_r + flow_dr[k]
            nc = cur_c + flow_dc[k]

            if r > nr or nr >= R or 0 > nc or nc >= C:
                k += 1
                continue

            if maps[nr][nc] == -1:
                maps[cur_r][cur_c] = 0
                break

            maps[cur_r][cur_c] = maps[nr][nc]
            cur_r, cur_c = nr, nc
    dap = 0
    for m in maps:
        dap += sum(m)
    print(dap+2)


if __name__ == '__main__':
    main()