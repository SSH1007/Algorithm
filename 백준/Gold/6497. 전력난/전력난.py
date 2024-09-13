import sys
input = lambda: sys.stdin.readline().rstrip()


def find(parent, x):
    if x != parent[x]:
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
    while 1:
        M, N = map(int, input().split())
        if M == 0 and N == 0:
            break
        parent = [n for n in range(M)]
        rank = [0]*M
        info = []
        for _ in range(N):
            A, B, C = map(int, input().split())
            info.append((A, B, C))
        # 가중치기준으로 내림차순 정렬
        info.sort(key=lambda x: -x[2])

        dap = 0
        oriC = 0
        while info:
            A, B, C = info.pop()
            if find(parent, A) != find(parent, B):
                union(parent, rank, A, B)
                dap += C
            oriC += C
        print(oriC-dap)


if __name__ == '__main__':
    main()