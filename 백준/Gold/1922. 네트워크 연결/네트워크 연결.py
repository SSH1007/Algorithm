# 1922 네트워크 연결
# 최소 스패닝 트리 - 크루스칼 알고리즘(간선 중심 - 간선이 적은 경우)
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
        elif rank[rootX] < rank[rootY]:
            parent[rootX] = rootY
        else:
            parent[rootY] = rootX
            rank[rootX] += 1


def main():
    N = int(input())
    M = int(input())

    parent = [i for i in range(N+1)]
    rank = [0]*(N+1)
    info = []
    for _ in range(M):
        a, b, c = map(int, input().split())
        info.append((a, b, c))
    # pop()으로 가중치가 최소인 간선 정보를 뺄 것이므로
    # 가중치를 기준으로 내림차순함
    info.sort(key=lambda x: -x[2])

    dap = 0
    while info:
        s, e, cost = info.pop()
        # 사이클이 발생하지 않는 경우에만 연결
        if find(parent, s) != find(parent, e):
            union(parent, rank, s, e)
            dap += cost

    print(dap)


if __name__ == '__main__':
    main()