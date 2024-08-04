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
    n = int(input())
    m = int(input())
    parent = [i for i in range(n+1)]
    rank = [0]*(n+1)
    for _ in range(m):
        a, b = map(int, input().split())
        union(parent, rank, a, b)

    # 한번 더 돌려서 루트 노드 갱신
    for i in range(1, n+1):
        find(parent, i)

    unique_roots = len(set(find(parent, i) for i in range(1, n+1)))
    # 0은 제외
    print(unique_roots - 1)


if __name__ == '__main__':
    main()