import sys
input = sys.stdin.readline
from collections import deque
# 데이터 입력 및 변수 초기화
N, M, T = map(int, input().rstrip().split())
dungeon = [list(map(int, input().rstrip().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]

# 검의 위치 찾기
sword = []
for n in range(N):
    for m in range(M):
        if dungeon[n][m] == 2:
            sword = [n, m]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

q = deque([(0, 0)])
while q:
    r, c = q.popleft()
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        # 던전 안을 벗어나지 않고
        if 0 <= nr < N and 0 <= nc < M:
            # 아직 방문하지 않은 벽이 아닌 곳이라면
            if not visited[nr][nc] and dungeon[nr][nc] != 1:
                visited[nr][nc] = visited[r][c] + 1
                q.append((nr, nc))

# for v in visited:
#     print(v)

# 검을 구하지 않고 벽을 돌아서 갈 경우
bare_hand = visited[N-1][M-1]
# 그람을 얻고 벽을 부수고 갈 경우
get_Gramr = visited[sword[0]][sword[1]]
with_sword = get_Gramr+(N-sword[0]-1)+(M-sword[1]-1)

# 벽을 돌아 공주한테 갈 수 있을 때
if visited[N-1][M-1]:
    if get_Gramr:
        dap = min(bare_hand, with_sword)
        if dap > T:
            print('Fail')
        else:
            print(dap)
    else:
        # 그람한테 도달 못하면 자연히 맨손으로 가는게 정답
        if bare_hand > T:
            print('Fail')
        else:
            print(bare_hand)
else:
    if get_Gramr:
        # 벽 때문에 막혀있지만 그람은 얻을 수 있을 때
        if with_sword > T:
            print('Fail')
        else:
            print(with_sword)
    else:
        # 그람에도 도달 못하면
        print('Fail')