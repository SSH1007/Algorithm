n, k = map(int, input().split())
dic = dict()


def DFS(hap, lst):
    if hap > n:
        return
    if hap == n:
        dic[tuple(lst)] = 1
        return
    if tuple(lst) in dic:
        return
    for i in [1, 2, 3]:
        lst.append(i)
        DFS(hap+i, lst)
        lst.pop()
    return


DFS(0, [])
k_lst = list(dic.keys())
if k > len(k_lst):
    print(-1)
else:
    print('+'.join(map(str, k_lst[k-1])))