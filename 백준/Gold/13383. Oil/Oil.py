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
        lst = list(map(int, input().split()))
        num, tri = lst[0], lst[1:]
        degree = [0]*N

        parent = [i for i in range(N)]
        rank = [0]*N
        for i in range(0, num*3, 3):
            x, y, z = tri[i], tri[i+1], tri[i+2]
            # 각 정점에 연결된 노드(=차수)를 z만큼 더하기
            degree[x] += z
            degree[y] += z
            for _ in range(z):
                union(parent, rank, x, y)

        for i in range(N):
            find(parent, i)

        root_set = set(find(parent, i) for i in range(N) if degree[i] > 0)
        if len(root_set) > 1:
            result.append('no')
            continue
        
        # 무향 그래프일 경우, 차수가 홀수인 정점이 2개면 오일러 경로(모든 점 방문).
        # 차수가 홀수인 정점이 0개면 오일러 회로(+ 시작점=도착점).
        odd_cnt = sum(1 for d in degree if d % 2 == 1)
        if odd_cnt == 0 or odd_cnt == 2:
            result.append('yes')
        else:
            result.append('no')

    for r in result:
        print(r)


if __name__ == '__main__':
    main()