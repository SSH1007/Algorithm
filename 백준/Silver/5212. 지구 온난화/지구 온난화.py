import sys
input = sys.stdin.readline

R, C = map(int, input().rstrip().split())
graph = [['.']+list(input().rstrip())+['.'] for _ in range(R)]
graph.insert(0, ['.']*(C+2))
graph.append(['.']*(C+2))

for r in range(1, R+1):
    for c in range(1, C+1):
        if graph[r][c] == 'X':
            cnt = 0
            for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
                if graph[r+dr][c+dc] == '.':
                    cnt += 1
            if cnt >= 3:
                graph[r][c] = cnt

minr, maxr, minc, maxc = R, 0, C, 0
for r in range(1, R+1):
    for c in range(1, C+1):
        if graph[r][c] == 3 or graph[r][c] == 4:
            graph[r][c] = '.'
        if graph[r][c] == 'X':
            if maxr < r:
                maxr = r
            if maxc < c:
                maxc = c
            if minr > r:
                minr = r
            if minc > c:
                minc = c

for i in range(minr, maxr+1):
    for j in range(minc, maxc+1):
        print(graph[i][j], end='')
    print()