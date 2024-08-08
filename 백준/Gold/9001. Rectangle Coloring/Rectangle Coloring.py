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
    T = int(input())
    result = []
    for _ in range(T):
        N = int(input())
        lst = []
        parent = [i for i in range(N)]
        rank = [0]*N
        for _ in range(N):
            x1, y1, x2, y2 = map(int, input().split())
            lst.append((x1, y1, x2, y2))
        for i in range(N):
            for j in range(i+1, N):
                # parent가 이미 같으면 함수 돌릴 필요 없지
                if parent[i] == parent[j]:
                    continue

                x1, y1, x2, y2 = lst[i][0], lst[i][1], lst[i][2], lst[i][3]
                c1, r1, c2, r2 = lst[j][0], lst[j][1], lst[j][2], lst[j][3]
                if x1 > c2:
                    continue
                elif x2 < c1:
                    continue
                elif y1 > r2:
                    continue
                elif y2 < r1:
                    continue
                union(parent, rank, i, j)

        for i in range(N):
            find(parent, i)

        result.append(len(set(parent)))
        
    for r in result:
        print(r)


if __name__ == '__main__':
    main()