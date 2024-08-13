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
            rootX += 1


def main():
    N = int(input())
    M = int(input())

    parent = [i for i in range(N+1)]
    rank = [0]*(N+1)

    info = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if info[i][j]:
                union(parent, rank, i+1, j+1)

    for i in range(1, N+1):
        find(parent, i)

    plan = list(map(int, input().split()))
    for i in range(M-1):
        if parent[plan[i]] != parent[plan[i+1]]:
            print('NO')
            exit(0)
    else:
        print('YES')
        

if __name__ == '__main__':
    main()