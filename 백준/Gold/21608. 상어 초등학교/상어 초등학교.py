import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    N = int(input())
    maps = [[0]*N for _ in range(N)]
    info = []
    info_dic = dict()
    for _ in range(N*N):
        info.append(list(map(int, input().split())))
    for data in info:
        final_info = []
        num = data[0]
        info_dic[num] = data[1:]
        for r in range(N):
            for c in range(N):
                # 이미 학생이 있는 칸이라면 패스
                if maps[r][c]:
                    continue
                std_cnt = 0
                blk_cnt = 0
                for i in range(4):
                    nr = r + dr[i]
                    nc = c + dc[i]
                    if 0 <= nr < N and 0 <= nc < N:
                        if maps[nr][nc] in data:
                            std_cnt += 1
                        if maps[nr][nc] == 0:
                            blk_cnt += 1
                    final_info.append((std_cnt, blk_cnt, r, c))
        # 1, 2, 3번 규칙에 맞게 정렬
        final_info.sort(key=lambda x: (-x[0], -x[1]))
        maps[final_info[0][2]][final_info[0][3]] = num

    dap = 0
    for r in range(N):
        for c in range(N):
            tmp = 0
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                if 0 <= nr < N and 0 <= nc < N:
                    if maps[nr][nc] in info_dic[maps[r][c]]:
                        tmp += 1
            if tmp == 0:
                continue
            dap += 10**(tmp-1)
    print(dap)


if __name__ == '__main__':
    main()