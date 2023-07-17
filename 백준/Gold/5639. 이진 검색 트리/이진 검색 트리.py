import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
tree = []
while 1:
    try:
        node = int(input().rstrip())
        tree.append(node)
    except:
        break


# tree 리스트를 순회.
# pre2post 함수 호출 시 첫번째 파라미터 0번째 수가 root 값(예제에선 50)
# 순회 시작 시, 해당 서브 트리가 좌하향 트리(내림차순)이라고 가정하여 mid를 end+1(최대값)로 지정
# 노드 확인 중 start보다 큰 노드가 나타나면 그 노드는 우하향으로 가야 하므로 mid를 갱신
# 큰 트리를 작은 서브 트리로 분할하는 방식으로 위의 흐름을 서브 트리마다 반복
def pre2post(start, end):
    if start > end:
        return
    mid = end + 1
    for i in range(start+1, end+1):
        if tree[start] < tree[i]:
            mid = i
            break

    pre2post(start+1, mid-1)
    pre2post(mid, end)
    print(tree[start])

pre2post(0, len(tree)-1)