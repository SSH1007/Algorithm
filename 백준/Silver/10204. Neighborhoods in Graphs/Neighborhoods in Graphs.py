# 특정 점을 거쳐가야 하며, 가짓수가 비교적 적다면 플로이드 와샬
import sys
input = sys.stdin.readline
T = int(input().rstrip())
for _ in range(T):
    lst = list(input().rstrip().split())
    n, e, lst = int(lst[0]), int(lst[1]), lst[2:]   # n: 슈퍼 빌런의 수, e: 간선의 수
    vx = lst.pop()
    # 연결 그래프 그리기
    graph = [[0]*n for _ in range(n)]
    for i in range(e):
        graph[int(lst[2*i][1:])-1][int(lst[2*i+1][1:])-1] = 1
        graph[int(lst[2*i+1][1:])-1][int(lst[2*i][1:])-1] = 1
    # 플로이드 와샬
    dap = [[0]*n for _ in range(n)]
    for k in range(n):  # 경유 점
        for i in range(n):  # 출발 점
            for j in range(n):  # 도착 점
                if i == j:
                    continue
                if graph[i][j] or (graph[i][k] and graph[k][j]):
                    dap[i][j] = 1
    print('The number of supervillains in 2-hop neighborhood of %s is %d'%(vx, sum(dap[int(vx[1:])-1])))