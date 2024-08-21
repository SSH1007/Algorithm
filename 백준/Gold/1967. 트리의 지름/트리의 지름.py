import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    n = int(input())
    tree = [[] for _ in range(n+1)]
    if n == 1:
        print(0)
        exit(0)
    for _ in range(n-1):
        # 부모, 자식, 가중치
        a, b, c = map(int, input().split())
        tree[a].append((b, c))
        tree[b].append((a, c))

    # 루트 노드인 1에서 가장 먼 노드를 구하고,
    # 그 노드에서 가장 먼 노드와의 거리를 구하면 그게 트리의 지름
    visited = [0 for _ in range(n+1)]
    visited[1] = 1
    leaves = []
    stack = []
    stack.append((1, 0))
    while stack:
        to, v = stack.pop()
        if len(tree[to]) == 1:
            leaves.append((to, v))
        for kid, kid_v in tree[to]:
            if not visited[kid]:
                stack.append((kid, kid_v+v))
                visited[kid] = 1
    leaves.sort(key=lambda x: x[1])
    s = leaves[-1]

    # s에서 가장 먼 노드까지의 거리 중 최댓값 구하기
    visited1 = [0 for _ in range(n+1)]
    visited1[s[0]] = 1
    stack1 = []
    stack1.append((s[0], 0))
    dap = -1
    while stack1:
        to, v = stack1.pop()
        dap = max(dap, v)
        for link, link_v in tree[to]:
            if not visited1[link]:
                stack1.append((link, link_v+v))
                visited1[link] = 1
    print(dap)


if __name__ == '__main__':
    main()