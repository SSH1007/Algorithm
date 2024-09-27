import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque


def main():
    N, K = map(int, input().split())
    visited = [-1]*100001
    q = deque()
    q.append((N, 0))
    visited[N] = 0
    while q:
        cur, time = q.popleft()
        if cur == K:
            print(time)
            tmp = [cur]
            while cur != N:
                tmp.append(visited[cur])
                cur = visited[cur]
            print(*tmp[::-1])
            break
        if cur+1 <= 100000 and visited[cur+1] == -1:
            q.append((cur+1, time+1))
            visited[cur+1] = cur
        if cur-1 >= 0 and visited[cur-1] == -1:
            q.append((cur-1, time+1))
            visited[cur-1] = cur
        if cur*2 <= 100000 and visited[cur*2] == -1:
            q.append((cur*2, time+1))
            visited[cur*2] = cur


if __name__ == '__main__':
    main()