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
        # 높이(랭크)가 더 높은 루트를 다른 루트의 부모로 설정
        if rank[rootX] > rank[rootY]:
            parent[rootY] = rootX
        elif rank[rootX] < rank[rootY]:
            parent[rootX] = rootY
        # 같다면 임의의 루트를 부모로 설정하고 해당 루트의 랭크 증가
        else:
            parent[rootY] = rootX
            rank[rootX] += 1


def main():
    dr = [-1, 0, 0, 1]
    dc = [0, -1, 1, 0]

    T = int(input())
    for t in range(1, T+1):
        H, W = map(int, input().split())
        # 물은 근접한 4방향으로 떨어진다
        # 근접한 구역 중 보다 낮은 곳이 없을 경우, 이곳은 구멍이라 부른다
        # 물은 4방향 중 가장 낮은 곳으로 떨어진다
        # 모두 같으면 북서동남 순으로 가장 낮은 곳으로 떨어진다.

        parent = list(range(H*W))  # 2차원 배열에서 1차원 배열로
        rank = [0]*(H*W)  # 유니온 파인드 성능 개선을 위한 rank 배열
        # rank 값을 비교하여 작은 트리를 큰 트리 밑에 붙여 전체 트리의 높이 최소화!

        info = [list(map(int, input().split())) for _ in range(H)]

        for h in range(H):
            for w in range(W):
                r, c, tmp = h, w, info[h][w]
                for i in range(4):
                    nr = h+dr[i]
                    nc = w+dc[i]
                    if 0 <= nr < H and 0 <= nc < W:
                        if tmp > info[nr][nc]:
                            tmp = info[nr][nc]
                            r, c = nr, nc
                if r != h or c != w:
                    union(parent, rank, h*W+w, r*W+c)

        basin_labels = {}
        label_cnt = ord('a')

        for h in range(H):
            for w in range(W):
                root = find(parent, h*W+w)
                if root not in basin_labels:
                    basin_labels[root] = chr(label_cnt)
                    label_cnt += 1

        result = []
        for h in range(H):
            row_result = []
            for w in range(W):
                row_result.append(basin_labels[find(parent, h*W+w)])
            result.append(' '.join(row_result))

        print('Case #%d:' % t)
        print('\n'.join(result))


if __name__ == '__main__':
    main()