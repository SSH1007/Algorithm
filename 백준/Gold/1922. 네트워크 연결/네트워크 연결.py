# 1922 네트워크 연결
# 최소 스패닝 트리 - 프림 알고리즘(정점 중심 - 간선이 많은 경우)
import sys
input = lambda: sys.stdin.readline().rstrip()
import heapq


def main():
    N = int(input())
    M = int(input())
    graph = [[] for _ in range(N+1)]
    visit = set()
    hq = []
    for _ in range(M):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))
        graph[b].append((a, c))

     # 임의의 정점 선택
    for to, cost in graph[1]:
        heapq.heappush(hq, (cost, to))
    visit.add(1)

    dap = 0
    while len(visit) < N:
        # hq 안의 정점과 연결된 정점들 중 가장 작은 가중치를 가지는 정점 선택
        cost, to = heapq.heappop(hq)

        # 이미 방문했다면 패스
        if to in visit:
            continue

        # 최소 가중치 누적
        dap += cost
        # 방문 체크
        visit.add(to)
        # 현재 정점과 연결된 정점들의 정보 추가
        for to, cost in graph[to]:
            heapq.heappush(hq, (cost, to))
    print(dap)


if __name__ == '__main__':
    main()