import sys
input = sys.stdin.readline
from collections import deque

# N:행 M:열
N, M = map(int, input().rstrip().split())
# 빙산 높이 정보
iceberg = [list(map(int, input().rstrip().split())) for _ in range(N)]
# 빙산 위치 리스트
location = []
for n in range(N):
    for m in range(M):
        if iceberg[n][m]:
            location.append((n, m))
# 델타탐색
dx = [0,-1,0,1]
dy = [-1,0,1,0]


def BFS(n, m, h):
    q = deque([(n, m, h)])
    visited[n][m] = 1
    meltinglst = []
    while q:
        nn, mm, hh = q.popleft()
        for i in range(4):
            nnn = nn + dy[i]
            nmm = mm + dx[i]
            if 0 <= nnn < N and 0 <= nmm < M:
                # 주변이 이미 바다라면 녹아야 하는 높이 +=1
                if not iceberg[nnn][nmm]:
                    hh += 1
                # 주변이 아직 방문하지 않은 빙하라면 다음 탐색 대상 큐에 삽입
                elif iceberg[nnn][nmm] and not visited[nnn][nmm]:
                    q.append((nnn, nmm, 0))
                    visited[nnn][nmm] = 1
        # 녹아야 하는 빙산이 있으면 리스트에 추가
        if hh > 0:
            meltinglst.append((nn, mm, hh))
    # 녹아야하는 빙산 리스트를 순회하며 빙산을 녹여줌
    for n, m, h in meltinglst:
        iceberg[n][m] = max(0, iceberg[n][m] - h)
    return 1


year = 0
while location:
    cnt = 0
    # 방문 그래프 초기화
    visited = [[0]*M for _ in range(N)]
    # 확인 결과 다 녹아버린 빙산 리스트
    melted = []
    # 빙산 위치 리스트 순회
    for n, m in location:
            # 방문하지 않은 빙산의 경우 BFS 실행
            if iceberg[n][m] and not visited[n][m]:
                cnt += BFS(n, m, 0)
            # 이미 다 녹았다면 melted에 추가
            if iceberg[n][m] == 0:
                melted.append((n, m))
    if cnt >= 2:
        print(year)
        break
    # 방문 예정 위치 리스트 갱신
    location = list(set(location)-set(melted))
    year += 1
else:
    print(0)