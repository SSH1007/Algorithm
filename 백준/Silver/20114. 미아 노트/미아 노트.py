N, H, W = map(int, input().split())
graph = []
for _ in range(H):
    S = input()
    graph.append(S)

dap = ''

def re(w):
    global dap
    for i in range(w, w+W):
        for j in range(H):
            if graph[j][i] != '?':
                dap += graph[j][i]
                return
    dap += '?'
    return

for w in range(0, N*W, W):
    re(w)
print(dap)