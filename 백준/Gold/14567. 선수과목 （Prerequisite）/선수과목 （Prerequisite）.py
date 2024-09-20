import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque


def main():
    N, M = map(int, input().split())
    # 진입차수와 진출차수
    in_degree = [0]*(N+1)
    out_degree = [[] for _ in range(N+1)]
    # 학기수의 최소 값은 1학기
    dap = [1]*(N+1)
    for _ in range(M):
        A, B = map(int, input().split())
        in_degree[B] += 1
        out_degree[A].append(B)

    q = deque()
    for n in range(1, N+1):
        if in_degree[n] == 0:
            q.append(n)
    while q:
        cur = q.popleft()
        for node in out_degree[cur]:
            in_degree[node] -= 1
            if in_degree[node] == 0:
                q.append(node)
                dap[node] = max(dap[node], dap[cur]+1)
    print(*dap[1:])


if __name__ == '__main__':
    main()