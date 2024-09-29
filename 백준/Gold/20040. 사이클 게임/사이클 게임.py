import sys
input = lambda: sys.stdin.readline().rstrip()


def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


def isUnion(parent, rank, x, y):
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
        return False
    return True


def main():
    n, m = map(int, input().split())
    parent = [i for i in range(n+1)]
    rank = [0]*(n+1)
    for i in range(1, m+1):
        A, B = map(int, input().split())
        if isUnion(parent, rank, A, B):
            print(i)
            return
    print(0)


if __name__ == '__main__':
    main()