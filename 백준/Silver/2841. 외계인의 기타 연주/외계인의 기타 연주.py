import sys
input = sys.stdin.readline
N, P = map(int, input().rstrip().split())
lst = [[] for _ in range(6+1)]
dap = 0
for _ in range(N):
    num, fret = map(int, input().rstrip().split())
    if lst[num]:
        while lst[num]:
            if lst[num][-1] < fret:
                lst[num].append(fret)
                dap += 1
                break
            elif lst[num][-1] > fret:
                lst[num].pop()
                dap += 1
            else:
                break
        if not lst[num]:
            lst[num].append(fret)
            dap += 1
    else:
        lst[num].append(fret)
        dap += 1
print(dap)