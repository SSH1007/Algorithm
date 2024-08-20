import sys
input = lambda: sys.stdin.readline().rstrip()
import heapq


def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent, cost, x, y):
    rootX = find(parent, x)
    rootY = find(parent, y)
    if rootX != rootY:
        if cost[rootX] < cost[rootY]:
            parent[rootY] = rootX
        else:
            parent[rootX] = rootY
        cost[find(parent, rootY)] = min(cost[rootX], cost[rootY])


def main():
    V, E = map(int, input().split())
    parent = [i for i in range(V+1)]

    cost = list(map(int, input().split()))
    linked = [list(map(int, input().split())) for _ in range(E)]
    for A, B in linked:
        union(parent, cost, A-1, B-1)

    info = []
    for i in range(V):
        if find(parent, i) == i:
            info.append(cost[i])

    if len(info) == 1:
        print(0)
    else:
        heapq.heapify(info)
        smallest = heapq.heappop(info)
        dap = 0
        while info:
            dap += smallest * heapq.heappop(info)

        print(dap)


if __name__ == '__main__':
    main()