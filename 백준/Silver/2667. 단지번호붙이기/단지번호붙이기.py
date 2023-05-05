# input 속도 증가를 위한 import
import sys
input = sys.stdin.readline
# 지도의 크기 N 입력
N = int(input().rstrip())
# 지도 정보 입력
graph = [list(map(int, input().rstrip())) for _ in range(N)]

# DFS 정의
def dfs(x, y):
    global houseCnt
    # 좌표가 범위 넘어서면 False 반환
    if x < 0 or x >= N or y < 0 or y >= N:
        return False
    # 집이 있으면 재귀 후 최종적으로 True 반환
    if graph[x][y]:
        # 재방문 방지
        graph[x][y] = 0
        # 델타 탐색 (재귀)
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx = x+dx
            ny = y+dy
            dfs(nx, ny)
        # 집 개수 +1
        houseCnt += 1
        return True
    # 집이 없으면 False 반환
    return False

houseCnt = 0
danjis = []
# x,y로 순회하면서 DFS 실행
for x in range(N):
    for y in range(N):
        if dfs(x, y):
            # 단지 리스트에 각 단지내 집 개수 삽입
            danjis.append(houseCnt)
            # 각 단지내 집 개수 카운터 초기화
            houseCnt = 0

print(len(danjis))
for d in sorted(danjis):
    print(d)