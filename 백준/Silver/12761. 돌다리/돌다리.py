import sys
input = sys.stdin.readline
from collections import deque


def main():
    # 0 <= N, M <= 100000
    A, B, N, M = map(int, input().rstrip().split())
    visited = [0]*100001
    q = deque()
    q.append(N)
    visited[N] = 1
    while q:
        now = q.popleft()
        for i in [1, -1, A, -A, B, -B, now*(A-1), now*(B-1)]:
            move = now + i
            if 0 <= move <= 100000 and not visited[move]:
                q.append(move)
                visited[move] = visited[now]+1
    print(visited[M]-1)


if __name__ == '__main__':
    main()