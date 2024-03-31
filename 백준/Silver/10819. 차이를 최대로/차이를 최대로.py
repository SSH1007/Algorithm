from itertools import permutations
N = int(input())
lst = list(map(int, input().split()))
per_lst = permutations(lst, N)
dap = 0


def cha(lst):
    tmp = 0
    for i in range(1, len(lst)):
        tmp += abs(lst[i-1]-lst[i])
    return tmp


for p in per_lst:
    dap = max(dap, cha(p))
print(dap)