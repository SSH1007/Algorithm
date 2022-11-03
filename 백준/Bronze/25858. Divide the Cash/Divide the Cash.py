n, d = map(int, input().split())
dap = []
solved = 0
for _ in range(n):
    a = int(input())
    solved+=a
    dap.append(a)
for i in range(n):
    print(dap[i]*(d//solved))