import sys
input = sys.stdin.readline
N = int(input().rstrip())
lst = []
dicX, dicY = {}, {}
for _ in range(N):
    x, y = map(int, input().rstrip().split())
    lst.append((x, y))
    if x not in dicX:
        dicX[x] = 1
    else:
        dicX[x] += 1
    if y not in dicY:
        dicY[y] = 1
    else:
        dicY[y] += 1
dap = 0
for l in lst:
    dap += ((dicX[l[0]]-1) * (dicY[l[1]]-1))
print(dap)