import sys
input = sys.stdin.readline
N = int(input().rstrip())
As = list(map(int, input().rstrip().split()))
opers = list(map(int, input().rstrip().split()))    # + - * //
max_v = float(-1e9)
min_v = float(1e9)


def backT(cnt, value, add, sub, mul, div):
    global max_v, min_v
    if cnt == N:
        max_v = max(max_v, value)
        min_v = min(min_v, value)
        return
    if add:
        backT(cnt+1, value+As[cnt], add-1, sub, mul, div)
    if sub:
        backT(cnt+1, value-As[cnt], add, sub-1, mul, div)
    if mul:
        backT(cnt+1, value*As[cnt], add, sub, mul-1, div)
    if div:
        backT(cnt+1, int(value/As[cnt]), add, sub, mul, div-1)
    return


backT(1, As[0], opers[0], opers[1], opers[2], opers[3])
print(max_v)
print(min_v)