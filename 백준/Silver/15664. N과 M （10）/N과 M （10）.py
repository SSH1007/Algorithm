N, M = map(int, input().split())
lst = sorted(list(map(int, input().split())))
visited = [0]*N
tmp = []


def DFS(start):
    if len(tmp) == M:
        print(*tmp)
        return
    before = -1
    for i in range(start, N):
        if not visited[i]:
            if before != lst[i]: # 중복 거르기
                before = lst[i]

                visited[i] = 1
                tmp.append(lst[i])
                # 비내림차순
                DFS(i+1)
                visited[i] = 0
                tmp.pop()


DFS(0)