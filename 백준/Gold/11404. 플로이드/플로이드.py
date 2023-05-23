# 플로이드 와샬
import sys
input = sys.stdin.readline
# 도시의 개수 N 입력(1 <= N <= 100)
N = int(input().rstrip())
# 대충 무한 값 설정
inf = int(1e9)
# 모든 정점끼리의 이동에 필요한 비용이 무한인(==못 가는) N*N 그래프 초기화
graph = [[inf]*N for _ in range(N)]
# 버스의 개수 M 입력
M = int(input().rstrip())
# 그래프의 인접행렬 입력
infoList = [list(map(int, input().rstrip().split())) for _ in range(M)]
# 입력받은 인접행렬 값을 그래프에 넣어준다(간선 존재 케이스만).
for info in infoList:
    # 버스 노선 정보에 같은 노선인데 비용이 다른 케이스가 있을 수 있으므로, 되도록 최소비용을 넣도록 한다.
    if graph[info[0]-1][info[1]-1] > info[2]:
        graph[info[0]-1][info[1]-1] = info[2]

# 플로이드 와샬
for m in range(N):
    for s in range(N):
        for e in range(N):
            if s!=e and graph[s][e] > graph[s][m]+graph[m][e]:
                graph[s][e] = graph[s][m] + graph[m][e]

# 플로이드 와샬 알고리즘 종료 후 남아있는 inf를 0으로 바꿔준다.
for i in range(N):
    for j in range(N):
        if graph[i][j] == inf:
            graph[i][j] = 0
# 출력
for g in graph:
    print(*g)