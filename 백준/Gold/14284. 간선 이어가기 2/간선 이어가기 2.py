import sys
input = lambda: sys.stdin.readline().rstrip()
import heapq


def main():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))
        graph[b].append((a, c))
    s, t = map(int, input().split())
    inf = int(1e9)
    distance = [inf for _ in range(n+1)]
    distance[s] = 0
    hq = []
    heapq.heappush(hq, (0, s))
    while hq:
        dist, cur = heapq.heappop(hq)
        if dist > distance[cur]:
            continue
        for node in graph[cur]:
            cost = node[1] + dist
            if distance[node[0]] > cost:
                distance[node[0]] = cost
                heapq.heappush(hq, (cost, node[0]))
    print(distance[t])


if __name__ == '__main__':
    main()