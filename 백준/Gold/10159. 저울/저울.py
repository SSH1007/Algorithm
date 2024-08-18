import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N = int(input())
    M = int(input())
    s2b = [[] for _ in range(N+1)]
    b2s = [[] for _ in range(N+1)]
    for _ in range(M):
        a, b = map(int, input().split())
        s2b[b].append(a)
        b2s[a].append(b)

    dap = [0]*(N+1)

    def DFS(cur, lst):
        dap[cur] += 1
        visited[cur] = 1
        for node in lst[cur]:
            if not visited[node]:
                visited[node] = 1
                DFS(node, lst)

    for i in range(1, N+1):
        visited = [0]*(N+1)
        DFS(i, s2b)

        visited = [0]*(N+1)
        DFS(i, b2s)

    for i in range(1, N+1):
        print(N+1-dap[i])


if __name__ == '__main__':
    main()