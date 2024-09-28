import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque


def main():
    N, K = map(int, input().split())
    visited = [0]*(100001)
    visited[N] = 1
    cnt = 0
    q = deque()
    q.append(N)
    while q:
        cur = q.popleft()
        if cur == K:
            cnt += 1
            continue    # 동생을 찾았다면 더 이동할 필요없음
        for next in [cur+1, cur-1, cur*2]:
            if 0 <= next <= 100000:
                # 첫 방문일 경우
                if not visited[next]:
                    visited[next] = visited[cur]+1
                    q.append(next)
                # 다른 경로로 재방문한 경우(최단거리)
                elif visited[next] == visited[cur]+1:
                    q.append(next)
    print(visited[K]-1)
    print(cnt)


if __name__ == '__main__':
    main()