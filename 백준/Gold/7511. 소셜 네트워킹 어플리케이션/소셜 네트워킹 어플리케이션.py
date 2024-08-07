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
    T = int(input())
    for t in range(1, T+1):
        if t != 1:
            print()
        print('Scenario %d:' % t)

        N = int(input())

        parent = [i for i in range(N+1)]
        rank = [0]*(N+1)

        K = int(input())
        for _ in range(K):
            a, b = map(int, input().split())
            union(parent, rank, a, b)

        for i in range(1, N+1):
            find(parent, i)

        M = int(input())
        for _ in range(M):
            u, v = map(int, input().split())
            if isUnion(parent, u, v):
                print(1)
            else:
                print(0)


if __name__ == '__main__':
    main()