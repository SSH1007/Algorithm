import sys
input = sys.stdin.readline
H, W = map(int, input().rstrip().split())
N = int(input().rstrip())
lst = [list(map(int, input().rstrip().split())) for _ in range(N)]

# ㅡ ㅣ ㅁ
dap = 0
for i in range(N):
    for j in range(i+1, N):
        r, c = lst[i]
        y, x = lst[j]
        if ((r+y) <= H and max(c, x) <= W) or (max(r, y) <= H and (c+x) <= W):
            dap = max(dap, r*c+y*x)
        if ((r+x) <= H and max(c, y) <= W) or (max(r, x) <= H and (c+y) <= W):
            dap = max(dap, r*c+y*x)
        if ((c+y) <= H and max(r, x) <= W) or (max(c, y) <= H and (r+x) <= W):
            dap = max(dap, r*c+y*x)
        if ((c+x) <= H and max(r, y) <= W) or (max(c, x) <= H and (r+y) <= W):
            dap = max(dap, r*c+y*x)
print(dap)