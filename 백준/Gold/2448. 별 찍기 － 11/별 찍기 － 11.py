def draw_star(graph, N):
    new_graph = [[' ']*(2*N*2-1) for _ in range(N*2)]
    for i in range(N):
        new_graph[i][N:N+len(graph[i])] = graph[i]
    t = 0
    for i in range(N, 2*N):
        new_graph[i] = graph[t]+[' ']+graph[t]
        t += 1
    if t*2 == n:
        return new_graph
    return draw_star(new_graph, N*2)


graph = [[' ', ' ', '*', ' ', ' '],
         [' ', '*', ' ', '*', ' '],
         ['*', '*', '*', '*', '*']]
n = int(input())
if n == 3:
    print('\n'.join(list(map(''.join, graph))))
else:
    dap = draw_star(graph, 3)
    print('\n'.join(list(map(''.join, dap))))