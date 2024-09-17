import sys
input = lambda: sys.stdin.readline().rstrip()


def findDepth(parent, node):
    depth = 0
    while parent[node] != 0:
        node = parent[node]
        depth += 1
    return depth


def getCommonAncestor(parent, u, v, interval):
    # u가 더 깊은 노드이므로, u를 v와 같은 깊이까지 끌어올린다.
    while interval != 0:
        u = parent[u]
        interval -= 1
    # 둘의 공통 조상을 찾아준다
    while u != v:
        u = parent[u]
        v = parent[v]
    return u


def LCA(parent, u, v):
    u_depth = findDepth(parent, u)
    v_depth = findDepth(parent, v)
    if u_depth > v_depth:
        return getCommonAncestor(parent, u, v, u_depth-v_depth)
    else:
        return getCommonAncestor(parent, v, u, v_depth-u_depth)


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        parent = [0]*(N+1)
        for _ in range(N-1):
            A, B = map(int, input().split())
            parent[B] = A
        start, end = map(int, input().split())
        print(LCA(parent, start, end))


if __name__ == '__main__':
    main()