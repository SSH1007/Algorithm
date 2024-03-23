N, M = map(int, input().split())
lst = sorted(list(map(int, input().split())))
tmp = []


def DFS(start):
    if len(tmp) == M:
        print(*tmp)
        return
    before = -1
    for i in range(N):
        if before != lst[i]:
            tmp.append(lst[i])
            before = lst[i]
            DFS(start+1)
            tmp.pop()


DFS(0)