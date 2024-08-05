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


def isUnion(parent, x, y):
    rootX = find(parent, x)
    rootY = find(parent, y)
    if rootX == rootY:
        return True
    return False


def main():
    N, M, Q = map(int, input().split())

    parent = [i for i in range(N+1)]
    rank = [0]*(N+1)

    for _ in range(M):
        a, b = map(int, input().split())
        union(parent, rank, a, b)
    for _ in range(Q):
        x, y = map(int, input().split())
        if isUnion(parent, x, y):
            print('Y')
        else:
            print('N')


if __name__ == '__main__':
    main()