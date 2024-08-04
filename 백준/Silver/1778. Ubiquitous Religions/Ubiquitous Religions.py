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
    t = 1
    while 1:
        n, m = map(int, input().split())
        if n == 0 and m == 0:
            break

        parent = [i for i in range(n+1)]
        rank = [0]*(n+1)
        for _ in range(m):
            i, j = map(int, input().split())
            union(parent, rank, i, j)

        for i in range(1, n+1):
            find(parent, i)

        print('Case {}: {}'.format(t, len(set(parent[1:]))))
        t += 1


if __name__ == '__main__':
    main()