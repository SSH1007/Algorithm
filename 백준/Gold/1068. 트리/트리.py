import sys
input = sys.stdin.readline


# 트리의 노드의 개수 N(0~50)
N = int(input().rstrip())
# 각 노드의 부모(없으면 -1)
parents = list(map(int, input().rstrip().split()))
# 지울 노드의 번호
toDelete = int(input().rstrip())

tree = [[] for _ in range(N)]
# print(tree)
root = 0
for n in range(N):
    if parents[n] >= 0:
        tree[parents[n]].append(n)
    else:
        root = n
tree[toDelete] = []
# print(tree, root)
dap = 0


def DFS(start):
    global dap
    if start == toDelete:
        return
    if not tree[start]:
        # print(start, tree[start])
        dap += 1
    elif len(tree[start]) == 1 and tree[start][0] == toDelete:
        dap += 1
    for node in tree[start]:
        DFS(node)


DFS(root)
print(dap)