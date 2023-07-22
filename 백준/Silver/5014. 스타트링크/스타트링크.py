from collections import deque
F, S, G, U, D = map(int, input().split())
visited = [False for _ in range(F+1)]
visited[S] = True
move = [0]*(F+1)
q = deque([S])
while q:
    floor = q.popleft()
    if floor == G:
        print(move[G])
        break
    for go in [floor+U, floor-D]:
        if go > F or go <= 0:
            continue
        if visited[go] == False:
            visited[go] = True
            move[go] = move[floor]+1
            q.append(go)
else:
    print('use the stairs')