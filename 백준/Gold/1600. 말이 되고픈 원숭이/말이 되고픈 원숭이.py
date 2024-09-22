import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque


def main():
    m_dr = [1, -1, 0, 0]
    m_dc = [0, 0, 1, -1]
    h_dr = [-1, -2, -2, -1, 1, 2, 2, 1]
    h_dc = [-2, -1, 1, 2, 2, 1, -1, -2]
    K = int(input())
    W, H = map(int, input().split())
    maps = [list(map(int, input().split())) for _ in range(H)]
    visited = [[[0]*W for _ in range(H)] for _ in range(K+1)]

    q = deque([(0, 0, 0)])
    visited[0][0][0] = 1
    while q:
        r, c, h_cnt = q.popleft()
        if r == H-1 and c == W-1:
            print(visited[h_cnt][r][c]-1)
            return
        for i in range(4):
            nr = r + m_dr[i]
            nc = c + m_dc[i]
            if 0 <= nr < H and 0 <= nc < W:
                if not visited[h_cnt][nr][nc] and not maps[nr][nc]:
                    q.append((nr, nc, h_cnt))
                    visited[h_cnt][nr][nc] = visited[h_cnt][r][c] + 1
        if h_cnt < K:
            for i in range(8):
                nr = r + h_dr[i]
                nc = c + h_dc[i]
                if 0 <= nr < H and 0 <= nc < W:
                    if not visited[h_cnt+1][nr][nc] and not maps[nr][nc]:
                        q.append((nr, nc, h_cnt+1))
                        visited[h_cnt+1][nr][nc] = visited[h_cnt][r][c] + 1
    else:
        print(-1)


if __name__ == '__main__':
    main()