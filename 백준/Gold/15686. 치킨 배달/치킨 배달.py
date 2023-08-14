import sys
input = sys.stdin.readline
N, M = map(int, input().rstrip().split())
city = []
for _ in range(N):
    city.append(list(map(int, input().rstrip().split())))

chick = []
house = []
# 치킨집, 집 위치 검색
for i in range(N):
    for j in range(N):
        if city[i][j] == 2:
            chick.append((i, j))
        elif city[i][j] == 1:
            house.append((i, j))

visited = [0]*(len(chick)+1)
stack = []
chick_d = []


def DFS(start):
    if len(stack) == M:
        # print(stack)
        cd = [200]*len(house)
        for h in range(len(house)):
            for s in stack:
                cd[h] = min(cd[h], abs(house[h][0]-s[0]) + abs(house[h][1]-s[1]))
        # print(cd)
        chick_d.append(sum(cd))
        return
    for i in range(start, len(chick)):
        if not visited[i]:
            visited[i] = 1
            stack.append(chick[i])
            DFS(i+1)
            stack.pop()
            visited[i] = 0


DFS(0)
print(min(chick_d))