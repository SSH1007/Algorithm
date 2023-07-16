N, M = map(int, input().split())
ladder = dict()
for _ in range(N):
    x, y = map(int, input().split())
    ladder[x] = y
snake = dict()
for _ in range(M):
    u, v = map(int, input().split())
    snake[u] = v

# print(ladder)
# print(snake)

dap = 0
from collections import deque
visited = [0]*101
q = deque([1])
visited[1] = 1
while q:
    cur = q.popleft()
    # print(cur, '<= cur')
    if cur == 100:
        break
    for eye in range(1, 7):
        next = cur + eye
        # print(next,'<= next')

        if next in ladder.keys():
            # print(next, '사다리!')
            next = ladder[next]
        if next in snake.keys():
            # print(next, '뱀!')
            next = snake[next]
        # print(next, '<== next.')
        if next <= 100 and not visited[next]:
            visited[next] = visited[cur]+1
            q.append(next)
            # print(q)
print(visited[100]-1)