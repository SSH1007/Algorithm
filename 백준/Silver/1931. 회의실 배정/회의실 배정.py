N = int(input())
arr = []
for _ in range(N):
    a,b = map(int, input().split())
    arr.append((a,b))
arr.sort(key=lambda i : (i[1], i[0]))
dap = 0
start = arr[0][1]
for a in range(1,len(arr)):
    if arr[a][0] >= start:
        start = arr[a][1]
        dap+=1
print(dap+1)