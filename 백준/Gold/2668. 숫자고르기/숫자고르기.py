import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N = int(input())
    lst = [[] for _ in range(N+1)]
    for n in range(1, N+1):
        lst[int(input())].append(n)
    # 시작점으로 다시 돌아오면(사이클) 조건을 만족시키는 정수 집합이 된다

    def DFS(start, node):
        visited[node] = 1
        stack = [node]
        while stack:
            v = stack.pop()
            for next in lst[v]:
                if visited[next] and next == start:
                    dap.append(next)
                elif not visited[next]:
                    stack.append(next)
                    visited[next] = 1

    dap = []
    for i in range(1, N+1):
        visited = [0]*(N+1)
        DFS(i, i)

    print(len(dap))
    for d in sorted(dap):
        print(d)


if __name__ == '__main__':
    main()