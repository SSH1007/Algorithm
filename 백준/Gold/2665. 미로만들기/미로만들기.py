import sys
input = lambda: sys.stdin.readline().rstrip()
import heapq


def main():
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]

    N = int(input())
    maps = [list(map(int, list(input()))) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]
    # 흰 방에서 출발
    visited[0][0] = 1
    hq = [[0, 0, 0]]
    while hq:
        cnt, r, c = heapq.heappop(hq)
        if r == N-1 and c == N-1:
            print(cnt)
            break
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < N:
                if visited[nr][nc] == 0:
                    visited[nr][nc] = 1
                    if maps[nr][nc] == 0:
                        heapq.heappush(hq, [cnt+1, nr, nc])
                    else:
                        heapq.heappush(hq, [cnt, nr, nc])


if __name__ == '__main__':
    main()