N = int(input())
graph = [[' ']*(N*2-1) for _ in range(N)]


def draw_star(r, c, N):
    if N == 3:
        graph[r][c] = '*'
        graph[r+1][c-1] = graph[r+1][c+1] = '*'
        for i in range(-2, 3):
            graph[r+2][c+i] = '*'
    else:
        newN = N//2
        draw_star(r, c, newN)
        draw_star(r+newN, c-newN, newN)
        draw_star(r+newN, c+newN, newN)


draw_star(0, N-1, N)
print('\n'.join(list(map(''.join, graph))))