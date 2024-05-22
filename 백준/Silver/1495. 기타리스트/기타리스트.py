import sys
input = sys.stdin.readline
# 곡의 개수 N, 시작 볼륨 S, 최대 볼륨 M
N, S, M = map(int, input().rstrip().split())
# v[i]는 i번째 곡을 연주하기 전에 바꿀 수 있는 볼륨(+-)
V = list(map(int, input().rstrip().split()))

from collections import deque


def BFS():
    q = deque([S])
    for n in range(N):
        now_q = deque()
        for _ in range(len(q)):
            currentV = q.popleft()
            if 0 <= currentV-V[n] <= M:
                if currentV-V[n] not in now_q:
                    now_q.append(currentV-V[n])
            if 0 <= currentV+V[n] <= M:
                if currentV+V[n] not in now_q:
                    now_q.append(currentV+V[n])
        q = now_q
        if not q:
            break
    if q:
        print(max(q))
    else:
        print(-1)


BFS()