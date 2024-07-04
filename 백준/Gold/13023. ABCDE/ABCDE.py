import sys
input = sys.stdin.readline


def main():
    N, M = map(int, input().rstrip().split())
    friend = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().rstrip().split())
        # 친구관계는 양방향 그래프
        friend[a].append(b)
        friend[b].append(a)


    def DFS(start, cnt):
        if cnt == 4:
            # 이미 원하는 답을 구했으니 괜히 남은 경우의 수까지 탐색해서
            # 시간초과 되지 말고 바로 exit
            print(1)
            exit(0)
        visited[start] = 1
        for node in friend[start]:
            if not visited[node]:
                DFS(node, cnt+1)
                visited[node] = 0
        visited[start] = 0


    visited = [0]*(N+1)
    for n in range(N):
        DFS(n, 0)
    print(0)


if __name__ == '__main__':
    main()