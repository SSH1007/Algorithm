import sys
input = lambda: sys.stdin.readline().rstrip()
from itertools import combinations


def main():
    # 정보 입력 & 선생님 위치 파악
    N = int(input())
    maps = [list(input().split()) for _ in range(N)]
    space = []
    teacher = []
    for i in range(N):
        for j in range(N):
            if maps[i][j] == 'X':
                space.append((i, j))
            elif maps[i][j] == 'T':
                teacher.append((i, j))

    # itertools 조합으로 장애물 설치
    comb = list(combinations(space, 3))

    # 장애물 위치에 따른 감시 회피 여부 판별
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    def check():
        for t in teacher:
            r, c = t
            for i in range(4):
                nr, nc = r, c
                while 0 <= nr < N and 0 <= nc < N:
                    # 학생과 부딪히면 감시 회피 실패
                    if maps[nr][nc] == 'S':
                        return False
                    # 장애물과 부딪히면 다른 방향 탐색으로
                    if maps[nr][nc] == 'O':
                        break
                    nr += dr[i]
                    nc += dc[i]
        # 모든 선생님의 감시에서 벗어남
        return True

    for obstacle in comb:
        for o_r, o_c in obstacle:
            maps[o_r][o_c] = 'O'

        if check():
            print('YES')
            exit(0)

        for o_r, o_c in obstacle:
            maps[o_r][o_c] = 'X'
    print('NO')


if __name__ == '__main__':
    main()