import sys
input = sys.stdin.readline
K = int(input().rstrip())
building = list(map(int, input().rstrip().split()))
dic = {2: 0, 4: 1, 8: 2, 16: 3, 32: 4, 64: 5, 128: 6, 256: 7, 512: 8, 1024: 9}
dap = [[] for _ in range(K)]


def sangkeun(lst):
    dap[dic[len(lst)+1]].append(lst[len(lst)//2])
    if len(lst) == 1:
        return
    else:
        sangkeun(lst[:len(lst)//2])
        sangkeun(lst[len(lst)//2+1:])


sangkeun(building)
for i in range(K-1, -1, -1):
    print(*dap[i])