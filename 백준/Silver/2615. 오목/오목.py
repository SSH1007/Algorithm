import sys
input = sys.stdin.readline
omok = [list(input().rstrip().split()) for _ in range(19)]
lst = []
# - | \ /
dr = [0, 1, 1, -1]
dc = [1, 0, 1, 1]


def check(r, c, color):
    # 현재 위치 r, c에서 다른 색 바둑알이나, 빈 칸, 혹은 바둑판의 끝에 도달했을 때
    # 바둑알 개수가 5개면 OK (6개 이상이면 NG)
    # 델타탐색
    for i in range(4):
        # 오목 탐색
        cnt = 1
        nr = r
        nc = c
        for _ in range(4):
            nr += dr[i]
            nc += dc[i]
            if 0 <= nr < 19 and 0 <= nc < 19:
                # print(nr, nc, omok[nr][nc])
                if omok[nr][nc] == color:
                    cnt += 1
        if cnt == 5:
            if 0 <= r-dr[i] < 19 and 0 <= c-dc[i] < 19:
                if omok[r-dr[i]][c-dc[i]] == color:
                    continue
            if 0 <= nr+dr[i] < 19 and 0 <= nc+dc[i] < 19:
                if omok[nr+dr[i]][nc+dc[i]] == color:
                    continue
            # print(r, c, '방향:', i, '색', color, '알 개수', cnt)
            lst.append((r, c, color))

    return


for j in range(19):
    for i in range(19):
        if omok[i][j] != '0':
            check(i, j, omok[i][j])
if not lst:
    print(0)
else:
    lst.sort(key=lambda x: (x[1], x[0]))
    # print(lst)
    if lst[0][2] == '1':
        print(1)
    else:
        print(2)
    print(lst[0][0]+1, lst[0][1]+1)