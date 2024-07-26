import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    # 정보 입력 & 선생님 위치 파악
    N = int(input())
    maps = [list(input().split()) for _ in range(N)]
    teacher = []
    for i in range(N):
        for j in range(N):
            if maps[i][j] == 'T':
                teacher.append((i, j))

    # 장애물이 3개가 되면 감시 체크, 아니면 3개가 될 때까지 백트래킹
    def backTrack(cnt):
        if cnt == 3:
            if check():
                print('YES')
                exit(0)
            else:
                return
        for i in range(N):
            for j in range(N):
                if maps[i][j] == 'X':
                    maps[i][j] = 'O'
                    backTrack(cnt+1)
                    maps[i][j] = 'X'

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

    backTrack(0)
    print('NO')


if __name__ == '__main__':
    main()