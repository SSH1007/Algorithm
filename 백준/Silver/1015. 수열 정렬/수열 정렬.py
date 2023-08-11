import sys
input = sys.stdin.readline
N = int(input().rstrip())
lst = list(map(int, input().rstrip().split()))
visited = [0]*N
dap = [0]*N
slst = sorted(lst)
tmp = 0
for i in range(N):
    for j in range(N):
        if not visited[j] and slst[i] == lst[j]:
            visited[j] = 1
            dap[j] = tmp
            tmp += 1
print(*dap)