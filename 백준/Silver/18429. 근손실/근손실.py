import sys
input = sys.stdin.readline
N, K = map(int, input().rstrip().split())
kit = list(map(int, input().rstrip().split()))
visited = [0]*N

routine = []
def perm(arr):
    global routine
    if len(arr) == N:
        routine.append(arr)
        return arr
    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            perm(arr + [kit[i]])
            visited[i] = 0
perm([])

dap = 0
for route in routine:
    tmp = 0
    for r in route:
        tmp += r
        tmp -= K
        if tmp < 0:
            break
    else:
        dap += 1
        
print(dap)