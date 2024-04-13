N = int(input())
ingredient = []
for _ in range(N):
    S, B = map(int, input().split())
    ingredient.append((S, B))

dap = 1000000001
for i in range(1, 1<<N):
    s, b = 1, 0
    for j in range(len(bin(i)[2:].zfill(N))):
        if bin(i)[2:].zfill(N)[j] == '1':
            s *= ingredient[int(j)][0]
            b += ingredient[int(j)][1]
    dap = min(dap, abs(s-b))
print(dap)