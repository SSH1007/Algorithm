from collections import deque
N, K = map(int, input().split())
q = deque([N])
move = [0]*100001
visited = [False] * 100001
visited[N] = True

while q:
    point = q.popleft()
    if point == K:
        break
    for i in range(3):
        if i == 0 and point*2 < 100001:
            if not visited[point*2]:
                move[point*2] = move[point]
                visited[point*2] = True
                q.append(point*2)
        elif i == 1 and point-1 >= 0:
            if not visited[point-1]:
                move[point-1] = move[point]+1
                visited[point-1] = True
                q.append(point-1)
        elif i == 2 and point+1 < 100001:
            if not visited[point+1]:
                move[point+1] = move[point]+1
                visited[point+1] = True
                q.append(point+1)

print(move[K])