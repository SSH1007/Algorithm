N = int(input())
lst = []
for _ in range(N):
    c, p = map(int, input().split())
    lst.append((c, p))
lst.sort(key=lambda x: (-x[0], x[1]))
dap = 0
for i in range(5, N):
    if lst[i][0] == lst[4][0] and lst[i][1] > lst[4][1]:
        dap += 1
print(dap)