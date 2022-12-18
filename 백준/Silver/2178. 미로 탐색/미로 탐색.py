# 델타 탐색 문제
# 상하좌우 이동할 때, 이동할 대상 칸이
# 범위 제한을 넘기지 않고, 가봤던 곳이 아니며, 값이 1이어야 이동 가능
# 최소의 칸이므로 너비 탐색 BFS로 간다.

# 세로 크기 N(행 수), 가로 크기 M(열 수) 입력 받기
N, M = map(int, input().split())
# 미로 구조를 받는다
graph = [list(map(int, list(input()))) for _ in range(N)]
# 방문 여부 확인용 M*N 리스트 생성
visit = [[0]*M for _ in range(N)]
# deque를 쓸 것이므로 임포트
from collections import deque
# bfs 함수 정의
def bfs():
    # 시작 당시의 q 설정 = (0,0)부터 시작
    q = deque([(0,0)])
    # (0,0) 방문 체크
    visit[0][0] = 1
    # 큐에 다음으로 이동할 지점이 남아있는 동안 계속 반복
    while q:
        # 다음 이동할 지점의 x,y 추출
        x, y = q.popleft()
        # 델타 탐색
        for dx,dy in [(0,1),(0,-1),(-1,0),(1,0)]:
            nx, ny = x+dx, y+dy
            # 새로이 이동할 장소가 범위 내에 있고
            if N > nx >= 0 and M > ny >= 0:
                # 아직 가지 않은 곳이며, 이동 가능한 공간일때(값이 1)
                if visit[nx][ny] == 0 and graph[nx][ny] == 1:
                    # 큐에 다음 이동 지점 정보를 넣는다.
                    q.append((nx, ny))
                    # 방문 체크 리스트에 이동한 거리를 계산해서 넣는다.
                    visit[nx][ny] = visit[x][y] + 1
# 함수 실행
bfs()
# 방문 체크 리스트 (N,M) 위치의 이동 거리를 출력
print(visit[N-1][M-1])