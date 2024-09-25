import sys
input = lambda: sys.stdin.readline().rstrip()
import heapq


def main():
    n, m, r = map(int, input().split())
    items = list(map(int, input().split()))
    inf = int(1e9)
    graph = [[] for _ in range(n+1)]
    for _ in range(r):
        a, b, l = map(int, input().split())
        graph[a].append((b, l))
        graph[b].append((a, l))

    dap = 0
    # 데이크스트라
    hq = []
    for i in range(1, n+1):
        heapq.heappush(hq, (0, i))
        distance = [inf for _ in range(n+1)]
        distance[i] = 0

        while hq:
            dist, cur = heapq.heappop(hq)
            if distance[cur] < dist:
                continue
            for node in graph[cur]:
                cost = distance[cur] + node[1]
                if distance[node[0]] > cost:
                    distance[node[0]] = cost
                    heapq.heappush(hq, (cost, node[0]))

        tmp = 0
        for i in range(1, n+1):
            if distance[i] <= m:
                tmp += items[i-1]
        dap = max(dap, tmp)
    print(dap)


if __name__ == '__main__':
    main()