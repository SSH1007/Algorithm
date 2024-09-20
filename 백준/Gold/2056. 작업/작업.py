import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque


def main():
    N = int(input())
    time = [0]
    in_degree = [0]*(N+1)
    out_degree = [[] for _ in range(N+1)]
    for n in range(1, N+1):
        sec, *lst = input().split()
        time.append(int(sec))
        if len(lst) != 1:
            for i in list(map(int, lst[1:])):
                in_degree[n] += 1
                out_degree[i].append(n)
    dap = [0]*(N+1)
    q = deque()
    for n in range(1, N+1):
        if in_degree[n] == 0:
            q.append(n)
            dap[n] = time[n]
    while q:
        cur = q.popleft()
        for node in out_degree[cur]:
            in_degree[node] -= 1
            if in_degree[node] == 0:
                q.append(node)
            dap[node] = max(dap[node], dap[cur]+time[node])
    print(max(dap))


if __name__ == '__main__':
    main()