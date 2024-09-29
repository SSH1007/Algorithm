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
    N, M, K = map(int, input().split())
    # 친구비 Ai
    As = list(map(int, input().split()))
    parent = [i for i in range(N+1)]
    rank = [0]*(N+1)

    for _ in range(M):
        v, w = map(int, input().split())
        union(parent, rank, v, w)
    for i in range(1, N+1):
        find(parent, i)

    dic = dict()
    for n in range(1, N+1):
        if not parent[n] in dic:
            dic[parent[n]] = As[n-1]
        else:
            dic[parent[n]] = min(As[n-1], dic[parent[n]])
    cost = sum(dic.values())
    if cost > K:
        print('Oh no')
    else:
        print(cost)


if __name__ == '__main__':
    main()