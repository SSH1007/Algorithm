import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque


def main():
    dr = [-1, 0, 0, 1]
    dc = [0, -1, 1, 0]

    def find(r, c):
        if parent[r][c] == (r, c):
            return r, c
        parent[r][c] = find(parent[r][c][0], parent[r][c][1])
        return parent[r][c]

    def union(r1, c1, r2, c2):
        rr, cc = find(r1, c1)
        rrr, ccc = find(r2, c2)
        if rr == rrr and cc == ccc:
            return
        parent[r2][c2] = (r1, c1)

    def isUnion(r1, c1, r2, c2):
        rr, cc = find(r1, c1)
        rrr, ccc = find(r2, c2)
        if rr == rrr and cc == ccc:
            return True
        return False

    T = int(input())
    for t in range(1, T+1):
        H, W = map(int, input().split())
        # 물은 근접한 4방향으로 떨어진다
        # 근접한 구역 중 보다 낮은 곳이 없을 경우, 이곳은 구멍이라 부른다
        # 물은 4방향 중 가장 낮은 곳으로 떨어진다
        # 모두 같으면 북서동남 순으로 가장 낮은 곳으로 떨어진다.
        basin = [['' for _ in range(W)] for _ in range(H)]

        parent = [[[] for _ in range(W)] for _ in range(H)]

        for h in range(H):
            for w in range(W):
                parent[h][w] = (h, w)
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
                union(r, c, h, w)

        for h in range(H):
            for w in range(W):
                isUnion(h, w, parent[h][w][0], parent[h][w][1])

        cnt = 97
        for h in range(H):
            for w in range(W):
                if basin[h][w] == '':
                    q = deque([(h, w)])
                    while q:
                        r, c = q.popleft()
                        basin[r][c] = chr(cnt)
                        for i in range(4):
                            nr = r + dr[i]
                            nc = c + dc[i]
                            if 0 <= nr < H and 0 <= nc < W:
                                if basin[nr][nc] == '':
                                    if parent[nr][nc] == parent[r][c]:
                                        q.append((nr, nc))
                    cnt += 1

        print('Case #%d:' % t)
        for b in basin:
            print(' '.join(b))


if __name__ == '__main__':
    main()