N, M = map(int, input().split())
lst = list(set(list(map(int, input().split()))))
lst.sort()
result = [0 for _ in range(M)]


def DFS(idx, start):
    if idx == M:
        print(*result)
        return
    for i in range(start, len(lst)):
        result[idx] = lst[i]
        DFS(idx+1, i)


DFS(0, 0)