import sys
input = sys.stdin.readline


def main():
    # 이동횟수가 짝수면 지고, 홀수면 이긴다
    N = int(input().rstrip())
    tree = [[] for _ in range(N+1)]
    visited = [0]*(N+1)
    # 부모 노드 1은 방문하지 말아야 하므로 체크
    visited[1] = -1
    distance = [0]*(N+1)
    for _ in range(N-1):
        a, b = map(int, input().rstrip().split())
        tree[a].append(b)
        tree[b].append(a)

    # 부모 노드 1에서 시작, 부모 노드까지의 거리는 당연히 0
    stack = [(1, 0)]
    while stack:
        # 현재 위치와 부모 노드(1)과의 거리
        current, l = stack.pop()
        visited[current] = 1
        if current != 1 and len(tree[current]) == 1:
            distance[current] = l
            continue
        for newNode in tree[current]:
            if not visited[newNode]:
                stack.append((newNode, l+1))
    dap = sum(distance)
    if dap % 2:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()