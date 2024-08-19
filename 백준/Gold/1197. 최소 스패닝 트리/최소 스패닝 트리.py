import sys
input = lambda: sys.stdin.readline().rstrip()
import heapq


def main():
    V, E = map(int, input().split())
    hq = []
    visit = set()
    graph = [[] for _ in range(V+1)]
    for _ in range(E):
        A, B, C = map(int, input().split())
        graph[A].append((B, C))
        graph[B].append((A, C))

    for to, cost in graph[1]:
        heapq.heappush(hq, (cost, to))
    visit.add(1)

    dap = 0
    while len(visit) < V:
        # 가중치가 가장 작은 정점
        cost, to = heapq.heappop(hq)
        # 이미 방문했다면 패스
        if to in visit:
            continue
        # 방문 체크
        visit.add(to)
        # 가중치 더하기
        dap += cost
        # 이동한 정점에서 다시 정보 기입
        for to, cost in graph[to]:
            heapq.heappush(hq, (cost, to))
    print(dap)


if __name__ == '__main__':
    main()