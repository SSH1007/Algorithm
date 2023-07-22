from collections import deque
F, S, G, U, D = map(int, input().split())
visited = [False for _ in range(F+1)]
visited[S] = True
move = [0]*(F+1)
q = deque([S])
while q:
    floor = q.popleft()
    for go in [U, -D]:
        if floor+go > 0 and floor+go <= F:
            if visited[floor+go] == False:
                visited[floor+go] = True
                move[floor+go] = move[floor]+1
                q.append(floor+go)

if move[G] == 0 and G!=S:
    print('use the stairs')
else:
    print(move[G])