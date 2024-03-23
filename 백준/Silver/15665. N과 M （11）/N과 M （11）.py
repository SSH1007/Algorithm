N, M = map(int, input().split())
lst = sorted(list(map(int, input().split())))
lstSet = set()
tmp = []


def DFS(start):
    if len(tmp) == M:
        lstSet.add(tuple(tmp))
        return
    for i in range(N):
        tmp.append(lst[i])
        DFS(start + 1)
        tmp.pop()


DFS(0)
lstSlst = sorted(list(lstSet))
for l in lstSlst:
    print(*l)