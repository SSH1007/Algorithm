import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque


dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]


def main():
    maps = [list(input()) for _ in range(12)]
    dap = 0
    while 1:
        # 매번 돌면서 맨 아래에 뿌요가 있는지 확인
        bottomCnt = 0
        for i in range(6):
            if maps[11][i] != '.':
                bottomCnt += 1
        # 밑에 아무것도 없으면 종료
        if bottomCnt == 0:
            break

        burstDic = dict()
        for i in range(11, -1, -1):
            for j in range(6):
                if maps[i][j] not in burstDic and maps[i][j] != '.':
                    q = deque([(i, j)])
                    burstDic[maps[i][j]+str((i, j))] = [(i, j)]
                    while q:
                        r, c = q.popleft()
                        for k in range(4):
                            nr = r + dr[k]
                            nc = c + dc[k]
                            if 0 <= nr < 12 and 0 <= nc < 6:
                                if maps[nr][nc] == maps[i][j]:
                                    if (nr, nc) not in burstDic[maps[i][j]+str((i, j))] and maps[nr][nc] != '.':
                                        q.append((nr, nc))
                                        burstDic[maps[i][j]+str((i, j))].append((nr, nc))

        # 뿌요 색마다 델타탐색으로 개수를 세서 4개 이상이면 삭제
        # 터진 열은 따로 센 뒤, 빈 공간을 채울 때 사용
        clst = set()
        for values in burstDic.values():
            if len(values) >= 4:
                for r, c in values:
                    clst.add(c)
                    maps[r][c] = '.'

        for i in range(10, -1, -1):
            for j in list(clst):
                if maps[i][j] != '.':
                    tmp = i
                    while 1:
                        tmp += 1
                        if tmp > 11 or maps[tmp][j] != '.':
                            maps[tmp-1][j], maps[i][j] = maps[i][j], maps[tmp-1][j]
                            break

        # 더 이상 터질게 없으면 종료
        if not len(clst) > 0:
            break

        # 연쇄 추가
        dap += 1
    print(dap)


if __name__ == '__main__':
    main()