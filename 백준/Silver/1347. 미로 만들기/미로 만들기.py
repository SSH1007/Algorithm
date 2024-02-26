N = int(input())
move = input()
# 0북 1동 2남 3서
direction = 2
maze = [[0]*101 for _ in range(101)]
r, c = 50, 50
maze[r][c] = 1
maxr, minr, maxc, minc = 50, 50, 50, 50
for m in move:
    if m == 'L':
        direction = (direction-1) % 4
    elif m == 'R':
        direction = (direction+1) % 4
    if m == 'F':
        if direction == 0:
            r += 1
            maze[r][c] = 1
            maxr = max(maxr, r)
        elif direction == 1:
            c += 1
            maze[r][c] = 1
            maxc = max(maxc, c)
        elif direction == 2:
            r -= 1
            maze[r][c] = 1
            minr = min(minr, r)
        elif direction == 3:
            c -= 1
            maze[r][c] = 1
            minc = min(minc, c)
            
for i in range(maxr, minr-1, -1):
    for j in range(minc, maxc+1):
        if maze[i][j]:
            print('.', end='')
        else:
            print('#', end='')
    print()