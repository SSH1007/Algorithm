import sys
input = sys.stdin.readline
from collections import deque
N, M, R = map(int, input().rstrip().split())
matrix = [list(map(int, input().rstrip().split())) for _ in range(N)]
answer = [[0]*M for _ in range(N)]
# 주어지는 배열은 min(N, M)//2 겹으로 되어 있다.
for i in range(min(N, M)//2):
    line = deque([])
    # 우
    line.extend(matrix[i][i+1:M-i])
    # 하
    line.extend([matrix[j][M-1-i] for j in range(i+1, N-i)])
    # 좌
    line.extend(matrix[N-1-i][i:M-1-i][::-1])
    # 상
    line.extend([matrix[j][i] for j in range(i, N-1-i)][::-1])
    # R번 회전
    line.rotate(-R)

    # 우측으로 채워넣기
    for n in range(i+1, M-i):
        answer[i][n] = line.popleft()
    # 하측으로 채워넣기
    for n in range(i+1, N-i):
        answer[n][M-1-i] = line.popleft()
    # 좌측으로 채워넣기
    for n in range(M-2-i, i-1, -1):
        answer[N-1-i][n] = line.popleft()
    # 상측으로 채워넣기
    for n in range(N-2-i, i-1, -1):
        answer[n][i] = line.popleft()
for a in answer:
    print(*a)