k = int(input())
gs = list(map(int, input().split()))
lst = []


def DFS(idx, left, right):
    lst.append(abs(right-left))
    if idx == k:
        return
    DFS(idx+1, left, right)
    DFS(idx+1, left+gs[idx], right)
    DFS(idx+1, left, right+gs[idx])


DFS(0, 0, 0)
print(sum(gs)-(len(set(lst))-1))