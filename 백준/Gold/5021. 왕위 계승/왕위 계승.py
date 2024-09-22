import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import defaultdict, deque


def main():
    N, M = map(int, input().split())
    name = input()
    in_degree = defaultdict(list)
    in_degree[name] = [0, 1]
    out_degree = defaultdict(list)

    for _ in range(N):
        kid, dad, mom = input().split()
        in_degree[kid] = [2, 0]
        if not dad in in_degree.keys():
            in_degree[dad] = [0, 0]
        if not mom in in_degree.keys():
            in_degree[mom] = [0, 0]
        out_degree[dad].append(kid)
        out_degree[mom].append(kid)

    q = deque()
    for parent in in_degree.keys():
        if in_degree[parent][0] == 0:
            q.append(parent)

    while q:
        cur = q.popleft()
        for node in out_degree[cur]:
            in_degree[node][0] -= 1
            if in_degree[cur][1] > 0:
                in_degree[node][1] += in_degree[cur][1]
            if in_degree[node][0] == 0:
                q.append(node)
                in_degree[node][1] /= 2

    heritor = [input() for _ in range(M)]
    dap, blood = '', 0
    for h in heritor:
        if h in in_degree.keys():
            if in_degree[h][1] > blood:
                blood = in_degree[h][1]
                dap = h
    print(dap)


if __name__ == '__main__':
    main()