import sys
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10**6)


def main():
    N, R, Q = map(int, input().split())
    connect = [[] for _ in range(N+1)]
    for _ in range(N-1):
        u, v = map(int, input().split())
        connect[u].append(v)
        connect[v].append(u)

    # 연결 정보로 트리 만들기
    tree = [[] for _ in range(N+1)]

    def makeTree(currentNode, parent):
        for node in connect[currentNode]:
            if node != parent:
                # add node to currentNode's child
                # set node's parent to currentNode
                tree[currentNode].append(node)
                makeTree(node, currentNode)

    makeTree(R, -1)

    # 서브트리에 속한 정점 수 계산하기
    size = [0]*(N+1)

    def countSubtreeNodes(currentNode):
        size[currentNode] = 1
        for Node in tree[currentNode]:
            countSubtreeNodes(Node)
            size[currentNode] += size[Node]

    countSubtreeNodes(R)

    # 쿼리 계산
    for _ in range(Q):
        print(size[int(input())])


if __name__ == '__main__':
    main()