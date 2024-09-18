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
    cnt = 1
    while 1:
        n, m = map(int, input().split())
        if n == 0 and m == 0:
            break
        parent = [i for i in range(n+1)]
        rank = [0]*(n+1)
        cycle = set()
        for _ in range(m):
            s, e = map(int, input().split())
            if isUnion(parent, rank, s, e):
                cycle.add(s)
                cycle.add(e)

        for i in range(1, n+1):
            find(parent, i)
            
        S = set(parent)
        S.discard(0)
        for c in cycle:
            S.discard(find(parent, c))
        if S:
            L = len(S)
            if L == 1:
                print('Case %d: There is one tree.' % cnt)
            else:
                print('Case %d: A forest of %d trees.' % (cnt, L))
        else:
            print('Case %d: No trees.' % cnt)
        cnt += 1


if __name__ == '__main__':
    main()