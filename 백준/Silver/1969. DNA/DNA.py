import sys
input = sys.stdin.readline
N, M = map(int, input().rstrip().split())
lst = []
for _ in range(N):
    DNA = input().rstrip()
    lst.append(DNA)


def f(lst):
    dic = {}
    for l in lst:
        if not l in dic:
            dic[l] = 1
        else:
            dic[l] += 1
    tmp = sorted(dic.items(), key=lambda x:(-x[1], x[0]))
    return tmp[0][0]


ziplst = list(zip(*lst))
dap = ''
for z in ziplst:
    dap += f(list(z))
dap2 = 0
for l in lst:
    for i in range(M):
        if dap[i] != l[i]:
            dap2 += 1
print(dap, dap2, sep='\n')