# 플로이드 와샬 기본형
import sys
input = sys.stdin.readline
# 정점의 개수 N 입력(1 <= N <= 100)
N = int(input().rstrip())
# 대충 무한 값 설정
inf = int(1e9)
# 모든 정점끼리의 이동에 필요한 비용이 무한인(==못 가는) N*N 그래프 초기화
graph = [[inf]*N for _ in range(N)]
# 그래프의 인접행렬 입력
info = [list(map(int, input().rstrip().split())) for _ in range(N)]
# 입력받은 인접행렬 값을 그래프에 넣어준다(간선 존재 케이스만).
for i in range(N):
    for j in range(N):
        if info[i][j] != 0:
            graph[i][j] = info[i][j]
# 플로이드 와샬
for m in range(N):
    for s in range(N):
        for e in range(N):
            if graph[s][e] > graph[s][m]+graph[m][e]:
                graph[s][e] = 1
                # 본래는 s->m과 m->e의 합을 s->e에 넣어주는 거지만 본 문제는 단순히 존재여부만 따지므로 1로 고정
                # graph[s][e] = graph[s][m]+graph[m][e]
# 플로이드 와샬 알고리즘 종료 후 남아있는 inf를 0으로 바꿔준다.
for i in range(N):
    for j in range(N):
        if graph[i][j] == inf:
            graph[i][j] = 0
# 출력
for g in graph:
    print(*g)