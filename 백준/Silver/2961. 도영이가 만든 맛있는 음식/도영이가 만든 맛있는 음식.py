N = int(input())
ingredient = []
for _ in range(N):
    S, B = map(int, input().split())
    ingredient.append((S, B))

dap = 1000000001
for i in range(1, 1<<N):
    s, b = 1, 0
    for j in range(N):
        if i & (1<<j):
            s *= ingredient[j][0]
            b += ingredient[j][1]
    dap = min(dap, abs(s-b))
print(dap)