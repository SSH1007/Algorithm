import sys
input = lambda: sys.stdin.readline().rstrip()
import heapq


def main():
    N, E = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(E):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))
        graph[b].append((a, c))
    v1, v2 = map(int, input().split())
    inf = int(1e9)

    def dijkstra(s, e):
        distance = [inf for _ in range(N+1)]
        distance[s] = 0
        hq = []
        heapq.heappush(hq, (0, s))
        while hq:
            dist, cur = heapq.heappop(hq)
            if dist > distance[cur]:
                continue
            for node in graph[cur]:
                cost = dist + node[1]
                if distance[node[0]] > cost:
                    distance[node[0]] = cost
                    heapq.heappush(hq, (cost, node[0]))

        return distance[e]

    A = dijkstra(1, v1)
    B = dijkstra(v1, v2)
    C = dijkstra(v2, N)
    E = dijkstra(1, v2)
    F = dijkstra(v2, v1)
    G = dijkstra(v1, N)
    dap = min(A+B+C, E+F+G)
    if dap >= inf:
        print(-1)
    else:
        print(dap)


if __name__ == '__main__':
    main()