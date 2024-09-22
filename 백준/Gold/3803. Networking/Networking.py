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
    while 1:
        lst = list(map(int, input().split()))
        if len(lst) == 1:
            break
        N, M = lst[0], lst[1]
        parent = [i for i in range(N+1)]
        rank = [0]*(N+1)
        q = []
        for _ in range(M):
            A, B, cost = map(int, input().split())
            q.append((A, B, cost))
        q.sort(key=lambda x: -x[2])
        _ = input()

        dap = 0
        while q:
            A, B, cost = q.pop()
            if not isUnion(parent, rank, A, B):
                dap += cost
        print(dap)


if __name__ == '__main__':
    main()