import sys
input = lambda: sys.stdin.readline().rstrip()


def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent, rank, x, y):
    rootX = find(parent, x)
    rootY = find(parent, y)
    if rootX != rootY:
        if rank[rootX] > rank[rootY]:
            parent[rootY] = rootX
        elif rank[rootX] < rank[rootX]:
            parent[rootX] = rootY
        else:
            parent[rootY] = rootX
            rank[rootX] += 1


def main():
    V, E = map(int, input().split())
    parent = [i for i in range(V+1)]
    rank = [0]*(V+1)

    cost = list(map(int, input().split()))
    linked = [list(map(int, input().split())) for _ in range(E)]
    for A, B in linked:
        union(parent, rank, A, B)

    info = []
    for i in range(1, V+1):
        for j in range(i+1, V+1):
            if parent[i] != parent[j]:
                info.append((i, j, cost[i-1]*cost[j-1]))
    # pop으로 뒤에서부터 빼줄거니까 뒤에 작은 값이 오도록
    # 가중치 기준으로 내림차순 정렬
    info.sort(key=lambda x: -x[2])

    dap = 0
    while info:
        A, B, C = info.pop()
        # 두 정점(간선)이 사이클을 이루지 않는다면
        if find(parent, A) != find(parent, B):
            union(parent, rank, A, B)
            dap += C
    print(dap)


if __name__ == '__main__':
    main()