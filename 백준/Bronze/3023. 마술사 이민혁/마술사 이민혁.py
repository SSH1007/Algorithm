from copy import deepcopy
R, C = map(int, input().split())
design = [list(input()) for _ in range(R)]
A, B = map(int, input().split())
All = []
for d in design:
    All.append(d+d[::-1])
cop = deepcopy(All)
All += cop[::-1]
if All[A-1][B-1] == '#':
    All[A-1][B-1] = '.'
else:
    All[A-1][B-1] = '#'

for a in All:
    print(''.join(a))