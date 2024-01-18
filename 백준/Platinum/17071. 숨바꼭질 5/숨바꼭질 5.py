from collections import deque
N, K = map(int, input().split())
max_point = 500000
q = deque([(N, 0)])
# -1, 1 이동 때문에 계속 제자리에 있으면서 동생을 기다리는 것이 나을 수가 있다.
# 제자리에 있는 것은 2초마다. 따라서 시간을 짝수 시간과 홀수 시간으로 나누어 생각한다.
# visited[0][n] = 수빈이가 짝수 시간(0, 2, 4초...)에 위치 n을 방문한 최소시간
# visited[1][n] = 수빈이가 홀수 시간(1, 3, 5초...)에 위치 n을 방문한 최소시간
# 초기화 숫자인 -1은 아직 모른다는 미지수를 의미
visited = [[-1]*(max_point+1) for _ in range(2)]
# 시작인 0초(짝수) 지점인 N으로 수빈이가 방문하는 가장 빠른 시간은 당연히 0초이다.
visited[0][N] = 0


def BFS():
    while q:
        sx, d = q.popleft()
        odd_even = d % 2
        for nx in [sx-1, sx+1, sx*2]:
            if 0 <= nx <= max_point and visited[1-odd_even][nx] == -1:
                visited[1-odd_even][nx] = d+1
                q.append((nx, d+1))


BFS()
sec = 0
for i in range(max_point+1):
    K += i
    if K > max_point:
        sec = -1
        break
    if visited[i%2][K] <= sec:
        break
    sec += 1
print(sec)