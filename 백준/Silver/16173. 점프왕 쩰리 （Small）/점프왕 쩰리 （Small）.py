import sys
input = sys.stdin.readline
N = int(input().rstrip())
graph = [list(map(int, input().rstrip().split())) for _ in range(N)]
visited = [[False]*N for _ in range(N)]

# dfs 함수 정의
def dfs(n, m):
    visited[n][m] = True
    # -1(도착점)까지 왔으면 더 이상 dfs를 할 이유가 없으므로 return
    if graph[n][m] == -1:
        return
    # 얼마나 이동할지를 칸의 내용에서 받아온다.
    kan = graph[n][m]
    # 델타탐색(우, 하 방면만)
    for dn, dm in [(kan, 0), (0, kan)]:
        nn = n+dn
        nm = m+dm
        if nn < N and nm < N and not visited[nn][nm]:
            dfs(nn, nm)

dfs(0, 0)
# 오른쪽 맨 아래칸 도달 여부에 따라 답 출력
if visited[N-1][N-1]:
    print('HaruHaru')
else:
    print('Hing')