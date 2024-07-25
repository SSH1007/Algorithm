import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N = int(input())
    lst = [0]*(N+1)
    for n in range(1, N+1):
        v = int(input())
        lst[n] = v
    visited = [0]*(N+1)
    # 시작점으로 다시 돌아오면 조건을 만족시키는 정수 집합이 된다

    def DFS(start, node):
        if lst[node] >= len(lst):
            return
        if visited[node]:
            if start == node:
                dap.append(node)
                return
            else:
                return
        visited[node] = 1
        DFS(start, lst[node])
        visited[node] = 0

    dap = []
    for i in range(1, N+1):
        if not visited[i]:
            DFS(i, i)

    print(len(dap))
    for d in dap:
        print(d)


if __name__ == '__main__':
    main()