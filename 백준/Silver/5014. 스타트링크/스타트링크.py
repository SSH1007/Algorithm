from collections import deque
F, S, G, U, D = map(int, input().split())
move = [0]*(F+1)
move[S] = 1
q = deque([S])
while q:
    floor = q.popleft()
    if floor == G:
        print(move[G]-1)
        break
    for go in [floor+U, floor-D]:
        if go > F or go <= 0:
            continue
        if move[go] == 0:
            move[go] = move[floor]+1
            q.append(go)
else:
    print('use the stairs')